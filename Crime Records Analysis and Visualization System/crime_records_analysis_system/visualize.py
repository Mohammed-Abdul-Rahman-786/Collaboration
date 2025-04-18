import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from colorama import init, Fore, Style
from tabulate import tabulate

init(autoreset=True)

def visualize_data():
    try:
        # Make sure the path to your CSV file is correct
        crime_data = pd.read_csv("data/fetched_crimes.csv")
        
        if crime_data.empty:
            print(Fore.RED + "❌ No data available for visualization.")
            return

        # Column checks (verify column names based on the CSV file)
        has_month = 'month' in crime_data.columns
        has_outcome = 'outcome_category' in crime_data.columns

        while True:
            print(Fore.YELLOW + "\n📊✨ Visualization Menu ✨📊\n")
            menu = [
                ["1", "🔝 Top 10 Crime Categories"],
                ["2", "📆 Monthly Crime Trend"],
                ["0", "🔙 Return to Main Menu"]
            ]
            print(tabulate(menu, headers=[Fore.CYAN + "Option", Fore.CYAN + "Description"], tablefmt="fancy_grid"))

            choice = input(Fore.GREEN + "\n👉 Select an option (0-2): ").strip()

            if choice in ['1', '2']:
                print(Fore.MAGENTA + "\n🎨 Choose Chart Type:\n")
                chart_menu = [
                    ["1", "📊 Bar Chart (Crime by Category)"],
                    ["2", "📈 Line Chart (Crimes per Month)"],
                    ["3", "🏠 Go Back to Visualization Menu"]
                ]
                print(tabulate(chart_menu, headers=[Fore.CYAN + "Option", Fore.CYAN + "Chart Type"], tablefmt="fancy_grid"))

                chart_choice = input(Fore.GREEN + "\n👉 Select chart type (1-3): ").strip()

                if chart_choice == '1':
                    plt.figure(figsize=(10, 6))
                    sns.countplot(data=crime_data, y='category',
                                  order=crime_data['category'].value_counts().index[:10],
                                  palette='Blues_r')
                    plt.title("🔝 Top 10 Crime Categories")
                    plt.xlabel("Number of Crimes")
                    plt.ylabel("Category")
                    plt.tight_layout()
                    plt.show()

                elif chart_choice == '2':
                    if has_month:
                        monthly = crime_data['month'].value_counts().sort_index()
                        plt.figure(figsize=(10, 6))
                        monthly.plot(kind='line', marker='o', color='orange')
                        plt.title("📈 Monthly Crime Trends")
                        plt.xlabel("Month")
                        plt.ylabel("Crime Count")
                        plt.xticks(rotation=45)
                        plt.tight_layout()
                        plt.show()
                    else:
                        print(Fore.RED + "⚠️ Cannot display line chart — 'month' column missing.")

                elif chart_choice == '3':
                    print(Fore.BLUE + "🔙 Returning to Visualization Menu...")
                    continue
                else:
                    print(Fore.RED + "⚠️ Invalid input. Please select a valid option (1-3).")

            elif choice == '0':
                print(Fore.BLUE + "🔙 Back to Main Menu...")
                break

            else:
                print(Fore.RED + "⚠️ Invalid input. Please choose a valid option (0-2).")

    except FileNotFoundError:
        print(Fore.RED + "❌ The data file 'fetched_crimes.csv' does not exist!")
    except Exception as e:
        print(Fore.RED + f"❌ An error occurred while visualizing the data: {e}")
