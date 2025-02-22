# Name: Justin Morrow
# Date: 02/21/2025
# Assignment: CSD325 Module 9.2 "APIs"
# Purpose: Create a Python program to use for OpenNotify astronauts is http://api.open-notify.org/astros.json

import requests
import json

# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


server_address = "http://api.open-notify.org/astros" # Defining the server address so I can reference it in the response
response = requests.get(server_address) # assigning the server response like message 200 to the variable response
return_code = (response.status_code) # I defined the response status as the variable return_code to format it later


if response.status_code == 200:
    print(f"\nServer Response Code: {return_code} from {server_address}\n\nYour request was Successful!\n")
    print("\nBelow was the data returned from the JSON file via this API\n\n")
    print("This is an unformatted view of the returned data\n")
    print(response.json()) # unformatted view
    print("\n\nThis is a formatted view of the returned data\n")
    jprint(response.json()) # formatted view utilizing the jprint function above
else:
    print(f"\nServer Response Code: {return_code}\n\nYour request Failed!\n")
    print("\nFor more information on the returned Server Code Failure please visit:\n")
    print("https://en.wikipedia.org/wiki/List_of_HTTP_status_codes")

