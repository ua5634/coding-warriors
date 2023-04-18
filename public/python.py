# Basic Analysis and Visualization
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import csv,json
from datetime import timedelta
# Mapping
import geopandas
import geopy
from geopy.geocoders import Nominatim
import folium
from geopy.extra.rate_limiter import RateLimiter
from folium import plugins
from folium.plugins import MarkerCluster
# Statistical OLS Regression Analysis matplotlib inline
import statsmodels.api as sm
from statsmodels.compat import lzip
from statsmodels.formula.api import ols
#Scipy sklearn Predictions
from sklearn.ensemble import GradientBoostingRegressor

# Pull in JSON and set index as case number (unique key)
df = pd.read_csv("./crimes.csv")
df = df.set_index("Victims")


m = folium.Map([39.086437,-77.161263], zoom_start=12)
for index, row in df.iterrows():
    folium.CircleMarker([row['Latitude'], row['Longitude']],
                        radius=3,
                        popup=row['Crime'],
                        fill_color="#3db7e4", # divvy color
                       ).add_to(m)

# convert to (n, 2) nd-array format for heatmap
dfmatrix = df[['Latitude', 'Longitude']].values
# plot heatmap
m.add_child(plugins.HeatMap(dfmatrix, radius=15))

m.save('./public/map.html')



string = "{Map was created}"
print(string)