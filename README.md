# Tourism-Chatbot
This repository contains the code for a Tourism Chatbot built using Streamlit. The chatbot allows users to input a location and receive information about nearby tourist places using the Travel Advisor API from RapidAPI.

Features:
* Input a location to find nearby tourist places.
* Display information about tourist places such as name, location, latitude, longitude, place type, and an image URL.
* Simple and user-friendly web interface.

Installation:
Prerequisites:
* Python 3.7 or higher
* pip (Python package installer)
* Streamlit
* Requests

  Setting Up
Clone the repository:
git clone https://github.com/your-username/tourism-chatbot.git
cd tourism-chatbot

Install required packages:
pip install streamlit requests

Set your RapidAPI credentials:

* Open the main.py file.
* Replace the API_KEY and API_HOST with your RapidAPI credentials.

  Running the Application
Start the Streamlit app:
streamlit run main.py

Open the login page:
* Open index.html in your web browser.
* Login to the chatbot:

Enter any username and password.
Click on the "Log In" button to be redirected to the Streamlit app.

API Usage:
This application uses the Travel Advisor API from RapidAPI to fetch information about tourist places. Make sure you have a valid API key from RapidAPI.
