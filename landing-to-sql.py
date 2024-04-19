import sqlite3

def create_db():

    connection = sqlite3.connect("database/test.db")
    
    cursor = connection.cursor()

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
    connection.commit()

create_db()