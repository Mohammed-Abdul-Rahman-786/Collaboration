import os
import sys
from fetch_data import fetch_crime_data
from insert_data import insert_data_from_json
from crud import add_crime, view_crimes, update_crime, delete_crime
from analyze import analyze_data
from visualize import visualize_data

from colorama import init, Fore, Style
from tabulate import tabulate

# Initialize colorama
init(autoreset=True)

def print_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.YELLOW + Style.BRIGHT + "🕵️‍♂️🔍 WELCOME TO CRIME DATA ANALYSIS SYSTEM 🔍🕵️‍♀️\n")

def main_menu():
    while True:
        print_header()

        menu_items = [
            ["1", "📡 Fetch Crime Data"],
            ["2", "📂 Insert Data from JSON"],
            ["3", "➕ Add a New Crime"],
            ["4", "📋 View All Crimes"],
            ["5", "✏️ Update a Crime Record"],
            ["6", "🗑️ Delete a Crime Record"],
            ["7", "📊 Analyze Crime Data"],
            ["8", "📈 Visualize Crime Data"],
            ["9", "🚪 Exit"]
        ]

        print(tabulate(menu_items, headers=[Fore.CYAN + "Option", Fore.CYAN + "Action"], tablefmt="fancy_grid"))

        try:
            choice = int(input(Fore.GREEN + "\n👉 Enter your choice (1-9): " + Style.RESET_ALL))
            
            if choice == 1:
                fetch_crime_data()
            elif choice == 2:
                insert_data_from_json()
            elif choice == 3:
                add_crime()
            elif choice == 4:
                view_crimes()
            elif choice == 5:
                update_crime()
            elif choice == 6:
                delete_crime()
            elif choice == 7:
                analyze_data()
            elif choice == 8:
                visualize_data()
            elif choice == 9:
                print(Fore.MAGENTA + "👋 Exiting the system. Goodbye!")
                sys.exit(0)
            else:
                print(Fore.RED + "❌ Invalid choice, please try again.")
            
            input(Fore.CYAN + "\n🔁 Press Enter to return to the menu...")

        except ValueError:
            print(Fore.RED + "❌ Please enter a valid number.")
            input(Fore.CYAN + "\n🔁 Press Enter to try again...")

if __name__ == "__main__":
    main_menu()
