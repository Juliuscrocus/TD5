import requests

def get_manor_ids(place_id):
    # Make a request to the API to get the data for the given place id
    response = requests.get(f'https://opendomesday.org/api/places/{place_id}/')

    # Convert the response to JSON format
    data = response.json()

    # Extract the manor ids from the JSON data and store them in a list
    manor_ids = [manor['id'] for manor in data['manors']]

    # Return the list of manor ids
    return manor_ids

# Check that calling your module does not produce any output
if __name__ == '__main__':
    manor_ids = get_manor_ids('db/Abney')
    assert len(manor_ids) == 3
    print(manor_ids)
