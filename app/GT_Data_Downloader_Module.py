import streamlit as st
import pandas as pd
from datetime import datetime
import time
#pd.set_option('future.no_silent_downcasting', True)
from pytrends.request import TrendReq

requests_args = {
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
}

pytrends = TrendReq(hl='en-US', tz=360, timeout=(40,25), requests_args=requests_args)


#  blue, green, orange, red, violet, gray/grey, rainbow.


def GT_Data_Downloader_Module():
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
        <h1>Google Trends Data Downloader</h1>
        </div>
        """,
        unsafe_allow_html=True
        )
    
    # tz = 360
    # cat = 0
    # geo = country_code
    # gprop = ''
    # kw_list = [keywords]
    
    st.markdown("---")  
    
    keywords = []  # Initialize keywords as an empty list

    
    def get_african_countries():
        return [
            "None", "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cape Verde", "Cameroon",
            "Central African Republic", "Chad", "Comoros", "Democratic Republic of the Congo", "Djibouti",
            "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea",
            "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali",
            "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo",
            "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa",
            "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"
        ]

    def get_name_code_dict():
        return {
            'None': 'None', 'Algeria': 'DZ', 'Angola': 'AO', 'Benin': 'BJ', 'Botswana': 'BW', 'Burkina Faso': 'BF',
            'Burundi': 'BI', 'Cape Verde': 'CV', 'Cameroon': 'CM', 'Central African Republic': 'CF', 'Chad': 'TD',
            'Comoros': 'KM', 'Democratic Republic of the Congo': 'CD', 'Djibouti': 'DJ', 'Egypt': 'EG',
            'Equatorial Guinea': 'GQ', 'Eritrea': 'ER', 'Eswatini': 'SZ', 'Ethiopia': 'ET', 'Gabon': 'GA',  'Gambia': 'GM',
            'Ghana': 'GH', 'Guinea': 'GN', 'Guinea-Bissau': 'GW', 'Ivory Coast': 'CI', 'Kenya': 'KE', 'Lesotho': 'LS',
            'Liberia': 'LR', 'Libya': 'LY', 'Madagascar': 'MG', 'Malawi': 'MW', 'Mali': 'ML', 'Mauritania': 'MR',
            'Mauritius': 'MU', 'Morocco': 'MA', 'Mozambique': 'MZ', 'Namibia': 'NA', 'Niger': 'NE', 'Nigeria': 'NG',
            'Republic of the Congo': 'CG', 'Rwanda': 'RW', 'Sao Tome and Principe': 'ST', 'Senegal': 'SN',
            'Seychelles': 'SC', 'Sierra Leone': 'SL', 'Somalia': 'SO', 'South Africa': 'ZA', 'South Sudan': 'SS',
            'Sudan': 'SD', 'Tanzania': 'TZ', 'Togo': 'TG', 'Tunisia': 'TN', 'Uganda': 'UG', 'Zambia': 'ZM', 'Zimbabwe': 'ZW'
        }

    def get_keyword_dict():
        return {
            "Capstone": ['Canada Revenue Agency', 'Niagara Falls', 'Plant', 'Unemployment', 'Paint', 'Book',
                        'The Globe and Mail', 'Mortgage loan', 'License', 'Theater', 'Election', 'Furniture', 'Gasoline',
                        'Lawyer', 'Boat', 'Shopping mall', 'Forest', 'Tax', 'Fertilizer', 'Anxiety', 'Advertising',
                        'Cigars & Cigarillos', 'Kijiji', 'FIFA', 'Hospital', 'Textile', 'Walmart', 'Carpet', 'Facebook',
                        'General contractor', 'Ferry', 'GitHub', 'Payment', 'Trailer', 'Java', 'Coronavirus disease 2019',
                        'Bank', 'Microsoft Windows', 'Scholarship', 'Bidding', 'Newspaper', 'Business',
                        'Global Positioning System', 'Toronto Transit Commission', 'ttc', 'Liquor Control Board of Ontario',
                        'Domain name', 'Credit', 'SQL', 'Toronto', 'Adhesive', 'Recipe', 'Insurance', 'Expedia', 'Shaving',
                        'Air conditioning', 'Clinic', 'Food', 'Ship', 'IKEA', 'Flooring', 'Jean Coutu Group', 'Trade fair',
                        'Real Estate', 'Theatre', 'Train', 'Valve', 'Employment', 'Dashboard', 'Walmart Canada',
                        'Cigarette', 'Manufacturing', 'Door', 'Cineplex Entertainment', 'Dress', 'National Hockey League',
                        'Dog', 'University', 'Home insurance', 'Lease', 'Menu', 'Cottage', 'Laptop', 'House', 'Salesforce',
                        'Desjardins Group', 'AVG Technologies', 'HollywoodPQ', 'News', 'Garmin Ltd.', 'FMyLife', 'Bankruptcy',
                        'Dance', 'Hotel', 'Backpack', 'Calculator', 'Netflix', 'Printing', 'Building insulation', 'Student',
                        'Logistics', 'Car', 'Bookstore', 'Antivirus software', 'Wedding', 'Health', 'RE/MAX', 'Side effect',
                        'Baggage', 'Staples', 'Gift', 'Park', 'Law', 'Massage', 'Walk-in clinic', 'Color',
                        'Canada Customs and Revenue Agency', 'Fish', 'Yoga', 'Real Canadian Superstore', 'Dye',
                        'Enterprise resource planning', 'Refrigerator', 'Wine', 'Electric generator', 'Royal Bank of Canada',
                        'Vacation', 'CEGEP', 'Exercise', 'Rail transport', 'Tree', 'Pesticide', 'Price', 'Jewellery',
                        'The Home Depot', 'Restaurant', 'Canada Post', 'Salmon', 'Grocery store', 'Git', 'Server',
                        'Apartment', 'Quebec City', 'Salary', 'GoDaddy', 'Clinique', "McDonald's", 'Waste', 'Swimming',
                        'Letter', 'BBC News', 'MySQL', 'Model', 'Passport', 'Résumé', 'Hydro-Québec', 'Job', 'Rent',
                        'Fashion', 'Marketing', 'Hair', 'Canning', 'Honda', 'SNC-Lavalin', 'AutoCAD', 'Carpool', 'Flower',
                        'Bridge', 'NBA', 'Film', 'Distribution', 'Customer relationship management', 'Circulaire',
                        'Staples Canada', 'Shoes', 'Email', 'School', 'Quebec', 'Sales', 'Truck', 'Airline',
                        'United Parcel Service', 'Flyer', 'PayPal', 'Plastic', 'Economy', 'Fire', 'Disease', 'Swimming pool',
                        'Account', 'Download', 'Academy Awards', 'Tractor', 'Hewlett-Packard', 'Customs', 'Driving',
                        'Stock', 'Cimpress', 'Spa', 'Software Developer', 'Veterinarian', 'Outsourcing', 'Boot',
                        'Air France', 'Architecture', 'Cruise ship', 'Google', 'Volkswagen Group', 'Canada', 'Xbox',
                        'John Deere', 'Architect', 'Flight'],
            "OESD": ['Economic crisis', 'Crisis', 'Recession', 'Financial crisis', 'Krach', 'Unemployment',
                    'Unemployment benefits', 'Welfare & Unemployment', 'Food & Drink', 'GPS & Navigation ',
                    'Performing Arts             ', 'Luggage topic', 'Vehicle', 'Brands', 'Birthday', 'Travel',
                    'Energy & Utilities', 'Vehicle Shopping', 'Tobacco Products', 'Health', 'Pharmacy',
                    'Carpooling & Ridesharing', 'Sports', 'Animal Products & Services', 'Fitness', 'Weddings', 'Car',
                    'Rental & Taxi Services', 'Autos & Vehicles', 'Tourist Destinations', 'Home & Garden',
                    'Events & Listings', 'Grocery & Food Retailers', 'Vehicle Licensing & Registration',
                    'Timeshares & Vacation Properties', 'Home', 'Appliances', 'Mass Merchants & Department Stores',
                    'Car Electronics', 'Fashion & Style', 'Trucks & SUVs', 'Home Furnishings', 'Footwear',
                    'Cruises & Charters', 'Hotels & Accommodations', 'Luggage & Travel', 'Accessories', 'Fast Food',
                    'Book Retailers', 'Veterinarians', 'Spas & Beauty Services', 'Acting & Theater',
                    'Travel Agencies & Services', 'Waiter', 'Job Listings', 'Resumes & Portfolios', 'Jobs topic',
                    'Temporary jobs', 'Private employment', 'agency', 'Recruitement', 'Developer Jobs', 'Job search',
                    'Bankruptcy topic', 'Judicial Liquidation', 'Bankruptcy', 'Affordable housing', 'House price index',
                    'Apartments & Residential Rentals', 'Insurance', 'Home Improvement', 'Economy News', 'Business News',
                    'World News', 'Politics', 'Newspapers', 'Flooring', 'Construction Consulting & Contracting',
                    'Swimming Pools & Spas', 'Civil', 'Engineering', 'Construction & Maintenance', 'Investment',
                    'Investing', 'Financial Planning', 'Data Management', 'Enterprise Technology', 'Accounting & Auditing',
                    'CAD & CAM', 'Development Tools', 'Customer Relationship Management (CRM)', 'Printing & Publishing         ',
                    'Events', 'Corporate', 'Computer Security', 'Outsourcing', 'Distribution & Logistics', 'Computer Servers',
                    'Consulting', 'Web Hosting & Domain Registration', 'Enterprise Resource Planning (ERP)', 'Business Operations',
                    'Commercial Vehicles', 'Agriculture & Forestry', 'Agrochemicals', 'Aviation', 'Business & Industrial',
                    'Chemicals Industry', 'Textiles & Nonwovens', 'Coatings & Adhesives', 'Food Production', 'Dyes & Pigments',
                    'Freight & Trucking', 'Transportation & Logistics', 'Mail & Package Delivery', 'Manufacturing',
                    'Private employment agency', 'House moving', 'Recruitment', 'Lawyer', 'Jobs', 'Public debt', 'Office',
                    'space', 'Housing bubble', 'Mortgage', 'Loan', 'Interest', 'Student loan', 'Bank', 'Commercial Building',
                    'Luggage', 'Exportation', 'Foreclosure'],
            "IBA": ['Economic crisis', 'Crisis', 'Recession', 'Financial crisis', 'Inflation', 'Unemployment', 'BISP',
                    'ehsaas program', 'USAID', 'Credit', 'Loan', 'Interest', 'House Loan', 'Car Loan', 'Food', 'Cinema',
                    'Cars', 'Birthday', 'Travel', 'Weddings', 'Fitness', 'Cigarette', 'Tourism', 'Hotels', 'Fast Food',
                    'House for sale', 'Construction', 'Investment', 'Jobs', 'Agriculture', 'FMCG', 'Aviation',
                    'Manufacturing', 'Textile', 'Economy News', 'Business News', 'World News', 'Politics', 'Newspapers',
                    'mehngai', 'Real estate', 'deficit', 'elections', 'parliament', 'taxes', 'government', 'budget',
                    'economic growth', 'subsidy', 'current account', 'trade', 'protest', 'stock market', 'revenue', 'LSM',
                    'M0', 'PSB', 'CPI']
        }

    african_countries = get_african_countries()
    name_code_dict = get_name_code_dict()
    keyword_dict = get_keyword_dict()
        
    
    st.subheader("Select Country")

    st.write("Please select a country from the dropdown list below")
    country = st.selectbox("Select a country:", african_countries, index=0, key="country") 

    if country != "None":
        country_code = name_code_dict[country]
        st.info("You selected: " + country + " and the 2 letter code for " + country + " is: " + country_code)
    else:
        st.info("Please select a country from the dropdown list")

    
    st.markdown("---")
    st.subheader("Select the time range")
    
    # st.write("Please select the date range for the data you would like to download")
    col1, col2 = st.columns(2)  
  
    start_date = datetime(2004, 1, 1)
    end_date = datetime.now()

    col1, col2 = st.columns(2)  
    with col1:
        start_date = st.date_input("Start date:", min_value=start_date, max_value=end_date)
    with col2:
        end_date = st.date_input("End date:", min_value=start_date, max_value=end_date)


    st.info("You selected: " + str(start_date) + " to " + str(end_date))
    
    # timeframe1 = f'{start_date}'
    # st.write(timeframe1)
    
    # timeframe2 = f'{end_date}'
    # st.write(timeframe2)
    
    # timeframe3 =f'{start_date} {end_date}'
    # st.write(timeframe3)

    
    
    
    st.markdown("---")
    st.subheader("Select Keywords")

    selection_option = st.radio("Select option:", ["Manually Enter Keywords", "Select From Dictionary"])


    if selection_option == "Manually Enter Keywords":
        # custom_keywords = st.text_input("Enter custom keywords (comma-separated):")
        # keywords = [keyword.strip() for keyword in custom_keywords.split(",")]
        # st.info("You entered a total of " + str(len(keywords)) + " keywords")
        custom_keywords = st.text_input("Enter custom keywords (comma-separated):")
    
        if custom_keywords:  # Check if the user entered any keywords
            keywords = [keyword.strip() for keyword in custom_keywords.split(",") if keyword.strip()]
            st.info("You entered a total of " + str(len(keywords)) + " keywords")
        else:
            st.info("You didn't enter any keywords.")
    else:
        
        keyword_category = st.selectbox("Select a keyword category:", ["None"] + list(keyword_dict.keys()), key="keyword_category1")
        if keyword_category == "None":
            st.info("Please select a keyword category from the dropdown list")
        else:
        
            selection_option = st.radio("Select option:", ["Select All", "Select Specific"])
            
            if selection_option == "Select All":
                keywords = keyword_dict[keyword_category]
                st.info("You selected all "  + str(len(keywords)) + " keywords from the " + keyword_category + " category ")
                # st.info("You selected all keywords from the category: " + keyword_category)
                # st.info("You selected a total of " + str(len(keywords)) + " keywords")
        
                df = pd.DataFrame(keywords, columns=["Keywords"])
        
                df.index = df.index + 1
                df.index.name = "S.No"
                
                st.dataframe(df)
                
            else:
                keyword_category = st.selectbox("Select a keyword category:", list(keyword_dict.keys()), key="keyword_category2")
                keywords = st.multiselect("Select Keywords:", keyword_dict[keyword_category])
                if keywords:  
                    st.info("You selected: " + str(keywords))
                    st.info("You selected a total of " + str(len(keywords)) + " keywords")
                    
        
        

    st.markdown("---")
    st.subheader("Download Data")

    if st.button("Download Data"):
        if keywords:  # Check if keywords is not empty
            keywords = list(set(keywords))
            # Define the chunk size
            chunk_size = 15

            # Split the list into chunks
            chunks = [keywords[i:i + chunk_size] for i in range(0, len(keywords), chunk_size)]
            
            # Initialize the status text
            # status_text = st.empty()
            
              # Display loading spinner
            # spinner_chars = "|/-\\"
            # for i in range(100):  # Adjust the range for the desired duration of the spinner
            #     status_text.text(f"Loading... {spinner_chars[i % len(spinner_chars)]}")
            #     time.sleep(0.1)
                
            
            for i, chunk in enumerate(chunks, 1):
                globals()[f'chunks{i}'] = chunk
                
                
            # status_text.text(f'Processing chunk {i} out of {len(chunks)}')
                
                
            def fetch_trends_in_batches(chunks,
                        batch_size,
                        cat, 
                        timeframe, 
                        geo, 
                        gprop=''):
                
                all_data = []
                
                batch_size=1
                
                
                num_batches = -(-len(chunks) // batch_size)  # Calculate number of batches
                
                for i in range(num_batches):
                    start_idx = i * batch_size
                    end_idx = (i + 1) * batch_size
                
                    batch_keywords = chunks[start_idx:end_idx]
            
                    pytrends.build_payload(batch_keywords, cat=cat, 
                                        timeframe=timeframe,
                                        geo=geo, 
                                        gprop=gprop)
                    data = pytrends.interest_over_time()
                    
                    all_data.append(data)

                combined_data = pd.concat(all_data, axis=1)
                return combined_data
            
            combined_data_dict = {}

            batch_size = 1
            for i in range(1, len(chunks) + 1):
                chunks = globals()[f'chunks{i}']
                combined_data_dict[f'combined_data{i}'] = fetch_trends_in_batches(chunks, 
                                                                                batch_size=batch_size,
                                                                                cat=0, 
                                                                                timeframe=f'{start_date} {end_date}', 
                                                                                geo=country_code, 
                                                                                gprop='')
            # Update the status text after each batch
            # status_text.text(f'Processing batch {i} out of {len(chunks)}')

            # Update the status text when the task is done
            # status_text.text('Data downloaded successfully')
                
          
                
                
                st.info(f"Batch {i} completed")
                #st.write(len(combined_data_dict))
                # Update the progress bar
                #progress_bar.progress(i / len(combined_data_dict))
                            
            # Determine the number of dataframes stored in combined_data_dict
            num_dataframes = len(combined_data_dict)

            # Initialize an empty list to store dataframes
            dataframes = []

            # Loop through the keys to access each dataframe
            for i in range(1, num_dataframes + 1):
                key = f'combined_data{i}'
                if key in combined_data_dict:
                    dataframes.append(combined_data_dict[key])

            # Concatenate the dataframes along the date index
            combined_df = pd.concat(dataframes, axis=1)

            combined_df = combined_df.loc[:, ~combined_df.columns.str.endswith('isPartial')]

            # Reset index to make date index
            combined_df.reset_index(inplace=True)

            # Drop duplicate date columns
            combined_df = combined_df.loc[:, ~combined_df.columns.duplicated()]

            # Set date column as index
            combined_df.set_index('date', inplace=True)

            st.write(combined_df)
            st.info(f'The final dataframe has {combined_df.shape[0]} rows and {combined_df.shape[1]} columns.   ')
            
            if (combined_df.shape[1] / len(keywords)) * 100 >= 80:
                st.info("Data downloaded successfully")
            else:
                st.warning("Please try again some keywords were not downloaded successfully.")
                
            st.download_button('Download data as CSV', 
                                combined_df.to_csv(index=False),  
                                file_name=f'gt_{start_date}_{end_date}_{country_code}.csv',
                                mime='text/csv')
                            
                
        
            
            
            
        else:
            st.info("Please enter or select some keywords before downloading data.")
            
    
    
  
    
                        
           
    
 


        
 
        
if __name__ == "__main__":
    GT_Data_Downloader_Module()
