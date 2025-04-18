import pandas as pd
import numpy as np
from db_connection import get_db_connection
from colorama import init, Fore, Style
from tabulate import tabulate

# Initialize Colorama
init(autoreset=True)

def analyze_data():
    conn, cursor = get_db_connection()

    if conn is None or cursor is None:
        print(Fore.RED + "❌ Database connection failed!")
        return

    # Load all crime data into DataFrame
    cursor.execute("SELECT * FROM crimes")
    rows = cursor.fetchall()
    if not rows:
        print(Fore.RED + "❌ No data available for analysis.")
        return

    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)

    while True:
        print(Fore.YELLOW + Style.BRIGHT + """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊  CRIME DATA ANALYSIS MENU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1️⃣  Show basic crime data overview
2️⃣  Show top 5 crime categories
3️⃣  Show number of crimes reported each month
4️⃣  Show crime outcome category distribution
5️⃣  Show all analysis together
0️⃣  Return to main menu
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """)

        choice = input(Fore.CYAN + "👉 Enter your choice: ").strip()

        if choice == '1':
            print(Fore.GREEN + "\n📊 Basic Crime Data Overview:\n")
            print(tabulate(df.describe(include='all'), headers='keys', tablefmt='fancy_grid', showindex=True))

        elif choice == '2':
            top_categories = df['category'].value_counts().head(5)
            print(Fore.BLUE + "\n📑 Top 5 Crime Categories:\n")
            print(tabulate(top_categories.reset_index().rename(columns={"index": "Category", "category": "Count"}), headers='keys', tablefmt='fancy_grid', showindex=False))

        elif choice == '3':
            monthly_crimes = df['month'].value_counts().sort_index()
            print(Fore.MAGENTA + "\n📅 Number of Crimes Reported Each Month:\n")
            print(tabulate(monthly_crimes.reset_index().rename(columns={"index": "Month", "month": "Crimes"}), headers='keys', tablefmt='fancy_grid', showindex=False))

        elif choice == '4':
            print(Fore.RED + "❌ No analysis for crime outcome categories. Data unavailable in 'crimes' table.")

        elif choice == '5':
            print(Fore.GREEN + "\n📊 Basic Crime Data Overview:\n")
            print(tabulate(df.describe(include='all'), headers='keys', tablefmt='fancy_grid', showindex=True))

            top_categories = df['category'].value_counts().head(5)
            print(Fore.BLUE + "\n📑 Top 5 Crime Categories:\n")
            print(tabulate(top_categories.reset_index().rename(columns={"index": "Category", "category": "Count"}), headers='keys', tablefmt='fancy_grid', showindex=False))

            monthly_crimes = df['month'].value_counts().sort_index()
            print(Fore.MAGENTA + "\n📅 Number of Crimes Reported Each Month:\n")
            print(tabulate(monthly_crimes.reset_index().rename(columns={"index": "Month", "month": "Crimes"}), headers='keys', tablefmt='fancy_grid', showindex=False))

        elif choice == '0':
            print(Fore.LIGHTGREEN_EX + "👋 Returning to main menu...\n")
            break

        else:
            print(Fore.RED + "❌ Invalid choice. Please try again.")

    cursor.close()
    conn.close()
