#Dependencies
import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#Remove this when working locally to access Github Secrets
os.environ['MAPBOX_API_KEY'] = st.secrets['MAPBOX_API_KEY']

#Mapbox Access Token
mapbox_access_token = os.environ['MAPBOX_API_KEY']

#Add & Clean Data
data = pd.read_csv('zip_code_database.csv')
data.dropna(subset=['ZIP'], inplace=True)

#Run Plotly Express
px.set_mapbox_access_token(mapbox_access_token)

fig = px.scatter_mapbox(data, 
                        lat="Latitude", 
                        lon="Longitude", 
                        color="Population",
                        color_continuous_scale=px.colors.cyclical.IceFire, 
                        size="Population", 
                        size_max=15, 
                        zoom=10, 
                        hover_name="City_ZIP",
                  )

fig.update_layout(
    title='Michigan Zip Codes by Population #',
    autosize=True,
    hovermode='closest',
    showlegend=False,
     mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=45,
            lon=-85
        ),
        pitch=0,
        zoom=4.5,
        style='light'
    ),
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

#Notes: Basically all set to go. Just need to get lat/long data and format it correctly in spreadsheet and then upload it/adjust details. Then update Streamlit App. Then I can get to work.
#Also need to drop all rows where population is zero.