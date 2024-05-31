import requests
import streamlit as st

API_KEY = "3ffbcfd703msh29472e58de6bd60p1efdb3jsne9d49e32c72b"
API_HOST = "travel-advisor.p.rapidapi.com"

def get_nearby_places(location):
    url = "https://travel-advisor.p.rapidapi.com/locations/v2/auto-complete"
    
    querystring = {
        "query": location,
        "lang": "en_US",
        "units": "km"
    }

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    return data

# Streamlit app
def main():
    st.title("Tourism Chatbot")
    st.text("Enter your location to get nearby tourist places:")
    
    location = st.text_input("Location")
    
    if st.button("Submit"):
        if location:
            result = get_nearby_places(location)
            
            if "data" in result and "Typeahead_autocomplete" in result["data"]:
                places = result["data"]["Typeahead_autocomplete"]["results"]
                
                for place in places:
                    if "__typename" in place and place["__typename"] == "Typeahead_LocationItem":
                        st.write("Name:", place["detailsV2"]["names"]["name"])
                        st.write("Location:", place["detailsV2"]["names"]["longOnlyHierarchyTypeaheadV2"])
                        st.write("Latitude:", place["detailsV2"]["geocode"]["latitude"])
                        st.write("Longitude:", place["detailsV2"]["geocode"]["longitude"])
                        st.write("Place Type:", place["detailsV2"]["placeType"])
                        st.write("Image URL:", place["image"]["photo"]["photoSizes"][0]["url"])
                        st.write("-" * 30)
            else:
                st.write("No results found.")
        else:
            st.write("Please enter a location")

if __name__ == "__main__":
    main()
