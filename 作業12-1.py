# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:41:17 2024

@author: user
"""

# Import necessary libraries
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# Create a DataFrame for better handling
df = pd.DataFrame(X, columns=iris.feature_names)
df['species'] = y

# Define colors for different species
colors = ['red', 'blue', 'green']
species_colors = [colors[label] for label in y]

# Plot the scatter plot
plt.figure(figsize=(8, 6))
for i, target_name in enumerate(target_names):
    plt.scatter(df[df['species'] == i].iloc[:, 0], 
                df[df['species'] == i].iloc[:, 1], 
                label=target_name,
                c=colors[i])
plt.title('Iris Dataset Scatter Plot')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.legend()
plt.show()
