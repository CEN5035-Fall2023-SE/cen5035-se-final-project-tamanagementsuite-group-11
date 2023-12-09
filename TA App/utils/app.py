import pyodbc
import json

def load_db_config(filename):
    with open(filename, 'r') as config_file:
        return json.load(config_file)

def establish_db_connection(config):
    try:
        conn = pyodbc.connect(
            f"Driver={{{config['Driver']}}};"
            f"Server={config['ServerName']};"
            f"Database={config['DatabaseName']};"
            f"UID={config['UserID']};"
            f"PWD={config['Password']};"
            f"Encrypt={config['Encrypt']};"
            f"TrustServerCertificate={config['TrustServerCertificate']};"
            f"ConnectionTimeout={config['ConnectionTimeout']};"
        )
        return conn
    except Exception as e:
        print("Error connecting to the database:", str(e))
        return None

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print("Error executing query:", str(e))
        return []

def main():
    config = load_db_config('db_config.json')
    connection = establish_db_connection(config)

    if connection:
        try:
            # Example: Select data from a table
            query = "SELECT * FROM TA_Applicants"
            results = execute_query(connection, query)
            
            # Print the results
            for row in results:
                print(row)

            # Example: Insert data into a table
            # query = "INSERT INTO TA_Applicants (studentid, semester) VALUES (?, ?)"
            # data = ('value1', 'value2')
            # execute_query(connection, query, data)
            # connection.commit()
        finally:
            connection.close()

if __name__ == "__main__":
    main()
