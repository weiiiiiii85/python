# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:41:19 2024

@author: user
"""

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Create the confusion matrix
conf_mat = confusion_matrix(y, y_kmeans)

# Plot the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Cluster 1', 'Cluster 2', 'Cluster 3'],
            yticklabels=iris.target_names)
plt.title('Confusion Matrix for K-means Clustering of Iris Dataset')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()
