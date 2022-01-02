# Transcriptomic signatures for severe COVID-19
This database contains transcriptomics data obtained from patients with severe COVID-19. By analysing multiple datasets, we hope to uncover the transcriptomics signatures that are most predictive of severe COVID-19
## Identifying DEGs for severe COVID-19
1. Identify the files for analysis. Only analyse RNAseq and microarray datasets
2. Record number of subjects each group, and the characteristics of each group. We are most interested in the COVID-19 severe patients. 
3. Download raw data, analyse with Partek, save the header columns the same way as STAGEs, and upload processed data into this GitHub. Save for both raw and processed data (e.g. raw_GSE155454_Acute_vs_Convalescent, processed_GSE155454_Acute_vs_Convalescent).
4. Analyse with STAGEs and save the data table for DEGs (FC > 1.3, q-value < 0.05). Save as DEGs_GSE155454_Acute_vs_Convalescent)
## Identifying converging signatures for severe COVID-19
1. Concatenate DEG table, identify DEGs that appear most often in the datasets
2. Plot correlation matrix between different datasets for the log2FC data and inspect for any outliers
3. Consider ploting the raw counts for these converging signatures
## Make Streamlit dashboard
1. Display study design
2. Display processed data
3. Display interactive volcano plot
4. Display DEG table, and allow export of tables
5. Consider making .gmt files, annotated volcano plots, correlation matrix for users to query their own datasets
