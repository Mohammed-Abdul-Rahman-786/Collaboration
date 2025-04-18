import mysql.connector
from db_connection import get_db_connection
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def add_crime():
    conn, cursor = get_db_connection()

    if conn is None or cursor is None:
        console.print("❌ [bold red]Database connection failed![/bold red]") 
        return

    crime_id = input("🆔 Enter Crime ID: ")
    category = input("📂 Enter Crime Category: ")
    location_type = input("📍 Enter Location Type: ")
    context = input("📋 Enter Context: ")
    persistent_id = input("🔁 Enter Persistent ID: ")
    location_subtype = input("🏠 Enter Location Subtype: ")
    month = input("📅 Enter Month (YYYY-MM-DD): ")
    latitude = float(input("🌐 Enter Latitude: "))
    longitude = float(input("🌐 Enter Longitude: "))
    street_id = int(input("🛣️ Enter Street ID: "))
    street_name = input("🚦 Enter Street Name: ")
    outcome_category = input("✅ Enter Outcome Category (Leave empty if none): ") or None
    outcome_date = input("📅 Enter Outcome Date (YYYY-MM-DD) (Leave empty if none): ") or None

    # Check if the location already exists in the locations table
    cursor.execute("""
        SELECT location_id FROM locations WHERE latitude = %s AND longitude = %s
    """, (latitude, longitude))
    location_record = cursor.fetchone()

    # If location does not exist, insert a new location
    if location_record is None:
        cursor.execute("""
            INSERT INTO locations (latitude, longitude)
            VALUES (%s, %s)
        """, (latitude, longitude))
        location_id = cursor.lastrowid  # Get the generated location_id
    else:
        location_id = location_record[0]  # Use the existing location_id

    # Insert into the outcomes table if an outcome is provided
    outcome_id = None
    if outcome_category and outcome_date:
        cursor.execute("""
            INSERT INTO outcomes (outcome_status, outcome_date)
            VALUES (%s, %s)
        """, (outcome_category, outcome_date))
        outcome_id = cursor.lastrowid  # Get the ID of the inserted outcome

    # Insert into crimes table
    sql = """
        INSERT INTO crimes (
            crime_id, category, location_type, context,
            persistent_id, location_subtype, month,
            location_id, outcome_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        crime_id, category, location_type, context,
        persistent_id, location_subtype, month,
        location_id, outcome_id
    )

    try:
        cursor.execute(sql, values)
        conn.commit()
        console.print(f"✅ [bold green]Crime record with ID {crime_id} added successfully![/bold green]")
    except mysql.connector.Error as err:
        console.print(f"❌ [bold red]Error inserting data:[/bold red] {err}")

    cursor.close()
    conn.close()


def view_crimes():
    conn, cursor = get_db_connection()

    if conn is None or cursor is None:
        console.print("❌ [bold red]Database connection failed![/bold red]")
        return

    cursor.execute("SELECT * FROM crimes")
    crimes = cursor.fetchall()

    if not crimes:
        console.print("[yellow]⚠️ No crime records found![/yellow]")
    else:
        columns = [desc[0] for desc in cursor.description]
        table = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE_HEAVY)

        for col in columns:
            table.add_column(col)

        for row in crimes:
            table.add_row(*[str(item) if item is not None else "N/A" for item in row])

        console.print(table)

    cursor.close()
    conn.close()


def update_crime():
    conn, cursor = get_db_connection()

    if conn is None or cursor is None:
        console.print("❌ [bold red]Database connection failed![/bold red]")
        return

    crime_id = input("🔁 Enter the Crime ID of the record you want to update: ")

    cursor.execute("SELECT * FROM crimes WHERE crime_id = %s", (crime_id,))
    record = cursor.fetchone()

    if not record:
        console.print("⚠️ [yellow]No record found with that Crime ID.[/yellow]")
        return

    column_names = [desc[0] for desc in cursor.description]

    table = Table(title="📋 Current Crime Record", show_header=True, header_style="bold cyan", box=box.MINIMAL_DOUBLE_HEAD)
    table.add_column("Field", style="bold")
    table.add_column("Value")

    for col, val in zip(column_names, record):
        table.add_row(col, str(val))

    console.print(table)

    print("\n✏️ Enter new values to update (leave blank to keep current):")

    update_fields = []
    values = []

    # Handle location_id separately
    new_location_id = None

    for i in range(1, len(column_names)):  # Skip crime_id (index 0)
        col = column_names[i]
        current_value = record[i]
        new_value = input(f"{col.replace('_', ' ').title()} [{current_value}]: ").strip()

        if new_value != "":
            if col == "location_id":  # Handle location_id separately
                new_location_id = int(new_value)
            elif col == "outcome_id" and new_value:
                new_value = int(new_value)  # Ensure outcome_id is updated
            update_fields.append(f"{col} = %s")
            values.append(new_value)

    # Ensure the new location_id exists in the locations table
    if new_location_id:
        cursor.execute("SELECT location_id FROM locations WHERE location_id = %s", (new_location_id,))
        location_exists = cursor.fetchone()

        if not location_exists:
            console.print(f"❌ [red]Location ID {new_location_id} does not exist. Please provide a valid location ID or add it first.[/red]")
            return

    if not update_fields:
        console.print("⚠️ [yellow]No fields to update.[/yellow]")
        return

    values.append(crime_id)
    sql = f"UPDATE crimes SET {', '.join(update_fields)} WHERE crime_id = %s"

    try:
        cursor.execute(sql, values)
        conn.commit()
        if cursor.rowcount > 0:
            console.print("✅ [green]Crime record updated successfully.[/green]")
        else:
            console.print("⚠️ [yellow]No changes were made.[/yellow]")
    except mysql.connector.Error as err:
        console.print(f"❌ [red]Error updating data:[/red] {err}")

    cursor.close()
    conn.close()



def delete_crime():
    conn, cursor = get_db_connection()

    if conn is None or cursor is None:
        console.print("❌ [bold red]Database connection failed![/bold red]")
        return

    crime_id = input("🗑️ Enter the Crime ID of the record to delete: ")

    try:
        # Check if there's an outcome_id in the crimes table
        cursor.execute("SELECT outcome_id FROM crimes WHERE crime_id = %s", (crime_id,))
        outcome_id = cursor.fetchone()

        if outcome_id and outcome_id[0] is not None:
            # Set the outcome_id to NULL in the crimes table before deleting the outcome
            cursor.execute("UPDATE crimes SET outcome_id = NULL WHERE outcome_id = %s", (outcome_id[0],))

            # Now delete the outcome from the outcomes table
            cursor.execute("DELETE FROM outcomes WHERE outcome_id = %s", (outcome_id[0],))

        # Delete the crime record (this will automatically delete the corresponding location due to cascading delete)
        cursor.execute("DELETE FROM crimes WHERE crime_id = %s", (crime_id,))
        conn.commit()

        if cursor.rowcount > 0:
            console.print("🧹 [green]Crime record deleted successfully, along with the corresponding location.[/green]")
        else:
            console.print("⚠️ [yellow]No record found with that Crime ID.[/yellow]")

    except mysql.connector.Error as err:
        console.print(f"❌ [red]Error deleting record:[/red] {err}")

    cursor.close()
    conn.close()
