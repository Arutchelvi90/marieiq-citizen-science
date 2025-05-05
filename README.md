# 🌊 MarieIQ Citizen Science Dashboard

MarieIQ is an open-source citizen science platform focused on sustainable ocean logistics and marine data. This dashboard displays **real-time ocean water temperature** data from NOAA and will soon support ship traffic monitoring and more.

## 🚀 Features

- 🌡️ Live water temperature from NOAA stations (dropdown-selectable)
- 📈 Interactive chart of recent temperature readings
- 🌐 Planned: Ship traffic heatmaps and port analytics
- 🔄 Open data, open science – powered by FastAPI + Streamlit

## 🧪 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/Arutchelvi90/marieiq-citizen-science.git
   cd marieiq-citizen-science
   ```

2. Create a virtual environment and install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run dashboards/streamlit_app.py
   ```

## 🌐 Live App

> Deploy it on [Streamlit Cloud](https://streamlit.io/cloud)  
> App path: `dashboards/streamlit_app.py`

## 📊 Data Sources

- **NOAA Tides & Currents API**: Live sea temperature  
- **Planned**: Global ship traffic datasets (AIS)

## 🤝 Contributing

We welcome pull requests! Check out our Issues tab for ways to get involved.

## 📄 License

MIT License – free to use, share, and build upon.

---
Built with ❤️ by Arutchelvi and contributors.
