import streamlit as st
import requests
import pandas as pd

st.title('MarieIQ Citizen Science Dashboard')

# NOAA stations: Station ID and Name
stations = {
    "Key West, FL (8724580)": "8724580",
    "New York, NY (8518750)": "8518750",
    "San Francisco, CA (9414290)": "9414290",
    "Seattle, WA (9447130)": "9447130"
}

# Select a station
station_name = st.selectbox("Select NOAA Station for Water Temperature", list(stations.keys()))
station_id = stations[station_name]

# NOAA API endpoint
url = (
    f"https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"
    f"?product=water_temperature&date=recent&units=metric"
    f"&station={station_id}&time_zone=gmt&format=json"
)

st.write(f"### Live Ocean Water Temperature at {station_name}")

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    readings = pd.DataFrame(data["data"])
    readings["t"] = pd.to_datetime(readings["t"])
    readings["v"] = readings["v"].astype(float)

    st.line_chart(data=readings.set_index("t")["v"])
    st.success("Live ocean temperature data loaded successfully.")
except Exception as e:
    st.error(f"Failed to load ocean data: {e}")

# Placeholder: Second dataset section (e.g., ship traffic)
st.write("---")
st.write("### Ship Traffic (Demo Placeholder)")
st.info("This section will show ship traffic data. Coming soon!")
