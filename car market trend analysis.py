# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cardekho dataset from a CSV file
data = pd.read_csv("cardekho.csv")

# Display the first few rows of the dataset
data.head()

# Display the last few rows of the dataset
data.tail()

# Generate summary statistics for the dataset
data.describe()

# Display information about the dataset, including data types and counts
data.info()

# Check for missing values in the dataset
data.isnull().sum()

# Display the count of each unique car name
print(data.Car_Name.value_counts())

# Create a figure with a specified size
fig_dims = (12, 20)
fig, ax = plt.subplots(figsize=fig_dims)

# Create a count plot of car names using seaborn
sns.countplot(y=data.Car_Name, ax=ax, data=data)

# Display the count of each fuel type
print(data.Fuel_Type.value_counts())

# Create a pie chart of fuel types
plt.pie(data.Fuel_Type.value_counts(), labels=["Petrol", "Diesel", "CNG"], shadow=True)
plt.show()

# Create a bar plot of fuel types
data.Fuel_Type.value_counts().plot.bar()
