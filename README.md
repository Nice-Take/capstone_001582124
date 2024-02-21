## Anthony Mascari | ML Sample Project ##
This project was created as a capstone project over the course of two to three days.

- The model was created using XGBoost.
- Visualizations were created using matplot/seaborn.
- The API was written with FastAPI.
- The front end of the application was an experiement with HTMX.
*The raw data was acquired from Kaggle and originally curated by:
Hummamm Qaasim: https://www.kaggle.com/datasets/hummaamqaasim/jobs-in-data*

Visualizations, documentation and explainations of the 
'business problem' being addressed by this project are available
in the 'Docs' folder.

If you desire to run a copy on your machine, please find
the necessary files inside the 'Dist' folder.
UN: guest
PW: guest

# The app was built to run (front & back-end) on the client machine.

## Project Overview

The goal of this project was to assist in estimating salaries in various parts of the world for employees working in Machine Learning & Data Science. The solution involves a number of pieces which included data preparation, model training/saving, back-end logic for using the model to make predictions, a RESTful API, a dockerized version of the backend, and front-end htmx/javascript to run in the client's browser for user interaction. The graph visualizations are created by the backend (using seaborn & matplot) once the user has selected the required fields. The graphs are stored temporarily in memory instead of being written to disk to minimize response time and avoid unnecessary i/o. 

## The Front End

One of the unique aspects of this project was that it was experimenting using HTMX. This allows content updates without the use of a heavy front-end framework or losing scroll state.

![Solar-Powered Camera System](https://github.com/Nice-Take/capstone_001582124/blob/master/visualizations/fullApp_Italy_ML_Engineer.jpg)
*Caption: A Machine Learning Engineer Living in Russia working in Italy.*


