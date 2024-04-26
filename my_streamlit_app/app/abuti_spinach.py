import streamlit as st
import datetime
import requests
import os

# Retrieve API keys from environment variables
google_api_key = os.environ.get('GOOGLE_API_KEY')
openweathermap_api_key = os.environ.get('OPENWEATHERMAP_API_KEY')

# Streamlit App
st.title("AbutiSpinach: Your Farming Assistant")
st.markdown("---")
st.image("C:\\abutispinach_logo.jpg")

# Task Selection
task_selection = st.radio("Select Task:", options=["Planting Calendar"])

if task_selection == "Planting Calendar":
    # Gather planting information from the farmer
    st.subheader("Planting Information")
    with st.form("planting_form"):
        location = st.text_input("Location (e.g., city, state, or country):", placeholder="Enter your location")
        crop = st.text_input("Crop (e.g., tomatoes, wheat):", placeholder="Enter the crop name")
        start_date = st.date_input("Start Date:", min_value=datetime.date.today(), help="Select the desired start date for planting")

        submitted = st.form_submit_button("Generate Calendar")

        if submitted:
            if not location or not crop or not start_date:
                st.error("Please fill out all fields.")
            else:
                try:
                    # Get weather information for the specified location
                    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={openweathermap_api_key}&units=metric"
                    weather_response = requests.get(weather_url)
                    weather_data = weather_response.json()

                    # Display weather information
                    if weather_data["cod"] != "404":
                        st.subheader("Current Weather")
                        cols = st.columns(2)
                        with cols[0]:
                            st.write(f"Temperature: {weather_data['main']['temp']}°C")
                            st.write(f"Humidity: {weather_data['main']['humidity']}%")
                        with cols[1]:
                            st.write(f"Weather: {weather_data['weather'][0]['description']}")
                            st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
                    else:
                        st.warning(f"Could not retrieve weather information for {location}.")

                    # Your remaining code for executing farming tasks goes here...

                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    # Handle errors gracefully

st.markdown("---")
st.info("This application was developed by AbutiSpinach to assist farmers with planting calendars and farming advice. For more information or support, please visit our [website](https://abutispinach.com).")
