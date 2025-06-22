import inquirer
import csv
import os
from colorama import Back, Fore, Style

def add_contacts():
    name : str = input("Enter name: ").strip().lower()
    phone : str = input("Enter phone number: ").strip().lower()
    
    with open("contacts.csv", "r") as file:
        reader = csv.DictReader(file)
        names = set(row["name"] for row in reader)
        if name in names:
            print("❌ This contact already exists!")
            return


    if os.path.exists("contacts.csv"):
        with open("contacts.csv", "a") as file:
            file.write(f"{name},{phone}\n")
            print(Fore.LIGHTGREEN_EX + "✅ Contact added successfully!" + Style.RESET_ALL)
    else:
        with open("contacts.csv", "w") as file:
            file.write("name,phone\n")
            file.write(f"{name},{phone}\n")
            print(Fore.LIGHTGREEN_EX + "✅ Contact added successfully!" + Style.RESET_ALL)


def view_contacts():
    if os.path.exists("contacts.csv"):
        with open("contacts.csv", "r") as file:
            print(Fore.LIGHTWHITE_EX + f"📖 Contacts List:" + Style.RESET_ALL)
            for line in file:
                name, phone = line.strip().split(",")
                print(Fore.LIGHTYELLOW_EX + f"Name: {name}, Phone: {phone}" + Style.RESET_ALL)
    else:
        print(Fore.LIGHTRED_EX + "❌ No contacts found!" + Style.RESET_ALL)


def main():
    while True:
        options = [inquirer.List('choice',
            message = "What would you like to do?",
            choices= ["Add Contact", "View Contacts", "Exit"])]
        
        answere = inquirer.prompt(options)['choice']

        if answere == "Add Contact":
            add_contacts()
        elif answere == "View Contacts":
            view_contacts()
        elif answere == "Exit":
            print(Fore.LIGHTBLUE_EX + "👋 Exiting the program. Goodbye!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()
