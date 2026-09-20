# Mental Health Detector

This repository contains a Streamlit application for predicting mental health risk based on user input. The application leverages a trained pipeline that includes preprocessing, feature extraction, and machine learning models. The pipeline is designed to provide users with a personalized assessment of their mental health risk.

## Application Features

The Streamlit application offers the following features:

- **User Input**: Users can input their demographic and behavioral data.
- **Data Preprocessing**: The input data is preprocessed to ensure it is in the correct format for the machine learning models. This includes encoding categorical variables and scaling numerical variables.
- **Feature Extraction**: The preprocessed data is passed through a feature extraction step, which may include techniques such as PCA or other dimensionality reduction methods.
- **Model Prediction**: The feature-extracted data is used to make predictions using the trained machine learning models. The application provides the user with the predicted risk of mental health issues.
- **Model Interpretation**: The application may include tools for interpreting the results of the machine learning models, such as feature importance or SHAP values.
- **Visualization**: The application may include visualizations of the user's input data and the results of the machine learning models.

## Usage

To use the Streamlit application, users need to provide their demographic and behavioral data. The application will preprocess the data, extract features, and make predictions using the trained machine learning models. The results will be displayed to the user, along with any visualizations or interpretations of the model predictions.

## Overview

The analysis focuses on identifying patterns in variables such as:

- age
- gender
- employment status
- work environment
- mental health history
- stress level
- sleep hours
- physical activity
- depression and anxiety scores
- social support and productivity
- mental health risk category

The goal is to better understand the relationships between behavioral and demographic indicators and mental health outcomes.

## Project Status

This repository currently includes:

- Data exploration notebooks
- Data preprocessing notebooks
- Structured analysis of a mental health dataset
- A deployed Streamlit application for interactive data exploration and insights

The project has progressed beyond exploratory analysis and is now available as a functional web application. Users can interact with the trained pipeline and visualize results through the Streamlit interface.

Future enhancements may include model improvements, additional features, API integration, and expanded deployment options.

## Repository structure

```text
Mental-Health-Detector/
├── README.md
├── Data Exploration/
│   └── data_exploration.ipynb
├── Data Preprocessing/
│   └── data_preprocessing.ipynb
└── data/
    └── mental_health_dataset.csv
```

Note: the notebooks reference a dataset located at `data/mental_health_dataset.csv`. If the dataset is not already present in your local copy, add it before running the notebooks.

## Dataset

The dataset contains approximately 10,000 records and includes the following fields:

- `age`
- `gender`
- `employment_status`
- `work_environment`
- `mental_health_history`
- `seeks_treatment`
- `stress_level`
- `sleep_hours`
- `physical_activity_days`
- `depression_score`
- `anxiety_score`
- `social_support_score`
- `productivity_score`
- `mental_health_risk`

The target variable, `mental_health_risk`, is categorized as:

- `Low`
- `Medium`
- `High`

## Notebooks

### Data Exploration

The exploration notebook reviews the dataset structure, checks missing values, summarizes statistical trends, and visualizes relationships between variables. It also investigates the distribution of key risk factors and correlations relevant to mental well-being.

### Data Preprocessing

The preprocessing notebook cleans and transforms the data for downstream analysis. Key steps include:

- loading the dataset
- converting categorical values into numeric encodings
- preparing features for model training or further analysis
- making the dataset consistent for machine learning workflows

## Models

The project includes three machine learning models trained to predict mental health risk based on the input features:

1. Logistic Regression
2. Decision Tree
3. Random Forest

Each model is saved as a separate `.pkl` file for deployment and inference.

## Setup

Use Python 3.10+ and install the required packages:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install pandas matplotlib seaborn notebook jupyter
```

## Running the project

1. Place the dataset in `data/mental_health_dataset.csv`.
2. Launch Jupyter Notebook:

```bash
jupyter notebook
```

3. Open the notebook files from the project folders.
4. Run the cells in sequence to explore and preprocess the data.

## Typical workflow

1. Load and review the dataset in the exploration notebook.
2. Understand summary statistics and feature patterns.
3. Use the preprocessing notebook to encode and structure the data.
4. Extend the project with modeling, validation, or report generation as needed.

## Notes

- The notebooks are designed for analysis and experimentation rather than deployment.
- The project is primarily a data science / research starter project focused on mental health risk detection.
- The dataset appears to be synthetic and designed for educational or analytical use.

## License

This project does not currently include a license file. If you plan to share or publish the project, add a license such as MIT or Apache 2.0 depending on your intended usage.
