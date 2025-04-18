import json
import os
from db_connection import get_db_connection
from colorama import init, Fore, Style
from tabulate import tabulate

# 🎨 Initialize colorama
init(autoreset=True)

def insert_data_from_json():
    conn, cursor = get_db_connection()

    if conn is None or cursor is None:
        print(Fore.RED + "❌ Database connection failed!")
        return

    json_file_path = os.path.join("data", "fetched_crimes.json")
    
    if not os.path.exists(json_file_path):
        print(Fore.RED + f"❌ File '{json_file_path}' not found!")
        return

    with open(json_file_path, "r") as file:
        data = json.load(file)

    print(Fore.CYAN + "📥 Inserting crime data into the database...\n")
    
    inserted_rows = []

    for index, item in enumerate(data):
        try:
            # Extract crime information
            category = item.get("category")
            location_type = item.get("location_type")
            context = item.get("context")
            persistent_id = item.get("persistent_id")
            crime_id = item.get("id")
            location_subtype = item.get("location_subtype")
            month = item.get("month")
            month_date = f"{month}-01" if month else None

            # Extract location info
            location = item.get("location") or {}
            latitude = location.get("latitude")
            longitude = location.get("longitude")

            # Extract street info
            street = location.get("street") or {}
            street_id = street.get("id")
            street_name = street.get("name")

            # Extract outcome status safely
            outcome_status_data = item.get("outcome_status")
            if outcome_status_data:
                outcome_status = outcome_status_data.get("category")
                outcome_date = outcome_status_data.get("date")
                if outcome_date and len(outcome_date) == 7:
                    outcome_date = f"{outcome_date}-01"
                elif outcome_date and len(outcome_date) != 10:
                    outcome_date = None
            else:
                outcome_status = None
                outcome_date = None

            # Insert into streets table (ignore if already exists)
            cursor.execute("""
                INSERT IGNORE INTO streets (street_id, street_name) 
                VALUES (%s, %s)
            """, (street_id, street_name))

            # Insert into locations table
            cursor.execute("""
                INSERT INTO locations (latitude, longitude, street_id) 
                VALUES (%s, %s, %s)
            """, (latitude, longitude, street_id))
            location_id = cursor.lastrowid

            # Insert into outcomes table (check if exists first)
            if outcome_status and outcome_date:
                cursor.execute("""
                    SELECT outcome_id FROM outcomes 
                    WHERE outcome_status = %s AND outcome_date = %s
                """, (outcome_status, outcome_date))
                existing_outcome = cursor.fetchone()

                if existing_outcome:
                    outcome_id = existing_outcome[0]
                else:
                    cursor.execute("""
                        INSERT INTO outcomes (outcome_status, outcome_date) 
                        VALUES (%s, %s)
                    """, (outcome_status, outcome_date))
                    outcome_id = cursor.lastrowid
            else:
                outcome_id = None

            # Insert into crimes table
            cursor.execute("""
                INSERT INTO crimes (
                    crime_id, category, location_type, context, persistent_id, 
                    location_subtype, month, location_id, outcome_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                crime_id,
                category,
                location_type,
                context,
                persistent_id,
                location_subtype,
                month_date,
                location_id,
                outcome_id
            ))

            # Append first few rows for preview
            if index < 5:
                inserted_rows.append([
                    crime_id, category, street_name, outcome_status, month
                ])

        except Exception as e:
            print(Fore.YELLOW + f"⚠️ Error inserting row {index}: {e}")

    conn.commit()
    cursor.close()
    conn.close()

    print(Fore.GREEN + "\n✅ JSON data inserted successfully into the database.\n")

    if inserted_rows:
        print(Fore.MAGENTA + "📊 Preview of Inserted Records:")
        print(tabulate(
            inserted_rows,
            headers=["Crime ID", "Category", "Street", "Outcome", "Month"],
            tablefmt="fancy_grid",
            showindex=True
        ))
