import streamlit as st
import joblib
import numpy as np

# Load the saved model, scaler, and PCA
model = joblib.load('rf_model.pkl')
scaler = joblib.load('scaler.pkl')
pca = joblib.load('pca.pkl')

# Custom CSS for full-page background color
st.markdown(
    """
    <style>
    /* Change the entire background color */
    .stApp {
        background-color: #d3d3d3;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and header
st.title('User Churn Prediction App')
st.write("This app predicts whether a user is likely to churn based on their behavior data.")

# Collecting inputs from the user
st.subheader('User Input Features')

# Using columns for better layout
col1, col2, col3 = st.columns(3)

with col1:
    sessions = st.number_input('Sessions', min_value=0, step=1)
    n_days_after_onboarding = st.number_input('Days After Onboarding', min_value=0, step=1)

with col2:
    total_navigations_fav1 = st.number_input('Total Navigations to Favorite 1', min_value=0, step=1)
    driven_km_drives = st.number_input('Driven Km in Drives', min_value=0.0, step=0.1)

with col3:
    duration_minutes_drives = st.number_input('Duration of Drives (minutes)', min_value=0.0, step=0.1)
    activity_days = st.number_input('Activity Days', min_value=0, step=1)
    device = st.selectbox('Device Type', ['Android', 'iOS'])

# Converting the device type to numeric (assuming it was label-encoded during training)
device_encoded = 1 if device == 'iOS' else 0

# When the user clicks "Predict"
if st.button('Predict'):
    # Combine user input into an array (in the same order as used during model training)
    user_input = np.array([[sessions, n_days_after_onboarding, total_navigations_fav1, driven_km_drives, 
                            duration_minutes_drives, activity_days, device_encoded]])

    # Scale and transform the input data
    user_input_scaled = scaler.transform(user_input)
    user_input_pca = pca.transform(user_input_scaled)

    # Predict using the model
    prediction = model.predict(user_input_pca)

    # Display the prediction
    st.subheader('Prediction')
    st.write(f'The user is predicted to be: {"Churned" if prediction[0] == 1 else "Not Churned"}')

