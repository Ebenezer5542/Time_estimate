import streamlit as st 
import joblib
import pandas as pd
import re
from datetime import datetime, timedelta


import streamlit as st
import pandas as pd

# Load town names
df = pd.read_csv("towns.csv")
towns = df["town_name"].tolist()
town_dict = dict(zip(df["town_name"], df["code"]))  # Map town names to codes





model = joblib.load('time_estimate.pkl')


st.title('Time Estimate App')
st.sidebar.title('NAVIGATION')
nav = st.sidebar.selectbox("Go to", ['Home', 'Estimate Time'])

if nav == 'Home':
    st.write('Estimate Your Arrival Time with Ease')
    st.markdown("""Tired of unpredictable commute times? Our app helps you estimate your arrival time based on:

Get real-time insights and plan your commute smarter!""")
    st.write("✅ Your departure time")
    st.write("✅ Your transport mode")
    st.write("✅ Your home location")
    st.write("✅ Your office location")
    st.title("How it works")
    st.markdown("""Enter your departure details.
Select your transport mode.
Get an estimated time of arrival.
Start now and take control of your daily commute!""")
    
    
    
    
## Prediction Page
if nav == 'Estimate Time':
    st.title('Estimate Your Arrival Time')
    st.write('Please enter your details to estimate your arrival time')
    
    # Departure time
    dep_time = st.text_input("Enter your time (HH:MM format):")
    st.write(f"You entered: {dep_time}")
    
    if dep_time:  # Only validate if the user has entered something
        if re.match(r"^([01]\d|2[0-3]):[0-5]\d$", dep_time):
            st.success(f"Valid departure time: {dep_time}")
        else:
            st.error("Invalid format! Use HH:MM (24-hour format)")

    
    # Transport mode
    trans_mode = st.selectbox('Transport Mode', ['Trotro', 'Taxi', 'Private Vehicle', 'Walking'])
    
    # Home location
    home_select = st.selectbox("Select your home location:", towns)
    st.write(f"You selected: {home_select}")

    
    # Office location
    office_select = st.selectbox("Select your office location:", towns)
    st.write(f"You selected: {office_select}")   
    
    
    ##COnverting the town names to town ids
    home_code = town_dict.get(home_select, None)  # Get town code
    office_code = town_dict.get(office_select, None)  # Get town code


    
    ## convert time to seconds
    time_in_seconds = None  # Default value

    if dep_time:  # Only validate if the user has entered something
        try:
            time_obj = datetime.strptime(dep_time, "%H:%M")  # Convert to time object
            time_in_seconds = time_obj.hour * 3600 + time_obj.minute * 60  # Convert to seconds  
        except ValueError:
            st.error("Invalid time format! Use HH:MM (24-hour format)")  
    
    ## COnvert transport mode to numerical value
    mode_t = {'Trotro': 1, 'Taxi': 2, 'Private Vehicle': 3, 'Walking': 4}
    mode = None
    if trans_mode=='Trotro':
        mode = 1
    elif trans_mode=='Taxi':
        mode = 2
    elif trans_mode == 'Private Vehicle':
        mode = 3
    else: mode = 4
    
    #### Predict button
    if st.button('Predict'):
        features = [ home_code, office_code, mode,time_in_seconds]
        prediction = model.predict([features])
        
        ar_time = (prediction + time_in_seconds)
        ar_time = int(ar_time[0])
        arrival_time = str(timedelta(seconds=(ar_time)))  # Converts to HH:MM:SS
        hh_mm = arrival_time.split('.')[0]   # Removes milliseconds
        #st.write(f"Debug - Selected home code: {home_code}")
        #st.write(f"Debug - Selected office code: {office_code}")
        #st.write(f"Debug - Selected mode: {mode}")
        #st.write(f"Debug - Departure time in seconds: {time_in_seconds}")
        #st.write(f"Debug - Arrival time in seconds: {ar_time}")

        st.success(f'Estimated arrival time: {hh_mm}')
        st.write('🚗 Safe travels! 🚗')
