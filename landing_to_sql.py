import sqlite3
import subprocess

def upload_csv(csv_path:str) -> None:
    """
    This function creates the database (if not exists), and populate it with a csv file retieved from the API.

    Args:
        csv_path (str): Csv file path. Ex: "csv-files/2024-04-15_dl.csv"
  
    """
    connection = sqlite3.connect("database/test.db")
    
    cursor = connection.cursor()

    # Creating Table, if not exists
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS example (
        id TEXT PRIMARY KEY,
        flight_date TEXT,
        flight_status TEXT,
        flight_number TEXT,
        flight_iata TEXT,
        flight_icao TEXT,
        airline_name TEXT,
        airline_iata TEXT,
        airline_icao TEXT,
        depart_airport TEXT,
         depart_timezone TEXT,
         depart_iata TEXT,
         depart_icao TEXT,
         depart_terminal TEXT,
         depart_gate TEXT,
         depart_delay TEXT,
         depart_scheduled TEXT,
         depart_estimated TEXT,
         depart_actual TEXT,
         depart_estimated_runway TEXT,
         depart_actual_runway TEXT,
        arrival_airport TEXT,
         arrival_timezone TEXT,
         arrival_iata TEXT,
         arrival_icao TEXT,
         arrival_terminal TEXT,
         arrival_gate TEXT,
         arrival_baggage TEXT,
         arrival_delay TEXT,
         arrival_scheduled TEXT,
         arrival_estimated TEXT,
         arrival_actual TEXT,
         arrival_estimated_runway TEXT,
         arrival_actual_runway TEXT,
        aircraft_registration TEXT,
         aircraft_iata TEXT,
         aircraft_icao TEXT,
         aircraft_icao24 );
    """
    )

    # Run subprocess for populating the DB with the csv file
    subprocess.run(['sqlite3',
                         str("database/test.db"),
                         '-cmd',
                         '.mode csv',
                         '.import --skip 1 ' + csv_path
                                 +' example'],
                        capture_output=True)
    connection.commit()

    print(f"Successfully populated db with file from : {csv_path}")
