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
- [Python 3.7+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MohamedAmmarAi/user-churn-prediction-app.git
   cd user-churn-prediction-app

2- Create a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
