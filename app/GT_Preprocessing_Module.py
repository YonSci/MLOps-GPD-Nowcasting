import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from statsmodels.tsa.stattools import adfuller, kpss
import statsmodels.api as sm
from ipywidgets import interact, Dropdown
from ipywidgets import widgets



def GT_Preprocessing_Module():
    #  blue, green, orange, red, violet, gray/grey, rainbow.
    st.markdown(
    """
    <style>
    .title {
        background-color: lightblue;
        padding: 10px;
        border-radius: 8px;
    }
    </style>
    <div class="title">
        <h1>Google Trends Preprocessing Module</h1>
    </div>
    """,
    unsafe_allow_html=True
    
)
    
    GT_data = None
    df_GT_data = None  
    df_GT_fill = None
    same_month_data = None

    st.markdown("---")
    st.subheader("Google Trends Data Preprocessing")
    

    # Load and Read the GDP data
    st.info("Please upload google trends data with the first column as the date (YYYY-MM) format and the remaining columns google trends data .")
    GT_data = st.file_uploader(f"Please upload google trends data data in CSV or Excel file formats", type={"csv", "xlsx", "xls"}, key="loader1")
    if GT_data is not None:
        try:
            df_GT_data= pd.read_csv(GT_data)
        except Exception as e:
            df_GT_data = pd.read_excel(GT_data)
                    
        if st.button('Load the data', key="gdp_display"):
            if df_GT_data is not None:
                # Convert the date column to datetime format in YYYY-MM format
                df_GT_data['date'] = pd.to_datetime(df_GT_data['date'])

                # Change the date format to YYYY-MM
                df_GT_data['date'] = df_GT_data['date'].dt.strftime('%Y-%m')

                st.success(f'You uploaded Google Trends data successfully! 🎉🎉🎉')
                st.write(df_GT_data)
                                 
            else:
                st.write("Please first upload .csv, .xlsx, or .xls files 😔")
    
        st.session_state.df_GT_data = df_GT_data


    st.markdown("---")
    st.subheader("Check Missing Data")
        
    st.session_state.df_GT_data = df_GT_data

    if 'df_GT_data' in locals() or 'df_GT_data' in globals():
        if df_GT_data is not None:
            missing_data_count = df_GT_data.iloc[:,1:].isnull().sum()
            missing_dates = df_GT_data[df_GT_data.isnull().any(axis=1)]['date']
            if st.button('Check Missing Data', key="missing_data"):
                st.info("Missing data count by column name:")
                st.table(pd.DataFrame(missing_data_count, columns=['Missing Values']))
                if missing_dates.empty:
                    st.info("No dates have missing data.")
                else:
                    st.info("Dates with missing data:")
                    st.table(missing_dates)           
                    
    else:
        st.write("Please first upload .csv, .xlsx, or .xls files 😔")

                    
    # st.markdown("---")
    # st.subheader("Impute Missing Data")

    if df_GT_data is None:
        st.write("No data available. Please upload a file.")
    else:
        missing_data_count = df_GT_data.isnull().sum()

        if missing_data_count.sum() > 0:
            st.subheader("Impute Missing Data")
            
            filling_method = st.selectbox(
                'Select a method to fill missing data:',
                ('None','Forward fill', 'Backward fill', 'Interpolate', 'Fill with mean', 'Fill with median', 'Fill with mode', 'Fill with a specific value'),
                index=0)
            
            if filling_method != 'None':
                # Select only numeric columns for filling missing values
                numeric_cols = df_GT_data.select_dtypes(include=[np.number]).columns
                df_numeric = df_GT_data[numeric_cols]

                if filling_method == 'Forward fill':
                    df_GT_fill = df_numeric.ffill()
                elif filling_method == 'Backward fill':
                    df_GT_fill = df_numeric.bfill()
                elif filling_method == 'Interpolate':
                    df_GT_fill = df_numeric.interpolate(method='linear')
                elif filling_method == 'Fill with mean':
                    df_GT_fill = df_numeric.fillna(df_numeric.mean())
                elif filling_method == 'Fill with median':
                    df_GT_fill = df_numeric.fillna(df_numeric.median())
                elif filling_method == 'Fill with mode':
                    df_GT_fill = df_numeric.fillna(df_numeric.mode().iloc[0])
                elif filling_method == 'Fill with a specific value':
                    specific_value = st.number_input('Enter the specific value:')
                    df_GT_fill = df_numeric.fillna(specific_value)

                # Combine filled numeric columns with non-numeric columns
                df_GT_fill = pd.concat([df_GT_data.drop(columns=numeric_cols), df_GT_fill], axis=1)

                st.info("Missing data filled successfully.")
                st.write(df_GT_fill)
                
                st.download_button('Download data as CSV', 
                                df_GT_fill.to_csv(index=False),  
                                file_name=f'GT_imputed_{filling_method}.csv',
                                mime='text/csv')
               
    st.markdown("---")
    st.subheader("Plot Google Trends Data")

    # Function to plot selected columns
    def plot_selected_column(column_name):
        if column_name:
            fig1 = go.Figure()
            fig1.add_trace(go.Scatter(x=df_GT_fill_cycle.index, y=df_GT_fill_cycle[column_name], mode='lines', name=column_name))

            fig1.update_layout(title=format(column_name), xaxis_title='Date', yaxis_title='Search Volume Index [%]')
            st.plotly_chart(fig1)

    df_GT_fill_cycle = df_GT_fill.copy()
    df_GT_fill_cycle['date'] = pd.to_datetime(df_GT_fill_cycle['date'], format='%m/%d/%Y')
    df_GT_fill_cycle['date'] = df_GT_fill_cycle['date'].dt.strftime('%Y-%m')
        
    df_GT_fill_cycle.set_index('date', inplace=True)

    # Get list of column names
    column_names1 = df_GT_fill_cycle.columns.tolist()

    # Dropdown widget for selecting column
    selected_column1 = st.selectbox('Select Column:', [''] + column_names1, index=0, key='selected_column1')

    # Interactive plot using dropdown
    plot_selected_column(selected_column1)
        
        
    st.markdown("---")
    st.subheader("Make Google Trends data quarterly")
    
    if st.button('Make Data Quarterly', key='quarterly_data'):
        df_quarterly = df_GT_fill.copy()
        df_quarterly.set_index('date', inplace=True)

        # Convert the DataFrame's index to datetime format
        df_quarterly.index = pd.to_datetime(df_quarterly.index)

        # Create a new DataFrame that only includes data for the months when GDP is published
        same_month_data = df_quarterly[(df_quarterly.index.month == 4) |
                                    (df_quarterly.index.month == 7) |
                                    (df_quarterly.index.month == 10) |
                                    (df_quarterly.index.month == 1)]

        # Convert the index to 'YYYY-MM' format
        same_month_data.index = same_month_data.index.strftime('%Y-%m')
        st.session_state.same_month_data = same_month_data
        
        st.write(same_month_data)  
        st.download_button('Download data as CSV', 
                        same_month_data.to_csv(index=False),  
                        file_name=f'GT_quarterly.csv',
                        mime='text/csv')
        
    st.markdown("---")    
    st.subheader("Plot Google Trends data quarterly")
    
    def plot_selected_column(column_name):
        if column_name:
            fig1 = go.Figure()
            fig1.add_trace(go.Scatter(x=same_month_data.index, y=same_month_data[column_name], mode='lines', name=column_name))

            fig1.update_layout(title=format(column_name), xaxis_title='Date', yaxis_title='Search Volume Index [%]')
            st.plotly_chart(fig1)


    st.write
    # same_month_data_plot.set_index('date', inplace=True)
    same_month_data.index = pd.to_datetime(same_month_data.index)

    # return the index to 'YYYY-MM' format
    same_month_data.index = same_month_data.index.strftime('%Y-%m')

    # Get list of column names
    column_names = same_month_data.columns.tolist()

    # Dropdown widget for selecting column
    selected_column = st.selectbox('Select Column:', [''] + column_names, index=0, key='selected_column2')

    # Interactive plot using dropdown
    plot_selected_column(selected_column)
    
        
    

    
            
        
    




    
        
        
        
    st.markdown("---")
    st.subheader("Remove downward trend bias")
    
    # # # Define the function get_long_term_trend
    # # def get_long_term_trend(dataframe, freq='M'):
        
    # #     # Apply natural logarithm to the input DataFrame
    # #     dataframe = np.log(dataframe)
        
    # #     # Create empty DataFrames for storing long-term trend and cycle components
    # #     long_term_trend_data = dataframe.copy()
    # #     cycle_data = dataframe.copy()
        
    # #     # Determine the lambda parameter based on the frequency
    # #     if freq == 'Q':
    # #         lamb = 1600
    # #     elif freq == 'M':
    # #         lamb = 1600 * 3 ** 4
        
    # #     # Iterate over each column in the DataFrame
    # #     for column_name in dataframe.columns:
            
    # #         # Apply Hodrick-Prescott filter to the current column
    # #         cycle, trend = sm.tsa.filters.hpfilter(dataframe[column_name], lamb)
            
    # #         # Update the corresponding column in the long-term trend DataFrame with the trend component
    # #         long_term_trend_data[column_name] = trend
            
    # #         # Update the corresponding column in the cycle DataFrame with the cycle component
    # #         cycle_data[column_name] = cycle
        
    # #     # Return the DataFrames containing the long-term trend and cycle components
    # #     return long_term_trend_data, cycle_data
    
    # # get_long_term_trend(df_GT_data, freq='M')

    
    
    # # trend_data = get_long_term_trend(gdp_categoryts_df, freq)
    # # log_category = np.log(dataframe)
    # # log_category.replace([np.inf, -np.inf], 0, inplace=True)
    # # avg_logcategory = log_category.mean()
    # # pca = PCA(n_components=1)
    # # pca.fit(trend_data)
    # # component = pd.DataFrame(pca.fit_transform(trend_data))
    # # rescaled_component = avg_logcategory.mean() + (component - component.mean())*(avg_logcategory.std()/component.std())
    # # transformed_data = log_category - rescaled_component.values
    # # transformed_data.index = pd.to_datetime(transformed_data.index)
    
    
    
    
    
    
    
    st.markdown("---")
    st.subheader("Normalize Google Trends series")
    
    
        
    st.markdown("---")
    st.subheader("Detrend Google Trends series")
    
    
    st.markdown("---")
    st.subheader("Remove seasonality from Google Trends series")
    
    st.markdown("---")
    st.subheader("Adjusting for breaks in Google Trends series")




    
  
    
    
    
    
    
    
    
    
    


   
        
        



    
    





# Plot for GDP

# Calculate GDP Growth Rate

# Plot for GDP growth rate

# Check for stationarity

# Convert the GDP time series data into stationary
        
if __name__ == "__main__":
    GT_Preprocessing_Module()