[![CICD](https://github.com/nogibjj/Nruta_Mini_Project_11/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Nruta_Mini_Project_11/actions/workflows/cicd.yml)

# IDS 706 Mini Project 11 - Data Pipeline with Databricks

### 🏗️ Requirements
- Create a data pipeline using Databricks
- Include at least one data source and one data sink


### 🛠️ Setup Instructions
#### Cloning the repository onto Databricks
1. Log into Databricks and click on the Workplaces section.
2. Navigate to the Workplaces tab, then select "Users".
3. Locate your email ID and click on it.
4. Click the Create button in the top-right corner and select "Git Folder".
5. Paste the GitHub repository link in the provided field.
<img width="1466" alt="Image 1" src="https://github.com/user-attachments/assets/041a266f-e5bb-4a8c-9aee-78c89b730039">


#### Setting up the Compute Cluster
1. Go to the Compute section in Databricks.
2. Click on Create and select "Personal Compute".
3. Configure your cluster as shown in the image below:
<img width="1464" alt="Image 2" src="https://github.com/user-attachments/assets/2e78fab5-1316-4fa6-ba73-b11725aa3b8c">


#### Install the required Libraries in your Compute Cluster
1. Navigate to your personal compute cluster and click on the Libraries tab.
2. Add the following libraries through PyPI to ensure smooth project execution:
	•	pandas
	•	pytest
	•	python-dotenv
3. Follow the Databricks prompts to complete the library installation process.
<img width="1464" alt="Image 3" src="https://github.com/user-attachments/assets/43cd662f-1a91-4f21-b0c1-3d57ec443ab4">

Installing libraries through PyPI:
<img width="1464" alt="Image 4" src="https://github.com/user-attachments/assets/eba53a08-7ad5-4c9c-b718-18b4a13b3b1c">


#### Linking your Databricks workflow to your GitHub account
It is crucial to link your Databricks account to your GitHub account to ensure that the repository can be pushed to GitHub easily.
1. Navigate to Account Settings (Click on profile icon in the top right corner)
2. Head to `Linked Accounts`
3. Integrate your GitHub account with Databricks using the `Personal Access Token`
<img width="1464" alt="Image 5" src="https://github.com/user-attachments/assets/9ce095a9-f0f1-4815-a763-2afaca20f8a7">


### 🚀 ETL Pipeline
#### Setting up the ETL Pipeline
1. Navigate to `Workflows`
2. Click on `Create Job`

There will be three separate jobs - one for each stage of the ETL process.

###### Task 1 - Extract
1. Start a new task named **"Extract"**
2. Set the type to `"Python Script"`
3. Set the Source to `"Workspaces"`
4. Set the path to the `extract.py` file within your repository
5. Set the compute to your personal compute
6. Click on `"Create Task"`
<img width="834" alt="Image 6" src="https://github.com/user-attachments/assets/3a75efc4-8796-47bd-8989-f4ba7723900e">


##### Task 2 - Transform_Load
1, Click on `"Add Task"` and name this new task as **"Transform_Load"**
2. Set the same configurations as Extract
3. In the `Depends On` section, add **Extract**

##### Task 3 - Query
1. Click on `"Add Task"` and name this new task as `"Query"`
2. Set the same configuration as **Extract** and **Transform_Load**
3. In the `Depends On` section, add Transform_Load

This setup ensures that the pipeline runs sequentially, maintaining the proper order of the ETL process.

The final pipeline should look like this:
<img width="1065" alt="Image 7" src="https://github.com/user-attachments/assets/18441794-c802-40f3-9de5-fdbddbb2db47">

#### Running the pipeline:
<img width="1468" alt="Image 8" src="https://github.com/user-attachments/assets/ea4cb563-46e7-47b1-863c-1250fa44840d">
