import mysql.connector

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="crime_records_analysis_system"
        )
        return conn, conn.cursor()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None, None
