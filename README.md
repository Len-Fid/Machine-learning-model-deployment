## Building a machine learning model that predicts house prices and deploying it on Heroku
<p align="center"><img src="https://images.squarespace-cdn.com/content/v1/5d242dd8a10ed400017e7a33/1581356023178-GAJBMC2VUGG05XNAU8IJ/houseprices.jpg?format=1500w" width="500" height="300"></p>

## Project description: 
As part of the AI training at <a href="https://github.com/becodeorg"><strong>BeCode</strong></a> a task was received to create an API that will make price forecasts on houses or apartments according to certain parameters (number of rooms, living area, garden/no garden and etc.)

**Steps of the project:**
- Pre-process the data that was scrapped in the last project 
- Build a a machine learning model
- Create a Flask API that can handle a machine learning model
- Deploy an API to Heroku
- Present it to the client

**Time allocated for the project:**
* **28/04/22 - 06/05/22**

## Modelling:
**Linear regression** model was used for predicting the house prices. 
* Y (Target/Dependent variable) - Price
* X ( Features/Independent variables) - [bedrooms,facades,liv_area,surface_area,fireplace,terrace,garden,pool,condition]
* Using **Pickle** library to save the model

**Libraries used:**
* Pandas for data analysis
* Numpy for data analysis
* Sklearn for training and building the model 
* **Pickle** library to save the model

## Application features 
Routes
* / -> alive
* /form -> Return a form for user's output
* /predict -> Return a prediction

## API in use: 
**https://house-predict-becode.herokuapp.com/**
