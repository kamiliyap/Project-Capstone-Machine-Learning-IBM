# Create an application to predict Students Adaptability Level in Online Education with Machine Learning

## Try the deployed App in : https://studentadaptabilitypredict.pythonanywhere.com/


![FinalDemo](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/DEMO.gif?raw=true)

As illustrated above, this application leverages machine learning models to predict the adaptability level of students in online education, providing valuable insights for understanding the impact of various factors. By analyzing the effects of age, gender, location, and other relevant variables, we aim to determine the level of adaptability of students in the online learning environment. Through the utilization of AI and machine learning, this application enables students to gain immediate predictions regarding their adaptability level, helping them make informed decisions and adjustments to optimize their online education experience.

## Description

By utilizing IBM AutoAI, you can streamline and automate the entire process of constructing predictive models to cater to diverse needs. This powerful tool expedites the generation of exceptional models, effectively minimizing the time and energy required while facilitating prompt decision-making. In this context, you can leverage AutoAI to create a model that accurately predicts the adaptability level of students in online education by considering various data points such as age, gender, region, institution type, network type, and more.

Upon completing this code pattern, you will gain proficiency in the following:

* Rapidly setting up services on IBM Cloud to build model development.
* Importing data and initiating the AutoAI process effortlessly.
* Constructing multiple models using AutoAI and assessing their performance.
* Selecting the optimal model and successfully deploying it.
* Generating predictions by making REST calls to the deployed model.
* Comparing the process of utilizing AutoAI with manual model building.
* Visualizing the deployed model through a user-friendly front-end application.

### Architecture Components

