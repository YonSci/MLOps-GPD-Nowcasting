Machine-Learning-project-structure, Environment 
===============================================


- Having a well-organized general Machine Learning project structure makes it easy to understand and make changes. 

- Moreover, this structure can be the same for multiple projects, which avoids confusion. 

- we will use the Cookiecutter package to create a Machine Learning project structure.


Machine Learning project structure: Steps
-----

1) Install cookiecutter


`pip install cookiecutter`

2) Create a repository on github.com (e.g., MLOps-GPD-Nowcasting)


    Note: Don’t check any options under ‘Initialize this repository with:’ while creating a repository.

3) Crate a project structure

    Go to a folder where you want to set up the project in your local system and run the following:

    `cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science`


    - project_name [project_name]: MLOps-GPD-Nowcasting
    
    - repo_name [my-test]: MLOps-GPD-Nowcasting
    
    - author_name [Your name (or your organization/company/team)]: yonas
    
    - description [A short description of the project.]: Description

    - Select open_source_license:
    1 - MIT
    2 - BSD-3-Clause
    3 - No license file
    Choose from 1, 2, 3 [1]: 1

    - skip this

        s3_bucket [[OPTIONAL] your-bucket-for-syncing-data (do not include 's3://')]:
        aws_profile [default]:


    - Select python_interpreter:
        1 - python3
        2 - python

    - Choose from 1, 2 [1]: 1


    - cd MLOps-GPD-Nowcasting

    - Initialize the git  
    `git init`

    - Add all the files and folder
    `git add .`

    - Commit the files  
    `git commit -m "Initialized the repo with cookiecutter data science structure"`


    - Set the remote repo URL
    `git remote add origin https://github.com/YonSci/MLOps-GPD-Nowcasting.git
    git remote -v`

    - Push to changes from local repo to github
    `git push origin master`


Machine Learning Python Environment
------------------------------------

`python -m venv ml_env`  

`ml_env\Scripts\activate`

`python.exe -m pip install --upgrade pip`

`pip install streamlit pandas datetime pytrends plotly statsmodels`


Git Comands
-----------------------------

To intialize the GIT    
`git init`  

To check the Status  
`git status`  
`git status -s`  

To check the commit history  

`git log`  

To add the file to the staging area  
`git add -A`  
`git add .`

To commit the changes  
`git commit -m "First commit"`  

Push the changes from the local to Github   
`git push origin master`



When a local branch is behind the remote branch:

`git fetch origin`  
`git merge origin/master`  
`git push origin master`




Resources: 
Github link: https://github.com/YonSci/MLOps-GPD-Nowcasting/data




To copy the project folder locally 

`git clone https://github.com/YonSci/MLOps-GPD-Nowcasting.git`


`git push origin master`





