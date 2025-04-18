import requests
import pandas as pd
import os
import json
from colorama import init, Fore, Style
from tabulate import tabulate

# 🎨 Initialize colorama
init(autoreset=True)

# 🌍 Default API parameters
API_URL = "https://data.police.uk/api/crimes-street/all-crime"
LATITUDE = "52.629729"
LONGITUDE = "-1.131592"
DATE = "2023-12"

def fetch_crime_data():
    print(Fore.CYAN + "📡 Fetching crime data from API...\n")

    # ✅ Ensure data folder exists
    os.makedirs("data", exist_ok=True)

    params = {
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "date": DATE
    }

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        print(Fore.GREEN + "✅ Data fetched successfully!\n")
        data = response.json()

        # 💾 Save raw JSON
        with open("data/fetched_crimes.json", "w") as f:
            json.dump(data, f, indent=2)
        print(Fore.YELLOW + "📝 JSON saved to 'data/fetched_crimes.json'")

        df = pd.json_normalize(data)
        df.to_csv("data/fetched_crimes.csv", index=False)
        print(Fore.YELLOW + f"📁 CSV saved to 'data/fetched_crimes.csv'. Total records: {len(df)}\n")

        # 📊 Preview the top 10 records
        if not df.empty:
            print(Fore.MAGENTA + "📋 Top 10 Records:\n")
            preview_cols = ['category', 'location.street.name', 'outcome_status.category', 'month']
            preview_df = df[preview_cols].fillna("N/A").head(10)
            print(tabulate(preview_df, headers="keys", tablefmt="fancy_grid", showindex=True))
        else:
            print(Fore.RED + "⚠️ No data available to display.\n")

        return df
    else:
        print(Fore.RED + "❌ Failed to fetch data from API.")
        print(Fore.RED + f"📡 Status Code: {response.status_code}")
        return None
