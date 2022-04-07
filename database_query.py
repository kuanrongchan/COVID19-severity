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


st.title("Database Query")
st.markdown('''
 <div style="text-align: justify">
This database is a curation of 6 datasets which study the differences between patients with severe or mild COVID-19 and healthy controls.

## Getting Started

1. Search for your gene of interest below in the first column of this dataframe or use the various filters in the dataframe headers and tick the checkbox
2. Select a database to query below

</div>
''', unsafe_allow_html=True)

df_paths = {"Fong 2021": ["counts/GSE155454_counts.csv", "anova/GSE155454_anova.csv"],
            "Bibert 2021":["counts/Bibert2021_counts.csv","anova/Bibert2021_anova.csv"],
            "McClain 2021":["counts/GSE161731_COVID_counts.csv","anova/GSE161731_anova.csv"],
            "Overmyer 2021":["counts/GSE157103_counts.csv","anova/GSE157103_anova.csv"],
            "Arunachalam 2020":["counts/GSE152418_counts.csv","anova/GSE152418_anova.csv"],
            "Carapito 2022":["counts/GSE172114_counts.csv","anova/GSE172114_anova.csv"]}

dfchoice = st.selectbox(label='Select a dataset', options=df_paths.keys())

df, df_anova = pd.read_csv(df_paths[dfchoice][0], index_col=0), pd.read_csv(df_paths[dfchoice][1]) # probably have to insert a for loop from here if we want a comparative box plot between datasets

######## Ag-Grid Stuff ###########
gb = GridOptionsBuilder.from_dataframe(df_anova)
gb.configure_selection('single', use_checkbox=True, pre_selected_rows=[0]) # allows for checkbox selection of the dataframe. Shows the anova data but will plot the raw expression counts
gridOptions = gb.build()

data = AgGrid(df_anova, gridOptions=gridOptions, theme='streamlit', update_mode=GridUpdateMode.SELECTION_CHANGED) # assigning a variable as it returns a dict of data and selected columns
##################################

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
