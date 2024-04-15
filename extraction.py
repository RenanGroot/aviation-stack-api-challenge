import requests
import pandas as pd


# CODE IDEA
# Check for API results
# Think in a way to save the results as files (csv)
#   Create a file for each day
#       Landing files
# Create another script that is going to read all the csv files and upload to a SQL locally

def retrive_hist_flights(date:str):
    """
    This function retrieves the data from historical flights of a specific date

    Args:
        date(str): Flight date
    Returns:
    
    """
    params = {
    "access_key" : "YOUR API KEY",
    "flight_date": date
    }

    api_result = requests.get('https://api.aviationstack.com/v1/flights', params)

    api_response = api_result.json()

    



    return temp_df




print(retrive_hist_flights("2024-04-14"))