import requests

# Make a request to the API to get the data for Derbyshire
response = requests.get('https://opendomesday.org/api/places/?county=Derbyshire')

# Convert the response to JSON format
data = response.json()

# Extract the place ids from the JSON data and store them in a list
place_ids = [place['id'] for place in data['results']]

# Print the list of place ids
print(place_ids)