# Name: Justin Morrow
# Date: 02/21/2025
# Assignment: CSD325 Module 9.2 "APIs"
# Purpose: Create a Python program to use an API for connection and display the results
# I chose the api.weather.gov site since it doesn't require a registered api_key


import requests
import json

# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# URL's to the weather.gov api site that doesn't require an API Key
url_location = "https://api.weather.gov/offices/ABQ" # Page to display the name of "Albuquerque, NM"
url_forecast = "https://api.weather.gov/gridpoints/ABQ/100,119/forecast" # Page to display the 7 day forecast


# Send a GET request to the API servers and store the data from the response to the specified data dictionaries
location_data = requests.get(url_location) # Stored as location_data dictionary
forecast_data = requests.get(url_forecast) # Stored as forecast_data dictionary
return_code = (location_data.status_code) # Defined the return status code as the variable return_code to format below

# if the return code is successful by code 200 it'll run the below code
if return_code == 200:
    print(f"\nServer Response Code: {return_code} from {url_location}\n\nYour request was Successful!\n")
    location = location_data.json() # Store the JSON response of data to a dictionary called location
    forecast = forecast_data.json()  # Store the JSON response of data to a dictionary called forecast

    # 'Albuquerque, NM' is found under 'name' with no higher level reference
    city_name = location.get('name')

    # 'https://www.weather.gov/abq/' is found under 'sameAs' with no higher level reference
    website_url = location.get('sameAs')

    # Generated Date/Time 'generatedAt' is under higher level reference 'properties'
    report_generated = forecast['properties'].get('generatedAt')


    # Print the 7-Day Forecast data specified below in a cleaner filtered view
    print(f"\nBelow is the 7-Day Weather Forecast for {city_name} found on {website_url}."
          f"\nReport Data Generated at UTC: {report_generated}\n")

    # I have this part here for the Unformatted request of the assignment. I'll comment it out on the submitted version
    #print("[Unformatted Print out of the Forecast]\n",forecast)

    # I have this part here for the Formatted request of the assignment. I'll comment it out on the submitted version
    #print("\n\n[Formatted Print out of the Forecast]\n")
    #jprint(forecast)

    # Best print out with an iteration loop to display the items I want to see in the 7-Day Forecast
    for period in forecast['properties']['periods']:
        print(f"{period['name']}: {period['detailedForecast']}")

# if the server response return code is anything other than code 200 it will display the Error message below
else:
    print(f"\nServer Response Code: {return_code}\n\nYour request Failed!\n")
    print("\nFor more information on the returned Server Code Failure please visit:\n")
    print("https://en.wikipedia.org/wiki/List_of_HTTP_status_codes")
