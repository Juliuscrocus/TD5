import requests
import pandas as pd

def get_manor_ids(place_id):
    """
    Get the list of manor ids for a given place id.

    Parameters:
    place_id (str): The id of the place to retrieve manor ids for.

    Returns:
    list: The list of manor ids for the given place id.
    """
    # Make a request to the API to get the data for the given place id
    response = requests.get(f'https://opendomesday.org/api/places/{place_id}/')

    # Convert the response to JSON format
    data = response.json()

    # Extract the manor ids from the JSON data and store them in a list
    manor_ids = [manor['id'] for manor in data['manors']]

    # Return the list of manor ids
    return manor_ids

def get_all_manor_ids():
    """
    Get the list of all manor ids in Derbyshire.

    Returns:
    list: The list of all manor ids in Derbyshire.
    """
    # Make a request to the API to get the data for Derbyshire
    response = requests.get('https://opendomesday.org/api/places/?county=Derbyshire')

    # Convert the response to JSON format
    data = response.json()

    # Loop over each place in Derbyshire and get the list of manor ids
    manor_ids = []
    for place in data['results']:
        manor_ids += get_manor_ids(place['id'])

    # Loop over each manor and get the geld paid and total ploughs owned
    data = []
    for manor_id in manor_ids:
        # Make a request to the API to get the data for the given manor id
        response = requests.get(f'https://opendomesday.org/api/manors/{manor_id}/')

        # Convert the response to JSON format
        data = response.json()

        # Extract the geld paid and total ploughs owned from the JSON data
        geld_paid = data['geld']
        total_ploughs = data['ploughs']

        # Add the geld paid and total ploughs owned to the data list
        data.append({
            'manor_id': manor_id,
            'geld_paid': geld_paid,
            'total_ploughs': total_ploughs
        })

    # Return the list of all manors in Derbyshire with their geld paid and total ploughs owned
    return data

def create_dataframe():
    """
    Create a Pandas DataFrame with the geld paid and total ploughs owned for all manors in Derbyshire.

    Returns:
    pandas.DataFrame: A DataFrame with the geld paid and total ploughs owned for all manors in Derbyshire.
    """
    # Get the data for all manors in Derbyshire
    data = get_all_manor_ids()

    # Create a dictionary with the geld paid and total ploughs owned for each manor
    manor_data = {}
    for row in data:
        manor_id = row['manor_id']
        geld_paid = row['geld_paid']
        total_ploughs = row['total_ploughs']
        manor_data[manor_id] = {'geld_paid': geld_paid, 'total_ploughs': total_ploughs}

    # Create a DataFrame from the manor data dictionary
    df = pd.DataFrame.from_dict(manor_data, orient='index')

    # Return the DataFrame
    return df

def sum_geld_and_ploughs():
    """
    Compute the sum of geld paid and total ploughs owned in Derbyshire.

    Returns:
    tuple: A tuple containing the sum of geld paid and total ploughs owned in Derbyshire.
    """
    # Create a DataFrame with the geld paid and total ploughs owned for all manors in Derbyshire
    df = create_dataframe()

    # Compute the sum of geld paid and total ploughs owned in Derbyshire using Pandas
    geld_paid_sum = df['geld_paid'].sum()
    total_ploughs_sum = df['total_ploughs'].sum()

    # Return the sum of geld paid and total ploughs owned in Derbyshire
    return geld_paid_sum, total_ploughs_sum



