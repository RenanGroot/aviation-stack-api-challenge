import requests
import pandas as pd
import json


# CODE IDEA
# Check for API results
# Think in a way to save the results as files (csv)
#   Create a file for each day
#       Landing files
# Create another script that is going to read all the csv files and upload to a SQL locally

#TODO
# Scalate it

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

    # Table definitions:
    df_fact = pd.DataFrame(columns=["id","flight_date","flight_status"])
    df_dim_flight = pd.DataFrame(columns=["id","number","iata","icao"])
    df_dim_airline = pd.DataFrame(columns=["id","name","iata","icao"])
    df_dim_departure = pd.DataFrame(columns=["id","airport", "timezone", "iata", "icao", "terminal", "gate", "delay", "scheduled", "estimated", "actual", "estimated_runway", "actual_runway"])
    df_dim_arrival = pd.DataFrame(columns=["id","airport", "timezone", "iata", "icao", "terminal", "gate", "baggage", "delay", "scheduled", "estimated", "actual", "estimated_runway", "actual_runway"])
    df_dim_aircraft = pd.DataFrame(columns=["id","registration", "iata", "icao", "icao24"])
    
    for row in api_response["data"]:

        # Condition due some data are missing aircraft information
        if row["aircraft"] == None:
            f_id = (row["flight_date"]) + (row["flight"]["iata"]) + "None"
        else:
            f_id = (row["flight_date"]) + (row["flight"]["iata"]) + (row["aircraft"]["iata"])

        # FACT TABLE POPULATE
        f_date = row["flight_date"]
        f_status = row["flight_status"]
        df_fact.loc[len(df_fact.index)] = [f_id, f_date, f_status]

        # DIMENSION FLIGHT TABLE POPULATE
        d_flight_nu = row["flight"]["number"]
        d_flight_ia = row["flight"]["iata"]
        d_flight_ic = row["flight"]["icao"]
        df_dim_flight.loc[len(df_dim_flight.index)] = [f_id, d_flight_nu, d_flight_ia, d_flight_ic]

        # DIMENSION AIRLNE TABLE POPULATE
        d_airline_na = row["airline"]["name"]
        d_airline_ia = row["airline"]["iata"]
        d_airline_ic = row["airline"]["icao"]
        df_dim_airline.loc[len(df_dim_airline.index)] = [f_id, d_airline_na, d_airline_ia, d_airline_ic]

        # DIMENSION DEPARTURE TABLE POPULATE
        d_departure_ai = row["departure"]["airport"]
        d_departure_ti = row["departure"]["timezone"]
        d_departure_ia = row["departure"]["iata"]
        d_departure_ic = row["departure"]["icao"]
        d_departure_te = row["departure"]["terminal"]
        d_departure_ga = row["departure"]["gate"]
        d_departure_de = row["departure"]["delay"]
        d_departure_sc = row["departure"]["scheduled"]
        d_departure_es = row["departure"]["estimated"]
        d_departure_ac = row["departure"]["actual"]
        d_departure_esrun = row["departure"]["estimated_runway"]
        d_departure_acrun = row["departure"]["actual_runway"]
        df_dim_departure.loc[len(df_dim_departure.index)] = [f_id, d_departure_ai, d_departure_ti, d_departure_ia, d_departure_ic, d_departure_te, d_departure_ga, d_departure_de, d_departure_sc, d_departure_es, d_departure_ac, d_departure_esrun, d_departure_acrun]
    
        # DIMENSION ARRIVAL TABLE POPULATE
        d_arrival_ai = row["arrival"]["airport"]
        d_arrival_ti = row["arrival"]["timezone"]
        d_arrival_ia = row["arrival"]["iata"]
        d_arrival_ic = row["arrival"]["icao"]
        d_arrival_te = row["arrival"]["terminal"]
        d_arrival_ga = row["arrival"]["gate"]
        d_arrival_ba = row["arrival"]["baggage"]
        d_arrival_de = row["arrival"]["delay"]
        d_arrival_sc = row["arrival"]["scheduled"]
        d_arrival_es = row["arrival"]["estimated"]
        d_arrival_ac = row["arrival"]["actual"]
        d_arrival_esrun = row["arrival"]["estimated_runway"]
        d_arrival_acrun = row["arrival"]["actual_runway"]
        df_dim_arrival.loc[len(df_dim_arrival.index)] = [f_id, d_arrival_ai, d_arrival_ti, d_arrival_ia, d_arrival_ic, d_arrival_te, d_arrival_ga, d_arrival_ba, d_arrival_de, d_arrival_sc, d_arrival_es, d_arrival_ac, d_arrival_esrun, d_arrival_acrun]

        # DIMENSION AIRCRAFT TABLE POPULATE
        try:
            d_aircraft_re = row["aircraft"]["registration"]
            d_aircraft_ia = row["aircraft"]["iata"]
            d_aircraft_ic = row["aircraft"]["icao"]
            d_aircraft_ic24 = row["aircraft"]["icao24"]
        except:
            d_aircraft_re,d_aircraft_ia,d_aircraft_ic,d_aircraft_ic24 = ["None","None","None","None"]
        df_dim_aircraft.loc[len(df_dim_aircraft.index)] = [f_id, d_aircraft_re, d_aircraft_ia, d_aircraft_ic, d_aircraft_ic24]


    df_fact.to_csv(f"csv-files/fact/fact_{date}.csv",index=False)
    df_dim_flight.to_csv(f"csv-files/dimension/dim_flight_{date}.csv",index=False)
    df_dim_airline.to_csv(f"csv-files/dimension/dim_airline_{date}.csv",index=False)
    df_dim_departure.to_csv(f"csv-files/dimension/dim_departure_{date}.csv",index=False)
    df_dim_arrival.to_csv(f"csv-files/dimension/dim_arrival_{date}.csv",index=False)
    df_dim_aircraft.to_csv(f"csv-files/dimension/dim_aircraft_{date}.csv",index=False)

    return api_response



retrive_hist_flights("2024-04-14", "dl", "iata")