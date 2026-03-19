# diabetes-prediction-ml
# Diabetes Prediction Web Application

This project is a machine learning based web application that predicts whether a person is diabetic or not using medical input parameters. The model is trained on a diabetes dataset and integrated with a simple web interface for real-time predictions.

## Overview

The application allows users to enter health-related details such as glucose level, BMI, age, etc., and provides an instant prediction. This project demonstrates how machine learning models can be deployed using a web framework.

## Features

- Simple and user-friendly interface  
- Real-time prediction  
- Machine learning model integration  
- Clean frontend design using HTML and CSS  
- Lightweight backend using Flask  

## Technologies Used

- Python  
- Flask  
- Scikit-learn  
- Pandas  
- NumPy  
- HTML & CSS  

## Project Structure
ML_Web_App/
│── app.py
│── train_model.py
│── diabetes.csv
│── model.pkl
│── templates/
│ └── index.html


## Installation & Setup

1. Clone the repository:git clone  https://github.com/kaushal-prog/diabetes-prediction-ml.git
2. 2. Navigate to the project directory:

cd diabetes-prediction-ml


3. Install required dependencies:

pip install flask pandas scikit-learn numpy


4. Train the model:

python train_model.py


5. Run the application:

python app.py


6. Open your browser and go to:
   http://127.0.0.1:5000/

   
## Input Parameters

The application requires the following inputs:

- Pregnancies  
- Glucose  
- Blood Pressure  
- Skin Thickness  
- Insulin  
- BMI  
- Diabetes Pedigree Function  
- Age  

## Output

The system provides one of the following results:

- Diabetic  
- Not Diabetic  

## Future Enhancements

- Improve model accuracy using advanced algorithms  
- Add input validation and error handling  
- Enhance UI with modern frontend frameworks  
- Deploy the application on cloud platform  

## Author

Kaushal Kakade  
GitHub: https://github.com/kaushal-prog
