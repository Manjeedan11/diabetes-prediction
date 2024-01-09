# Diabetes Prediction using K-Nearest Neighbors (KNN)

This repository contains a Python script for predicting diabetes using the K-Nearest Neighbors (KNN) algorithm. The code uses the popular machine learning library scikit-learn and involves preprocessing the data, handling missing values, and training a KNN classifier.

## Dataset

The dataset used in this project is named "diabetes.csv." It is assumed to contain information related to diabetes, with columns such as Glucose, BloodPressure, SkinThickness, BMI, Insulin, and others.

## Code Overview

### Data Preprocessing:

- Replace zero values in specific columns ('Glucose', 'BloodPressure', 'SkinThickness', 'BMI', 'Insulin') with the mean of non-zero values.
- Split the dataset into input features (X) and output labels (y).

### Train-Test Split:

- Split the dataset into training and testing sets using the `train_test_split` function from scikit-learn.

### Feature Scaling:

- Standardize the features using the `StandardScaler` to ensure that all features have the same scale.

### K-Nearest Neighbors Classification:

- Create a KNN classifier with parameters (n_neighbors=11, p=2, metric='euclidean').
- Train the classifier using the training data.

### Prediction and Evaluation:

- Predict the labels for the test set using the trained classifier.
- Evaluate the model performance using confusion matrix and F1 score.

## Running the Code

To run this code, make sure you have Python installed along with the required libraries specified in the script. You can install these dependencies using:

```bash
pip install pandas numpy scikit-learn

