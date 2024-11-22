import streamlit as st
import requests
from datetime import datetime

'''
# TaxiFareModel
'''

st.markdown('## Calculate the price of your next ride')

url_lewagon = 'https://taxifare.lewagon.ai/predict'
url = 'https://taxifare-795872844038.europe-west1.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':
    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


date = st.date_input("Date")
time = st.time_input("Time") #step parameter not working
date_str = date.strftime("%Y-%m-%d")
time_str = time.strftime("%H:%M")

pickup_datetime = date_str + " " + time_str
pickup_longitude = st.number_input("Pickup longitude", value=-73.950655, format="%0.6f")
pickup_latitude = st.number_input("pickup latitude", value=40.783282, format="%0.6f")
dropoff_longitude = st.number_input("Dropoff longitude", value=-73.984365, format="%0.6f")
dropoff_latitude = st.number_input("Dropoff latitude", value=40.769802, format="%0.6f")
passenger_count = st.number_input("Passenger count", value=2)

params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}


if st.button('Calculate'):
    st.write('Calculating your price')
    response = requests.get(url, params=params)
    fare = response.json().get('fare')
    st.write("Your fare is:", fare)
else:
    st.write('Click me to get your fare')


# http://127.0.0.1:8000/predict?pickup_datetime=2014-07-06+19:18:00&pickup_longitude=-73.950655&pickup_latitude=40.783282&dropoff_longitude=-73.984365&dropoff_latitude=40.769802&passenger_count=2
# http://127.0.0.1:8000/predict?pickup_datetime=2024-11-22+12%3A44&pickup_longitude=-73.950655&pickup_latitude=40.783282&dropoff_longitude=-73.984365&dropoff_latitude=40.769802&passenger_count=2

# pickup_datetime: str,  # 2014-07-06 19:18:00
# pickup_longitude: float,    # -73.950655
# pickup_latitude: float,     # 40.783282
# dropoff_longitude: float,   # -73.984365
# dropoff_latitude: float,    # 40.769802
# passenger_count: int
    
# full_url = requests.Request('GET', url, params=params).prepare().url
# print(f"Full URL being called: {full_url}")