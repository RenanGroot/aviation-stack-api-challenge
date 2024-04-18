import requests
import pandas as pd
import json


# CODE IDEA
# Check for API results
# Think in a way to save the results as files (csv)
#   Create a file for each day
#       Landing files
# Create another script that is going to read all the csv files and upload to a SQL locally

def retrive_hist_flights(date:str, airline:str, option:str):
    """
    This function retrieves the data from historical flights of a specific date

    Args:
        date(str): Flight date
        airline(str): Airline name, IATA code or ICAO code. According to the option explicited on the args.
        option(str): "name", "iata" or "icao". Option for the airline filter.
    Returns:
    
    """
    params = {
    "access_key" : "YOUR API KEY",
    "flight_date": date
    }

    # Adding to params the airline filter option selected
    if option == "name":
        params["airline_name"] = airline
    elif option == "iata":
        params["airline_iata"] = airline    
    elif option == "icao":
        params["airline_icao"] = airline
    
    # Condition if the user didn't give a right option
    else:
        print('You should give an option for the airline filter:\n There are three possibilites:"name", "iata" or "icao"')

    # Requesting from API endpoint
    try:
        api_result = requests.get('https://api.aviationstack.com/v1/flights', params)
    
    except:
        print("Failed to get information from the server")

    api_response = api_result.json()

    df_fact = pd.DataFrame(columns=["id","flight_date","flight_status"])
    
    for row in api_response["data"]:

        # TODO
        #   Also I need to continue test to create a csv file containing the fact table before creating the dimension's ones.
        # Unique id created for each flight registred
        #   flight date + flight iata + aircraft iata
        # Condition due some data are missing aircraft information
        if row["aircraft"] == None:
            f_id = (row["flight_date"]) + (row["flight"]["iata"]) + "None"
        else:
            f_id = (row["flight_date"]) + (row["flight"]["iata"]) + (row["aircraft"]["iata"])

        f_date = row["flight_date"]
        f_status = row["flight_status"]
        df_fact.loc[len(df_fact.index)] = [f_id, f_date, f_status]
    
    df_fact.to_csv("test.csv",index=False)

    return api_response



retrive_hist_flights("2024-04-14", "dl", "iata")