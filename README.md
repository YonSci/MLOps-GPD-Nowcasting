Welcome to the ML based GDP Nowcasting Tool 
=============================================


📊 Project Overview
-------------------
  
The GDP Nowcasting app utilizes advanced machine learning algorithms and Google Trends search volume data to deliver accurate and timely GDP predictions. Having up-to-date information on the current state of the economy is essential for effective macroeconomic policymaking, especially during periods of rapid economic change or crises when traditional statistical data sources are unavailable or inaccessible.

The near real-time predictions on the current state of GDP empower policymakers, economists, and business leaders across Africa to make data-driven decisions and develop effective strategies for the continent's economic landscape.

This user-friendly tool empowers you to leverage the power of Machine Learning Operations (MLOps) to automate the entire GDP nowcasting pipeline, including workflows, deployments, and the implementation of various machine learning algorithms.

The app is deployed on streamlit cloud sever [GDP ML app](https://mlops-gpd-nowcasting-88t9uagbxrtgq2ajmbpcw4.streamlit.app/) 

Benefits of the tool:
  - **Automation**: Focuses on automating the entire pipeline, including the Machine Learning workflows and deployments.
  - **Scalability**: The tool facilitates scalable GDP Nowcasting via MLOps-powered frameworks, allowing it to handle growing data volumes and customization to different countries effortlessly.
  - **Reproducibility**: Ensures consistent andV reliable results, enabling reproducible GDP Nowcasting implementations.
  - **User-Friendliness**: Maintains the user-friendly aspect of the tool.

--------

Data Sources
-------------
  
We combine [Google Trend](https://trends.google.com/trends/) search volume data with GDP data from various sources to train multiple machine learning prediction models.

  **Sources for GDP data:**
  
  - [International Monetary Fund (IMF)](https://www.imf.org/en/Data)
  - [World Bank](https://data.worldbank.org/indicator/)
  - [Organization for Economic Co-operation and Development (OECD)](https://www.oecd.org/sdd/na/)
  - National Statistical Offices:
    - [Nigeria](https://www.nigerianstat.gov.ng/)
    - [Senegal](https://www.ansd.sn/)
    - [Kenya](https://www.knbs.or.ke/)
    - [Egypt](https://www.capmas.gov.eg/)


--------

Methodology
-------------

This mind map provides a structured overview of the complex ML process involved in GDP nowcasting. Overall, this mind map outlines the key steps involved in developing a machine learning model for GDP Nowcasting. It emphasizes data preparation, model selection, training, and ongoing monitoring for accurate and timely GDP predictions. Each stage plays a crucial role in building accurate models for economic forecasting. 

![Alt text](/reports/figures/mind_map_bg.jpg)

The flowchart captures the essential steps involved in building and deploying a machine learning model for GDP Nowcasting. The Machine Learning (ML) workflow involves several key steps. 

First, data is collected and pre-processed. Next, datasets are built for training and evaluation. Model selection and algorithm training follow, with hyperparameter tuning to optimize performance. The model is then evaluated, and if satisfactory, deployed for real-world use. Monitoring and maintenance ensure ongoing effectiveness. If the model doesn’t meet expectations, retraining occurs. This iterative process continues until the model performs well.

![Alt text](/reports/figures/ML_workflow_bg.jpg)

--------

Project Modules
---------------

The project is divided into 5 modules:
  
  - **Data Downloader Module**: This module retrieves Google Trends data for a specified keyword and country, as well as GDP data.
  - **Data Preprocessing Module**: This module preprocesses the Google Trends and GDP data (Data Cleaning, Outlier Detection and Removal, Time Series Transformation, Resampling, Decomposition, and Data Integration etc). In addtion, this module creates new features based on existing data to improve model performance.
  - **Model Development**: This module trains different machine learning models on the preprocessed data.
  - **Model Evaluation**: This module uses various metrics to evaluate how well the trained models predict GDP compared to actual data. It helps identify the best-performing model for real-world use.
  - **Visualization & Interpretation**: This module creates visualizations to showcase the model's predictions and how different features influence the GDP estimates. It helps users understand the model's reasoning and gain valuable economic insights.

--------

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


Resources
-------------

Explore resources designed to help you make the most of our platform:
  - [Github Project Link](https://github.com/YonSci/MLOps-GPD-Nowcasting/tree/master)
  - [Tutorials](https://github.com/YonSci/MLOps-GPD-Nowcasting/tree/master/notebooks)
  - [Data](https://github.com/YonSci/MLOps-GPD-Nowcasting/tree/master/data)
  - [Model](https://github.com/YonSci/MLOps-GPD-Nowcasting/tree/master/models)
  - [Documentation](https://github.com/YonSci/MLOps-GPD-Nowcasting/tree/master/reports)
  - [Blog](https://github.com/YonSci/GPD-Nowcasting)

--------


Acknowledgments
------------------

The project is developed by the African Center for Statistics (ACS) at the United Nations Economic Commission for Africa (UNECA) and supported by the Regular Program of Technical Cooperation (RPTC).

--------

Contact Us
------------
  
  - **Anjana Dube**, Senior Regional Advisor | African Centre for Statistics (ACS) | United Nations Economic Commission for Africa (UNECA) | anjana.dube@un.org | anjanad09@gmail.com
  - **Issoufou Seidou**, Principal Statistician | African Centre for Statistics (ACS) | United Nations Economic Commission for Africa (UNECA) | seidoui@un.org
  - **Yonas Mersha**, Data Science Consultant | African Centre for Statistics (ACS) | United Nations Economic Commission for Africa (UNECA) | yonas.yigezu@un.org

--------
