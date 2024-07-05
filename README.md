# Welcome to the ML based GDP Nowcasting Tool 

📊 Project Overview
-------------------
  
<p>The GDP Nowcasting app utilizes advanced machine learning algorithms and Google Trends search volume data to deliver accurate and timely GDP predictions. Having up-to-date information on the current state of the economy is essential for effective macroeconomic policymaking, especially during periods of rapid economic change or crises when traditional statistical data sources are unavailable or inaccessible.</p>

<p>The near real-time predictions on the current state of GDP empower policymakers, economists, and business leaders across Africa to make data-driven decisions and develop effective strategies for the continent's economic landscape.</p>

<p>This user-friendly tool empowers you to leverage the power of Machine Learning Operations (MLOps) to automate the entire GDP nowcasting pipeline, including workflows, deployments, and the implementation of various machine learning algorithms.</p>
  
Benefits of the tool:
  - **Automation**: Focuses on automating the entire pipeline, including the Machine Learning workflows and deployments.
  - **Scalability**: The tool facilitates scalable GDP Nowcasting via MLOps-powered frameworks, allowing it to handle growing data volumes and customization to different countries effortlessly.
  - **Reproducibility**: Ensures consistent and reliable results, enabling reproducible GDP Nowcasting implementations.
  - **User-Friendliness**: Maintains the user-friendly aspect of the tool.

Data Sources
---------------
  
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


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
