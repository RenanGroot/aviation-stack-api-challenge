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
# Give it a range date (calculation)
# Checks if the file already exists

def retrieve_hist_flights(date:str, airline:str, option:str) -> str:
    """
    This function retrieves the data from historical flights of a specific date

    Args:
        date(str): Flight date
        airline(str): Airline name, IATA code or ICAO code. According to the option explicited on the args.
        option(str): "name", "iata" or "icao". Option for the airline filter.
    Returns:
        csv_path (str): Csv file path.
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
        print("Server connection failed")
    
    if api_result.status_code == 401:
        return print("ERROR 401 - Unauthorized. Please check you API KEY.")

    api_response = api_result.json()

    # Table definitions:
    df_fact = pd.DataFrame(columns=["id","flight_date","flight_status","flight_number","flight_iata","flight_icao","airline_name","airline_iata","airline_icao","depart_airport", "depart_timezone", "depart_iata", "depart_icao", "depart_terminal", "depart_gate", "depart_delay", "depart_scheduled", "depart_estimated", "depart_actual", "depart_estimated_runway", "depart_actual_runway","arrival_airport", "arrival_timezone", "arrival_iata", "arrival_icao", "arrival_terminal", "arrival_gate", "arrival_baggage", "arrival_delay", "arrival_scheduled", "arrival_estimated", "arrival_actual", "arrival_estimated_runway", "arrival_actual_runway","aircraft_registration", "aircraft_iata", "aircraft_icao", "aircraft_icao24"])
    
    for row in api_response["data"]:

        # Condition due some data are missing aircraft information
        if row["aircraft"] == None:
            f_id = (row["flight_date"]) + (row["flight"]["iata"]) + "None"
        else:
            f_id = (row["flight_date"]) + (row["flight"]["iata"]) + (row["aircraft"]["iata"])

        # FACT TABLE POPULATE
        f_date = row["flight_date"]
        f_status = row["flight_status"]

        # FLIGHT DATA
        d_flight_nu = row["flight"]["number"]
        d_flight_ia = row["flight"]["iata"]
        d_flight_ic = row["flight"]["icao"]

        # AIRLNE DATA
        d_airline_na = row["airline"]["name"]
        d_airline_ia = row["airline"]["iata"]
        d_airline_ic = row["airline"]["icao"]

        # DEPARTURE DATA
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
    
        # ARRIVAL DATA
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


        #AIRCRAFT DATA
        try:
            d_aircraft_re = row["aircraft"]["registration"]
            d_aircraft_ia = row["aircraft"]["iata"]
            d_aircraft_ic = row["aircraft"]["icao"]
            d_aircraft_ic24 = row["aircraft"]["icao24"]
        except:
            d_aircraft_re,d_aircraft_ia,d_aircraft_ic,d_aircraft_ic24 = ["None","None","None","None"]

        df_fact.loc[len(df_fact.index)] = [f_id, f_date, f_status, d_flight_nu, d_flight_ia, d_flight_ic,d_airline_na, d_airline_ia, d_airline_ic,d_departure_ai, d_departure_ti, d_departure_ia, d_departure_ic, d_departure_te, d_departure_ga, d_departure_de, d_departure_sc, d_departure_es, d_departure_ac, d_departure_esrun, d_departure_acrun,d_arrival_ai, d_arrival_ti, d_arrival_ia, d_arrival_ic, d_arrival_te, d_arrival_ga, d_arrival_ba, d_arrival_de, d_arrival_sc, d_arrival_es, d_arrival_ac, d_arrival_esrun, d_arrival_acrun,d_aircraft_re, d_aircraft_ia, d_aircraft_ic, d_aircraft_ic24]

    csv_path = f"csv-files/{date}_{airline}.csv"

    df_fact.to_csv(csv_path,index=False)

    print(f"Successfully downloaded file for {airline} at {date}")

    return csv_path
