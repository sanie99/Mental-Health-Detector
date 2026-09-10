import streamlit as st
import pandas as pd
import joblib

# Loading trained models
logistic_model = joblib.load('models/logistic_model.pkl')
decision_tree_model = joblib.load('models/decision_tree_model.pkl')
random_forest_model = joblib.load('models/random_forest_model.pkl')

# streamlit app
st.title("Healthcare AI Model Prediction")
st.write("This app allows you to input patient data and get predictions from three different machine learning models:")
st.write("- Logistic Regression")
st.write("- Decision Tree")
st.write("- Random Forest")

st.sidebar.header("Input Patient Data")
st.sidebar.warning("Note: Please ensure that the input data is in the correct format and range as expected by the models.")
st.sidebar.write("Please enter the patient data below:")


# Function to get user input
def user_input_features():
    feature1 = st.sidebar.number_input("Depression Score:", min_value=0.0, max_value=100.0)
    feature2 = st.sidebar.number_input("Anxiety Score:", min_value=0.0, max_value=100.0)
    data = {'depression_score': feature1,
            'anxiety_score': feature2,
            }
    features = pd.DataFrame(data, index=[0])
    return features

user_input_df = user_input_features()

if st.sidebar.button("Predict Risk Level"):
    # Making predictions
    logistic_prediction = logistic_model.predict(user_input_df)
    decision_tree_prediction = decision_tree_model.predict(user_input_df)   
    random_forest_prediction = random_forest_model.predict(user_input_df)

    # Displaying predictions
    st.subheader("Predictions from Logistic Regression:")
    if logistic_prediction[0] == 0:
        st.success("Logistic Regression Prediction: Low Risk")
    elif logistic_prediction[0] == 1:
        st.warning("Logistic Regression Prediction: Medium Risk")
    elif logistic_prediction[0] == 2:
        st.error("Logistic Regression Prediction: High Risk")

    st.subheader("Predictions from Decision Tree:")
    if decision_tree_prediction[0] == 0:
        st.success("Decision Tree Prediction: Low Risk")
    elif decision_tree_prediction[0] == 1:
        st.warning("Decision Tree Prediction: Medium Risk")
    elif decision_tree_prediction[0] == 2:
        st.error("Decision Tree Prediction: High Risk")

    st.subheader("Predictions from Random Forest:")
    if random_forest_prediction[0] == 0:
        st.success("Random Forest Prediction: Low Risk")
    elif random_forest_prediction[0] == 1:
        st.warning("Random Forest Prediction: Medium Risk")
    elif random_forest_prediction[0] == 2:
        st.error("Random Forest Prediction: High Risk")