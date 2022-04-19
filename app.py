import pandas as pd
import numpy as np
# import time
# import math
import re
# import base64
# from io import BytesIO

# from scipy.spatial.distance import pdist, squareform
# from scipy.cluster.hierarchy import dendrogram, linkage
# from scipy import stats

import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

import plotly.graph_objects as go
# from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import plotly.express as px
# import matplotlib.pyplot as plt
# import seaborn as sns


st.title("Severe COVID-19 blood transcriptomics database")
st.markdown('''
 <div style="text-align: justify">
This database is a curation of 6 transcriptomics datasets which compare gene expression differences between severe and mild COVID-19 patients.

## Getting Started

1. Select a dataset to query:


</div>
''', unsafe_allow_html=True)

df_paths = {"Fong et al., 2021": ["counts/GSE155454_counts.csv", "anova/GSE155454_anova.csv"],
            "Bibert et al., 2021":["counts/Bibert2021_counts.csv","anova/Bibert2021_anova.csv"],
            "McClain et al., 2021":["counts/GSE161731_COVID_counts.csv","anova/GSE161731_anova.csv"],
            "Overmyer et al., 2021":["counts/GSE157103_counts.csv","anova/GSE157103_anova.csv"],
            "Arunachalam et al., 2020":["counts/GSE152418_counts.csv","anova/GSE152418_anova.csv"],
            "Carapito et al., 2022":["counts/GSE172114_counts.csv","anova/GSE172114_anova.csv"]}

df_desc = {"Fong et al., 2021": ("14 severe COVID-19, 18 mild COVID-19, and 6 healthy", "GSE155454", "https://doi.org/10.15252/emmm.202114045"),
            "Bibert et al., 2021":("15 severe COVID-19, 63 mild COVID-19, and 27 healthy", "Bibert2021", "https://dx.doi.org/10.3389%2Ffimmu.2021.666163"),
            "McClain et al., 2021":("6 severe COVID-19, 10 mild COVID-19, and 19 healthy", "GSE161731", "https://www.nature.com/articles/s41467-021-21289-y"),
            "Overmyer et al., 2021":("50 severe COVID-19 and 50 mild COVID-19", "GSE157103", "https://doi.org/10.1016/j.cels.2020.10.003"),
            "Arunachalam et al., 2020":("4 severe COVID-19, 12 mild COVID-19, and 17 healthy", "GSE152418", "https://doi.org/110.1126/science.abc6261"),
            "Carapito et al., 2022":("46 severe COVID-19 and 23 mild COVID-19", "GSE172114", "https://doi.org/10.1126/scitranslmed.abj7521")}

dfchoice = st.selectbox(label='Select a dataset', options=df_paths.keys())

df, df_anova = pd.read_csv(df_paths[dfchoice][0], index_col=0), pd.read_csv(df_paths[dfchoice][1]) # probably have to insert a for loop from here if we want a comparative box plot between datasets



st.markdown(' 2. Search for your gene of interest using the filters indicated the dataframe headers') 
st.markdown(' 3. Tick the checkbox indicated beside the gene name. Note that only one gene can be selected at a time for graph plotting. For multiple gene queries, please use processed data available at https://github.com/kuanrongchan/COVID19-severity')


######## Ag-Grid Stuff ###########
gb = GridOptionsBuilder.from_dataframe(df_anova)
gb.configure_selection('single', use_checkbox=True, pre_selected_rows=[0]) # allows for checkbox selection of the dataframe. Shows the anova data but will plot the raw expression counts
gridOptions = gb.build()

with st.expander("Expand for dataset details", expanded=False):
    st.markdown(f'''
    <div style="text-align: justify">

    **Description of {dfchoice} dataset**

    {dfchoice} dataset compares the gene expression differences between {df_desc[dfchoice][0]} subjects. 
    Raw count data can be found in [{df_desc[dfchoice][1]}]({df_desc[dfchoice][2]}) and the full processed data is available at https://github.com/kuanrongchan/COVID19-severity. 
    In the processed data, the fold-change, p-value (t-test) and adjusted p-value (BH step-up procedure) between severe vs mild and severe vs healthy subjects are presented.

    </div>
    ''', unsafe_allow_html=True)
    
data = AgGrid(df_anova, gridOptions=gridOptions, theme='streamlit', update_mode=GridUpdateMode.SELECTION_CHANGED) # assigning a variable as it returns a dict of data and selected columns
##################################

st.markdown(' 4. Box plots and strip plots comparing severe COVID-19, mild COVID-19 or healthy subjects. Users can mouse over the plots to gather data statistics') 


idx_name = df_anova.columns[0] # Prevents the need to rename the anova columns
fig = go.Figure()

if len(data['selected_rows']) != 0:
    severe = df.filter(regex=('[Ss]evere'), axis=1)
    mild = df.filter(regex=('[Mm]ild'), axis=1)
    healthy = df.filter(regex=('[Hh]ealthy'), axis=1)
    genechoice = data['selected_rows'][0][idx_name]
    fig.add_trace(go.Box(y=severe.loc[genechoice], name='Severe', boxpoints='all', marker_color = 'indianred'))
    fig.add_trace(go.Box(y=mild.loc[genechoice], name="Mild", boxpoints='all', marker_color='royalblue'))
    fig.add_trace(go.Box(y=healthy.loc[genechoice], name="Healthy", boxpoints='all', marker_color='lightseagreen'))
    
    fig.update_layout(title=f"Box Plot of {genechoice} in {dfchoice} Dataset", title_x=0.5,
                        xaxis_title="Severity of Disease", yaxis_title="Expression")
    st.plotly_chart(fig)
