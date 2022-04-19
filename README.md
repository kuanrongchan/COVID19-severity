# Introduction to database
This database is a curation of 6 transcriptomics datasets comparing the gene expression in severe COVID-19 and mild COVID-19 subjects. Each database contains raw count data and a processed file, where the raw count data may be visualised with the box and strip plots in the app. The processed files contain p-value (t-test), adjusted p-value (BH step-up procedure), ratio, and fold-change data between severe COVID-19 and mild COVID-19, or severe COVID-19 and healthy subjects. The transcriptomics data may be found in the counts and anova folders respectively.

# Severe COVID-19 datasets included in the study
## 1. Fong et al., 2021. 
Dataset compares the gene expression differences between 14 severe COVID-19, 18 mild COVID-19, and 6 healthy subjects.
## 2. Bibert et al., 2021
Dataset compares the gene expression differences between 15 severe COVID-19, 63 mild COVID-19, and 27 healthy subjects.
## 3. McClain et al., 2021
Dataset compares the gene expression differences between 6 severe COVID-19, 10 mild COVID-19, and 19 healthy subjects.
## 4. Overmyer et al., 2021
Dataset compares the gene expression differences between 50 severe COVID-19 and 50 mild COVID-19 subjects. 
## 5. Arunachalam et al., 2020
Dataset compares the gene expression differences between 4 severe COVID-19, 12 mild COVID-19, and 17 healthy subjects.
## 6. Carapito et al., 2022
Dataset compares the gene expression differences between 46 severe COVID-19 and 23 mild COVID-19 subjects. 

# Website
Database app website instance is accessible at https://share.streamlit.io/kuanrongchan/covid19-severity/main/app.py

Users can modify the codes to launch the app on your computer by doing these steps:
1.
2.
3.

# Getting Started
To use the app:
1. Select a database to query
2. Search for your gene of interest using the filters indicated in the dataframe headers.
3. Tick the checkbox next to the gene of interest. Note that only one gene can be selected at a time for graph plotting.
4. Box and strip plots of the selected gene of interest in the dataset will be plotted. Mouse over the various plots for more in-depth statistics of each group.
