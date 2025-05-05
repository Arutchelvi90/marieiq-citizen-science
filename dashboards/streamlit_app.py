import streamlit as st
import requests
import pandas as pd

st.title('MarieIQ Citizen Science Dashboard')
st.write('Live Ocean Water Temperature (NOAA - Key West Station)')

# NOAA API endpoint for Key West station water temperature
url = (
    "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"
    "?product=water_temperature&date=recent&units=metric"
    "&station=8724580&time_zone=gmt&format=json"
)

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    readings = pd.DataFrame(data["data"])
    readings["t"] = pd.to_datetime(readings["t"])
    readings["v"] = readings["v"].astype(float)

    st.line_chart(data=readings.set_index("t")["v"])
    st.success("Live ocean data loaded successfully.")
except Exception as e:
    st.error(f"Failed to load ocean data: {e}")