![Architecture Components](https://media.github.ibm.com/user/21063/files/3b77e580-913c-11ea-9dea-425b1d4f4ee0)

## Flow Description
1. The user creates an IBM Watson Studio Service on IBM Cloud.
2. The user creates an IBM Cloud Object Storage Service and adds that to Watson Studio.
3. The user uploads the student adaptability level in online education data file into Watson Studio.
4. The user creates an AutoAI Experiment to predict student adaptability level on Watson Studio
5. AutoAI uses Watson Machine Learning to create several models, and the user deploys the best performing model.
6. The user uses the Flask web-application to connect to the deployed model and predict the student adaptability level in online education.

## Included components
*	[IBM Watson Studio](https://cloud.ibm.com/catalog/services/watson-studio) - IBM Watson® Studio helps data scientists and analysts prepare data and build models at scale across any cloud.
*	[IBM Watson Machine Learning](https://cloud.ibm.com/catalog/services/machine-learning) - IBM Watson® Machine Learning helps data scientists and developers accelerate AI and machine-learning deployment. 
*	[IBM Cloud Object Storage](https://cloud.ibm.com/catalog/services/cloud-object-storage) - IBM Cloud™ Object Storage makes it possible to store practically limitless amounts of data, simply and cost effectively.

## Featured technologies
+ [artificial-intelligence](https://developer.ibm.com/technologies/artificial-intelligence/) - Build and train models, and create apps, with a trusted AI-infused platform.
+ [Python](https://www.python.org/) - Python is an interpreted, high-level, general-purpose programming language.


## Prerequisites

This Cloud pattern assumes you have an **IBM Cloud** account. Go to the 
create account in link below 
  - [IBM Cloud account](https://cloud.ibm.com)
  - [Python 3.11.0](https://www.python.org/downloads/release/python-3110/)

# Steps
0. [Download the data set ](#step-0-Download-the-data-set)
1. [Clone the repo](#step-1-clone-the-repo)
2. [Explore the data (recommended)](#step-2-explore-the-data-recommended)
3. [Create IBM Cloud services and the AutoAI](#step-3-create-ibm-cloud-services-and-the-AutoAI)
4. [Run AutoAI experiment](#step-4-run-autoai-experiment)
5. [Create a deployment and test your model](#step-5-create-a-deployment-and-test-your-model)
6. [Create a notebook from your model (optional)](#step-6-create-a-notebook-from-your-model-optional)
7. [Run the application](#step-7-run-the-application)

## Step 0. Download the data set 
We will use an student data set from Kaggle. You can find it [here](https://www.kaggle.com/datasets/mdmahmudulhasansuzan/students-adaptability-level-in-online-education).
 Click on the `Download` button, and you should see
that you will download a datasets file named `students_adaptability_level_online_education.csv`.
This is the data set we will use for the remainder of the example. Remember that this example is purely educational, and you
could use any data set you want - we just happened to choose this one.

## Step 1. Clone the repo
Clone this repo onto your computer in the destination of your choice:
```
git clone https://github.com/omidiyanto/student-adaptability-prediction.git
```
## Step 2. Explore the data (Recommended)

#### If you want to run the notebook that include the Exploratory Data Analysis below, go to [here](https://github.com/omidiyanto/student-adaptability-prediction/blob/main/Exploratory%20Data%20Analysis/notebooks.ipynb).

* Within Watson Studio, you explore the data before you create any 
machine learning models. You want to understand the data, and find any trends between 
what you are trying to predict student <b>adaptivity level</b> and the data's features.

* Once you import, you see the data into a data frame, and call the `df_.head()` function, you will see the first 5 rows of the data set also the 13 data features.
![dfHEAD](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/dfHEAD.png?raw=true)

* To check the data types, missing values, and statistics summary
![dfSUM](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/dfSUM.png?raw=true)

* How are the students adapting to the online learning system?
![percentADAPT](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/percentageADAPT.png?raw=true)

* What are the relationships between the independent variables measured and adaptivity level?
![relationships](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/relationships.png?raw=true)

* What is the top 5 factors that are the most important in predicting the adaptivity levels of the students?
![top5](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/top55.png?raw=true)

<b>If you want to see all of the Exploratory Data Analysis code, and run the notebook yourself, go to [here](https://github.com/omidiyanto/student-adaptability-prediction/blob/main/Exploratory%20Data%20Analysis/notebooks.ipynb)</b>

## Step 3. Create IBM Cloud services and the AutoAI

![Creating-Watson-Service](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/1.-create-IBM-Services.gif?raw=true)

1.	Login to your IBM Cloud account: https://cloud.ibm.com 

2.	Within your IBM Cloud account, click on the top search bar to search for cloud services and offerings. Search and create this services: <b>Watson Studio</b>, <b>Watson Machine Learning</b>, and <b>Cloud Object Storage</b>

3.	 Once all the services instance is ready, redirect to the Watson Studio page. Click on the “Launch in IBM Cloud Pak for Data” button to launch Watson Studio in a new tab.

![Creating-empty-project](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/2.-Open-Watson-studio_-create-new-project_-integrate-with-Wa.gif?raw=true)

4.  Create new project that says, “New Project”. Next, click on “Create an empty project”.

5.  On the new project page, give your project a name. You will also need to associate an IBM Cloud Object Storage instance to store the data set.

6. Go to Manage Tab, in the Service & Integrations option, associate the <b>Watson Machine Learning</b> service.

![Add-dataset and AutoAI](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/3.-Import-data-and-AutoAI.gif?raw=true)

7.  Upload the `students_adaptability_level_online_education.csv` dataset that you have downloaded it previously. Watson Studio takes a couple of seconds to load the data, and then you should see the import has completed. To make sure it has worked properly, you can click on “Assets” on the top of the page, and you should see your insurance file under “Data Assets”.

8.  Once you have added the data set, click on the “New Asset” button on the top right corner. This time select “AutoAI”.



## Step 4. Run AutoAI experiment

![Run-AutoAI-project](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/4.-Customize-experiment-settings-on-AutoAI.gif?raw=true)

1.  On the New AutoAI Experiment page, give a name to your AutoAI project.

2.  After you create your experiment, you are taken to a page to add a data source to your project. Click on “Select from project” and then add the `students_adaptability_level_online_education.csv` file. Click on Select asset to confirm your data source.

3.  Next, you see that AutoAI processes your data, and you see a What do you want to predict section. Select the <b>Adaptivity Level</b> as the Prediction column.

4.  Next, let's explore the AutoAI settings to see what you can customize when running your experiment. Click on Experiment settings.First, you see the data source tab, which lets you omit certain columns from your experiment. You choose to leave all columns. You can also select the training data split. It defaults to 85% training data. The data source tab also shows which metric you optimize for. For the regression, it is RMSE (Root Mean Squared Error), and for other types of experiments, such as Binary Classification, AutoAI defaults to Accuracy. Either way, you can change the metric from this tab depending on your use case.

5.  Click on the Prediction tab from within the Experiment settings. There you can select from Binary Classification, Regression, and Multiclass Classification.

6.  Lastly, you can see the Runtime tab from the Experiment settings this shows you other experiment details you may want to change depending on your use case.

7.  Once you are happy with your settings, ensure you are predicting for the <b>Adaptivity Level</b> column, and click on the run 'Run Experiment' button on the bottom-right corner of the screen.

![running](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/5.-Run-Experiment-AutoAI.gif?raw=true)

8.  Next, your AutoAI experiment runs on its own. You see a progress map on the right side of the screen which shows which stage of the experiment is running. This may be Hyper Parameter Optimization, feature engineering, or some other stage.

![complete](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/AutoAI%20Complete.png?raw=true)

![pipeline](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/AutoAI%20Pipeline.png?raw=true)

9.  You have different pipelines that are created, and you see the rankings of each model. Each model is ranked based on the metric that you selected. Once the experiment is done, you see Experiment completed under the Progress map on the right-hand side of the screen. As you can see, the best pipeline for this model is the Pipeline 16 with Snap Decision Tree Classifier algortihm with great accuracy of 0.884

![evaluateModel](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/6.-Evaluate-the-model.gif?raw=true)

10. On the left-hand side, you can see different “Model Evaluation Measures”, “Feature Transformations”, and “Feature Importance”.

## Step 5. Create a deployment and test your model

![deployment-space](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/7.-Create-a-deployment.gif?raw=true)

1.	Once you are ready to deploy one of the models, click on “Save As” at the top-right corner of the model you want to deploy. Save it as a “Model” and name your model as you want. Click on “Create” 
Note: We show you how to save it as a notebook in step 6.

2.	Once the model is successfully saved, click on the “View in project” in the green notification on the right side of the screen. Alternatively, you can also find your model saved in the “Assets” tab under “Models”.

3.	Next, you are taken to a screen that has the overview of the model you just saved. Click on “Promote to deployment space” on the top right corner of your screen.  Alternatively, if you’re doing it from the Assets tab, then under the “Models” section, click on the 3 dots on the right side of your screen and click “promote”.

4.	On the Promote to space page, you need a target space to promote your model. Click on “New space +” on the right side of your screen. 

5.	Next, on the Create a deployment space screen, give your space a name, make sure the right cloud object storage is selected, and select your machine learning service instance. For this experiment, selecting the machine learning service is mandatory as we need to build a prediction model. Then click on “Create”.

6.	Once the space is ready, click on “Close” in the pop-up and you will be redirected to the promote to space page. You see your newly created space under the “Target space”. Once you’re happy with your selections, click on “Promote”. 

7.	Once the model is successfully promoted, you will see a green notification box, click on “deployment space” in the notification. Alternatively, you can also find your deployment spaces when you click on the hamburger sign on the top left most side on your screen. 

8.	You will be redirected to the deployments page, where you will find your promoted model. Hover over the row, to see a rocket shaped icon, click on the icon to deploy you model. 

9.	In the dialog box, select “Online” as your deployment type, give your deployment a name and click “Create”.

10.	Click on the “Deployments” tab to see the status of your deployment. Once the deployment is completed, click on the name your deployment. 

11.	On this page you find the API references, endpoint and code snippets to help you integrate your model with your applications.

![testDEPLOY](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/8.-Try-validatetest-the-model-deployed.gif?raw=true)

12. To test your model, click on the “Test” tab. You can select a row from the data set and enter the data in the fields then click on the “Predict” button at the bottom. 

13. To validate the prediction, you check the data file that you used to train the model. As you can see, the model predicted a "Moderate". Until now, we know the model is working properly.

## Step 6. Create a notebook from your model (optional)

![create notebook](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/9.-Create-Notebooks.gif?raw=true)

With AutoAI's latest features, the code that is run to create these models is no more a black box. One or more of these models can be saved as a Jupyter notebook and the Python code can be run and enhanced from within. 

* Click on `Save As` at the top-right corner of the model, and click `Notebook`. 

* This opens a new tab (be sure to enable pop-up for this website) titled `New Notebook` where in you can edit the default name if you choose to and then click on `Create`. This might take a few minutes to load for the first time. 


## Step 7. Run the application

The driver code to run the application can be found under the web-app folder within the git repository that was cloned from [Step 1](#step-1-clone-the-repo). To run and test your deployed model through this Python-based user-interface,
you need to replace the API key & Endpoint URL information within `web-app/app.py` code.


### 7.1 Get IBM Cloud API key

![generateAPIKEY](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/10.-Get-IBM-Cloud-API-key.gif?raw=true)

* Generate an IBM Cloud apikey by going to `cloud.ibm.com` and then from the top-right part of the screen click on `Manage`-> `IAM`.

* Next, click on `API keys` from the left side-bar. Next click on `Create an IBM Cloud API key`.

* Name the key as you wish, and then click `Create`. Once the key is created, click on the `Download` button. in that file you can see your API_KEY

![apiKEY](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/API%20key_downloaded.png?raw=true)


### 7.2 Get Endpoint URL

![getURL](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/endpointURL.png?raw=true)

* Inside Watson Studio (Or Cloud Pak for Data)`Deployment Spaces`, there is the Endpoint URL, you can click the Copy button to easily copy the URL.

### 7.3 Modify the API key & Endpoint URL in app.py

* After you get your own API key & Endpoint URL for your deployement model, change the app.py code with your own just like the below picture shown:

![modAPPPY](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/codeChange.png?raw=true)


### 7.4 Install dependencies, and run the app

Note, this app is tested on this version of Python 3.11.0

Within the `web-app` directory, run the following command: 

```
pip install flask flask-wtf urllib3 requests
```
run the app.py code!

<b>Great job! You are ready application is ready!</b>

### 7.5 Run application from browser

* Go to `127.0.0.1:5000` in your browser to view the application. Go ahead and fill in the form, and click on the `Predict`
button to see your predicted Adaptability Level based on your data.

![FinalDemo](https://github.com/omidiyanto/program_omi/blob/main/asset-gif/DEMO.gif?raw=true)

