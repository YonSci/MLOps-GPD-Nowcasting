import streamlit as st

def Landing_Page():
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
        <h1>Welcome to the GDP Nowcasting App</h1>
    </div>
    """,
    unsafe_allow_html=True
    )
    
    st.markdown("---")
    

    with st.expander("📊 **Project Overview**"):
        st.markdown("""
                    
                    <div style="text-align: justify">
                    <p> The GDP Nowcasting app utilizes advanced machine learning algorithms and Google Trends search volume data to deliver accurate and timely GDP predictions. Having up-to-date information on the current state of the economy is essential for effective macroeconomic policymaking, especially during periods of rapid economic change or crises when traditional statistical data sources are unavailable or inaccessible. </p>

                    <p> The near real-time predictions on the current state of GDP, empowers policymakers, economists, and business leaders across Africa to make data-driven decisions and and develop effective strategies for the continent's economic landscape. </p>

                    <p> This user-friendly tool empowers you to leverage the power of Machine Learning Operations (MLOps) to automate the entire GDP nowcasting pipeline, including workflows, deployments, and the implementation of various machine learning algorithms. </p>
                  
                    Benefits of the tool:
                    
                    - **Automation**: Focuses on automating the entire pipeline, including the Machine Learning workflows and deployments.
                    
                    - **Scalability**: The tool facilitates scalable GDP Nowcasting via MLOps-powered frameworks, allowing it to handle growing data volumes and customization to different countries effortlessly.

                    - **Reproducibility**: Ensure consistent and reliable results, enabling reproducible GDP Nowcasting implementations.
                    
                    - **User-Friendliness**: Maintains the user-friendly aspect of the tool.
                    
                    </div>
                    
                    """, unsafe_allow_html=True
                    )
        
    with st.expander("**Data Sources**"):
        st.markdown("""
                    <div style="text-align: justify">

                    We combine <a href="https://trends.google.com/trends/"> Google Trend </a> search volume data with GDP data from various data source to train multiple machine learning prediction models.

                    Sources for GDP data:
                    - <a href="https://www.imf.org/en/Data"> International Monetary Fund (IMF) </a>
                    - <a href="https://data.worldbank.org/indicator/"> World Bank </a>
                    - <a href="https://www.oecd.org/sdd/na/"> Organization for Economic Co-operation and Development (OECD) </a> 
                    - National Statistical Offices:
                      - <a href="https://www.nigerianstat.gov.ng/"> Nigeria </a>
                      - <a href="https://www.ansd.sn/"> Senegal </a> 
                      - <a href="https://www.knbs.or.ke/"> Kenya </a>  
                      - <a href="https://www.capmas.gov.eg/"> Egypt </a> 
                    
                    </div>
                    """, unsafe_allow_html=True
                    )


    with st.expander("**Methodology**"):
        st.markdown("""
            
            <div style="text-align: justify">
            <p> The project is developed by the African Center for Statistics (ACS) at the United Nations Economic Commission for Africa (UNECA) and supported by the Regular Program of Technical Cooperation (RPTC). </p> 
            </div>
            
            """, unsafe_allow_html=True
            )


    with st.expander("**Project Modules**"):
        st.markdown("""
                    <div style="text-align: justify">
                    The project is divided into 5 modules: 

                    - **Data Downloader Module**: This module retrieves Google Trends data for a specified keyword and country, as well as GDP data.
                    - **Data Preprocessing Module**: This module preprocesses the Google Trends and GDP data (Data Cleaning, Outlier Detection and Removal, Time Series Transformation, Resampling, Decomposition, and Data Integration etc).  
                    - **Feature Engineering**: This module create new features based on existing data to improve model performance.   
                    - **Model Development**: This module trains different machine learning models on the preprocessed data.    
                    - **Model Evaluation**: This module uses various metrics to evaluate how well the trained models predict GDP compared to actual data. It helps identify the best-performing model for real-world use. 
                    - **Visualization & Interpretation**: This module creates visualizations to showcase the model's predictions and how different features influence the GDP estimates. It helps users understand the model's reasoning and gain valuable economic insights.  
                    </div>
                    """, unsafe_allow_html=True
                )
        


    with st.expander("**Resources**"):
        st.markdown("""
                
                <div style="text-align: justify">
                <p> Explore resources designed to help you make the most of our platform:</p>
                    
                - <a href=" https://github.com/YonSci/GPD-Nowcasting"> Github Project Link</a>    
                - <a href=" https://github.com/YonSci/GPD-Nowcasting"> Tutorials </a>    
                - <a href=" https://github.com/YonSci/GPD-Nowcasting"> Blog </a>   
                    
                </div>
                
                """, unsafe_allow_html=True
                )
        

    with st.expander("**Acknowledgments**"):
        st.markdown("""
                    
                    <div style="text-align: justify">
                    <p> The project is developed by the African Center for Statistics (ACS) at the United Nations Economic Commission for Africa (UNECA) and supported by the Regular Program of Technical Cooperation (RPTC). </p> 
                    </div>
                    
                    """, unsafe_allow_html=True
                    )
        


    with st.expander("**Contact US**"):
        st.markdown("""
                    
                    <div style="text-align: justify">  

                    - **Anjana Dube**, Senior Regional Advisor | African Centre for Statistics (ACS) | United Nations Economic Commission for Africa (UNECA) | anjana.dube@un.org
                    - **Issoufou Seidou**, Principal Statistician | African Centre for Statistics (ACS) | United Nations Economic Commission for Africa (UNECA) | seidoui@un.org
                    - **Yonas Mersha**, Data Science Consultant | African Centre for Statistics (ACS) | United Nations Economic Commission for Africa (UNECA) |  yonas.yigezu@un.org
                    </div>
                    
                    """, unsafe_allow_html=True
                    )
        



if __name__ == "__main__":
    Landing_Page()
