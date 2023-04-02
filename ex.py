import time
import base64
import pandas as pd
import geopandas
import streamlit as st
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import plotly_express as px
import webbrowser
with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
st.image("1.png")
st.title("Geolocation using Python")
st.markdown("Upload a CSV File with address columns(Street name & number , Postcode , City)")
if st.button('CSV File'):
    fi=st.file_uploader('choose a csv file',accept_multiple_files=True,type=['csv'])
