import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from statsmodels.tsa.stattools import adfuller, kpss

def GDP_Preprocessing_Module():
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
        <h1>GDP Data Preprocessing Module</h1>
    </div>
    """,
    unsafe_allow_html=True
    
)
    
    GDP_data = None 
    df_GDP_gr = None 
    
    # Initialize df_GDP_data in session_state if it's not already initialized
    if "df_GDP_data" not in st.session_state:
        st.session_state.df_GDP_data = None  # or initialize it with some default value

    # Now you can use it
    df_GDP_data = st.session_state.df_GDP_data
        


    
    st.markdown("---")
    st.subheader("Load GDP Data")

    # Load and Read the GDP data
    st.info("Please upload GDP data with the first column as the date (YYYY-MM) format and the second column as the GDP value.")
    GDP_data = st.file_uploader(f"Please upload GDP data data in CSV or Excel file formats", type={"csv", "xlsx", "xls"}, key="loader1")
    if GDP_data is not None:
                try:
                    df_GDP_data= pd.read_csv(GDP_data)
                except Exception as e:
                    df_GDP_data = pd.read_excel(GDP_data)
                    
                if st.button('Load the data', key="gdp_display"):
                    if df_GDP_data is not None:
                        st.success(f'You uploaded GDP data successfully! 🎉🎉🎉')
                        st.write(df_GDP_data)
                    else:
                        st.write("Please first upload .csv, .xlsx, or .xls files 😔")
    
                st.session_state.df_GDP_data = df_GDP_data
                
     

    st.markdown("---")
    st.subheader("Check Missing Data")
        
    if 'df_GDP_data' in locals() or 'df_GDP_data' in globals():
        if df_GDP_data is not None:
            # Check for missing data in the GDP column
            missing_data_count = df_GDP_data['GDP'].isnull().sum()

            # Identify dates with missing data
            missing_dates = df_GDP_data[df_GDP_data['GDP'].isnull()]['Date']
        else:
            st.write("No data available. Please upload a file.")
        
        if st.button('Check Missing Data', key="missing_data"):
            st.info(f"Missing data count in GDP column: {missing_data_count}")
            if missing_dates.empty:
                st.info("No dates have missing data.")
            else:
                st.table(missing_dates)           

    else:
        st.write("Please first upload .csv, .xlsx, or .xls files 😔")
        
        
    st.markdown("---")
    st.subheader("Impute Missing Data")
    
    df_GDP_data = st.session_state.df_GDP_data
    
    if df_GDP_data is None:
        st.write("No data available. Please upload a file.")
    else:
        missing_data_count = df_GDP_data['GDP'].isnull().sum()
        
        # If there is missing data
        if missing_data_count > 0:
            st.write(f"Missing data count in GDP column: {missing_data_count}")

            # Let the user select a filling method
            filling_method = st.selectbox(
                'Select a method to fill missing data:',
                ('None','Forward fill', 'Backward fill', 'Interpolate', 'Fill with mean', 'Fill with median', 'Fill with mode', 'Fill with a specific value'),
                index=0)

            # Apply the selected filling method
            if filling_method == 'None':    
                st.write("No filling method selected.")
            else:
                if filling_method == 'Forward fill':
                    df_GDP_data['GDP'].ffill(inplace=True)
                elif filling_method == 'Backward fill':
                    df_GDP_data['GDP'].bfill(inplace=True)
                elif filling_method == 'Interpolate':
                    df_GDP_data['GDP'].interpolate(method='linear', inplace=True)
                elif filling_method == 'Fill with mean':
                    df_GDP_data['GDP'].fillna(df_GDP_data['GDP'].mean(), inplace=True)
                elif filling_method == 'Fill with median':
                    df_GDP_data['GDP'].fillna(df_GDP_data['GDP'].median(), inplace=True)
                elif filling_method == 'Fill with mode':
                    df_GDP_data['GDP'].fillna(df_GDP_data['GDP'].mode().iloc[0], inplace=True)
                elif filling_method == 'Fill with a specific value':
                    specific_value = st.number_input('Enter the specific value:')
                    df_GDP_data['GDP'].fillna(specific_value, inplace=True)
                    
                st.info("Missing data filled successfully.")
                st.write(df_GDP_data)
                
                st.download_button('Download data as CSV', 
                                df_GDP_data.to_csv(index=False),  
                                file_name=f'GDP_imputed_{filling_method}.csv',
                                    mime='text/csv')
        else:
            st.write("No missing data in the GDP column.")
        
  

            
    st.markdown("---")
    st.subheader("Plot GDP Data")
    
    if st.button('Plot GDP Data', key="plot_gdp"):
        if 'df_GDP_data' in locals() or 'df_GDP_data' in globals():
            # Create a new figure
            fig = go.Figure()
            df_GDP_data.set_index('Date', inplace=True)

            # Add a scatter plot to the figure
            fig.add_trace(go.Scatter(x=df_GDP_data.index,
                                    y=df_GDP_data['GDP'],
                                    mode='markers+lines',
                                    name='GDP',
                                    marker=dict(color='blue'),
                                    line=dict(color='blue', width=2),
                                    showlegend=True,
                                    hoverlabel=dict(bgcolor='white', font_size=12, font_family='Rockwell'),
                                    hoverinfo='x+y',
                                    # hovertemplate='Quarter: %{x}<br>GDP: %{y:.2f} trillion USD<br>',
                                    textposition='top center',
                                    textfont=dict(family='Rockwell', size=12, color='blue'),
                                    text='GDP'))

            # Set the title, x-label, and y-label of the plot
            fig.update_layout(title="Quarterly GDP value over time [2004-01 - 2023-09]", 
                            xaxis_title='Date [Quarters]', 
                            yaxis_title='GDP', 
                            autosize=False, 
                            width=1500,
                            height=500,
                            margin=dict(l=50, r=50, b=100, t=100, pad=4),
                            hoverlabel=dict(bgcolor='white', font_size=12, font_family='Rockwell'),
                            hovermode='x unified')
            
            st.plotly_chart(fig, use_container_width=True)
      
    
    st.markdown("---")
    st.subheader("Calculate GDP Growth Rate")
    
    
    if st.button('Calculate GDP Growth Rate', key="gdp_growth_rate"):
        st.write("GDP growth rate formula:")
        st.latex(r'GDP_{growth rate} = \frac{GDP_{current} - GDP_{previous}}{|GDP_{previous}|} \times 100')

        df_GDP_data['GDP_GrowthRate'] = df_GDP_data['GDP'].pct_change()
        df_GDP_gr= df_GDP_data.copy()
        st.info("GDP growth rate calculated successfully.")
        st.write(df_GDP_gr)
        
        st.session_state.df_GDP_gr = df_GDP_gr
        
        st.download_button('Download data as CSV', 
                            df_GDP_gr.to_csv(index=False),  
                            file_name=f'GDP_growthrate.csv',
                            mime='text/csv')
    
    st.markdown("---")
    st.subheader("Plot  GDP Growth Rate")
    if st.button('Plot GDP Growth Rate', key="plot_gdp_rate"):
        df_GDP_gr = st.session_state.df_GDP_gr
        if 'df_GDP_gr' in locals() or 'df_GDP_gr' in globals():            
            fig = go.Figure()
            
            df_GDP_gr.set_index('Date', inplace=True)

            # Add a scatter plot to the figure
            fig.add_trace(go.Scatter(x=df_GDP_gr.index,
                                    y=df_GDP_gr['GDP_GrowthRate'],
                                    mode='markers+lines',
                                    name='GDP GrowthRat',
                                    marker=dict(color='blue'),
                                    line=dict(color='blue', width=2),
                                    showlegend=True,
                                    hoverlabel=dict(bgcolor='white', font_size=12, font_family='Rockwell'),
                                    hoverinfo='x+y',
                                    #hovertemplate='Quarter: %{x}<br>GDP: %{y:.2f} trillion USD<br>',
                                    textposition='top center',
                                    textfont=dict(family='Rockwell', size=12, color='blue'),
                                    text='GDP'))

            # Set the title, x-label, and y-label of the plot
            fig.update_layout(title="Quarterly GDP value over time [2004-01 - 2023-09]", 
                            xaxis_title='Date [Quarters]', 
                            yaxis_title='GDP Growth Rate [%]', 
                            autosize=False, 
                            width=1500,
                            height=500,
                            margin=dict(l=50, r=50, b=100, t=100, pad=4),
                            hoverlabel=dict(bgcolor='white', font_size=12, font_family='Rockwell'),
                            hovermode='x unified')

            st.plotly_chart(fig, use_container_width=True)
            
            
    st.markdown("---")
    st.subheader("Check for Stationarity")
    
    # write the null and alternate hypothesis

    
    
    stationarity_test = st.selectbox('Select the statistical test for stationarity:', ('None','Augmented Dickey-Fuller (ADF)', 'Kwiatkowski-Phillips-Schmidt-Shin test (KPSS)'), index=0)

    
    if stationarity_test == 'None':
        st.write("No statistical test selected.")
        # if ADF test is selected
    elif stationarity_test == 'Augmented Dickey-Fuller (ADF)':
        # st.info("Null Hypothesis (H0): suggests the time series is non-stationary")
        # st.info("Alternate Hypothesis (H1): suggests the time series is stationary")
        df_GDP_gr = st.session_state.df_GDP_gr
        if df_GDP_gr is None:
            st.write("No data available. Please upload a file.")
        else:
            timeseries = df_GDP_gr['GDP_GrowthRate']
            
            result = adfuller(timeseries.dropna(), autolag='AIC')

            st.info(f'ADF Statistic: {result[0]:.4f}')
            st.info(f'p-value: {result[1]:.6f}')

            is_stationary = result[1] < 0.05
            
            if is_stationary:
                st.info("The time series is stationary 😊")
            else:
                st.info("The time series is not stationary 😔")
                
    elif stationarity_test == 'Kwiatkowski-Phillips-Schmidt-Shin test (KPSS)':
        df_GDP_gr = st.session_state.df_GDP_gr
        if df_GDP_gr is None:
            st.write("No data available. Please upload a file.")
        else:
            timeseries = df_GDP_gr['GDP_GrowthRate']
            result = kpss(timeseries.dropna(), regression='c', nlags='auto')
            st.info(f'KPSS Statistic: {result[0]:.4f}')
            st.info(f'p-value: {result[1]:.6f}')

            is_stationary = result[1] > 0.05

            if is_stationary:
                
                st.info("The time series is stationary 😊")
            else:
                st.info("The time series is not stationary 😔")
            
    
    
    st.markdown("---")
    st.subheader("Convert the GDP data into stationary")


        
if __name__ == "__main__":
    GDP_Preprocessing_Module()