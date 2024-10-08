# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nIUftfYTxDOCcjt8tsNyWMsZH5aMxc6H
"""

# Import necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load the CSV file into a DataFrame (replace 'iris.csv' with the name of your file)
iris_df = pd.read_csv('IRIS.csv')

# Display the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(iris_df.head())

# Summary statistics of the dataset
print("\nSummary statistics of the dataset:")
print(iris_df.describe())

# Display unique species in the dataset
print("\nUnique species in the dataset:")
print(iris_df['species'].unique())

# Pairplot to visualize relationships between features
sns.pairplot(iris_df, hue='species', markers=["o", "s", "D"])
plt.suptitle('Pairplot of Iris Dataset')
plt.show()

# Prepare the features (X) and target (y)
X = iris_df.drop('species', axis=1)
y = iris_df['species']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the K-Nearest Neighbors (KNN) classifier
knn = KNeighborsClassifier(n_neighbors=3)

# Train the KNN classifier
knn.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn.predict(X_test)

# Assuming you have already run predictions and have y_test and y_pred
# Extract unique species names from the dataset
target_names = iris_df['species'].unique()

# Generate and print the confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Generate and print the classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=target_names))

# Print accuracy score
print("\nAccuracy Score:")
print(accuracy_score(y_test, y_pred))

# Extract unique species names from the dataset
target_names = iris_df['species'].unique()

# Compute the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Create the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=target_names, yticklabels=target_names)
plt.title('Confusion Matrix')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

# Test with new data
new_data = [[5.1, 3.5, 1.4, 0.2]]  # Replace with actual measurements
new_data_scaled = scaler.transform(new_data)

# Make predictions with the trained KNN model
prediction = knn.predict(new_data_scaled)

# Directly print the predicted class label
print("Prediction for new data:", prediction[0])