PROJECT OVERVIEW

This project involves exploratory data analysis (EDA) of a dataset containing information about cars, specifically focusing on the distribution of car names and fuel types. The analysis is performed using Python programming language and various libraries, including NumPy, Pandas, Matplotlib, and Seaborn.

DATA IMPORT AND INSPECTION

The code begins by importing the necessary libraries and loading the dataset from a CSV file named "cardekho.csv" into a Pandas DataFrame object called data. The head() and tail() methods are used to inspect the first and last few rows of the dataset, respectively. The describe() method is employed to generate summary statistics for the dataset, including count, mean, standard deviation, min, 25%, 50%, 75%, and max values for each column. Additionally, the info() method is used to display information about the dataset, such as the number of non-null values in each column and the data types of each column.

MISSING VALUE ANALYSIS

The code then checks for missing values in the dataset using the isnull().sum() method, which returns the number of missing values in each column.

CAR NAME DISTRIBUTION ANALYSIS

The code proceeds to analyze the distribution of car names in the dataset. The value_counts() method is used to count the frequency of each unique car name, and the result is printed to the console. A count plot is created using Seaborn's countplot() function to visualize the distribution of car names. The plot is customized with a specified figure size and axis labels.

FUEL TYPE DISTRIBUTION ANALYSIS

Next, the code analyzes the distribution of fuel types in the dataset. The value_counts() method is used to count the frequency of each fuel type, and the result is printed to the console. A pie chart is created using Matplotlib's pie() function to visualize the distribution of fuel types. The chart is customized with labels and a shadow effect. Additionally, a bar plot is created using Pandas' plot.bar() method to visualize the distribution of fuel types.

TECHNICAL SKILLS DEMONSTRATED

This project demonstrates the following technical skills:

Data import and inspection using Pandas
Data summary and description using Pandas
Missing value analysis using Pandas
Data visualization using Seaborn and Matplotlib
Data manipulation and analysis using Pandas


Key Features:

Exploratory data analysis of car dataset
Data visualization using Seaborn and Matplotlib
Insights into distribution of car names and fuel types
Missing value analysis and data summary

Dataset:

Car Dekho dataset (included in the repository)
