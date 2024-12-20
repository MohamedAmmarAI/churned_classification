# User Churn Prediction App
This is a **Streamlit-based web application** that predicts whether a user is likely to churn based on their behavioral data.
The application was built using machine learning algorithms, specifically a **Random Forest Classifier**. 
The model was trained using features extracted from user activity data, and the app provides a user-friendly interface for inputting data and viewing predictions.

## Features
- **User Input**: The app takes user activity details (like sessions, days after onboarding, total navigations, and more) as input.
- **Prediction**: It outputs a prediction on whether the user will churn or not.
- **Interactive UI**: Built using **Streamlit** for an interactive and responsive user interface.
- **Model**: The app uses a **Random Forest Classifier** trained on labeled churn data.

## Screenshots

![image](https://github.com/user-attachments/assets/77bbda52-adad-49bc-b409-3b95645dbefb)

## Installation

### Prerequisites
Make sure you have the following installed:
- [Python 3.11+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MohamedAmmarAi/user-churn-prediction-app.git
   cd user-churn-prediction-app

2.  Create a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
   
3. Install required dependencies:
   pip install -r requirements.txt
   pip install streamlit scikit-learn joblib imbalanced-learn matplotlib seaborn

## Running the Application
   1. Run the app
      streamlit run app.py
   2. View the app in your browser: After running the above command, a local web server will start.
   3.  You can access the app at https://churnedclassification-9m3zxytx7iswnxlxxldoo2.streamlit.app/


## Project Structure
   user-churn-prediction-app/

 - app.py                    # Streamlit app entry point
 - rf_model.pkl              # Pretrained Random Forest model (saved using joblib)
 - scaler.pkl                # Pretrained StandardScaler (for scaling input data)
 - pca.pkl                   # Pretrained PCA (for dimensionality reduction)
 - README.md                 # This README file
 - requirements.txt          # Python dependencies
 - data/
    └─waze_dataset.csv       # Dataset used for training the model (optional to include)

## Model Details
 - Model Used: Random Forest Classifier
 - Libraries: scikit-learn for model training and imbalanced-learn for handling class imbalance.
 - Preprocessing:
         - Features are normalized using StandardScaler.
         - PCA (Principal Component Analysis) is applied for dimensionality reduction.
         - SMOTE (Synthetic Minority Over-sampling Technique) is used to balance the training data.

## Technologies Used
 - Programming Language: Python 3.11+
 - Machine Learning: scikit-learn, imbalanced-learn
 - Data Processing: pandas, numpy
 - Visualization: matplotlib, seaborn
 - Web Framework: Streamlit



