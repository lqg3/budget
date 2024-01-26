import matplotlib.pyplot as plt
import pandas as pd
import etc  # miscelanious functions, grouped into one file
import datetime
import os
import shutil
from time import sleep
import tabulate
from calendar import monthrange

profile = None


# Greets the user ONLY on program bootup
def greet():
    print(etc.render_text("+------+\n  |   Budget  |\n+------+", font="chunky"))
    print("Welcome!")
    print(
        datetime.date.today(),
        f"{datetime.datetime.today().hour}:{datetime.datetime.today().minute}:{datetime.datetime.today().second}",
    )


def main():
    global profile
    if (
        profile == None
    ):  # if user hasn't selected profile yet, this conditional will select a profile.
        profile = select_profile()

    while True:
        d = main_menu(profile)
        if d == "CHANGE_PROFILE":
            profile = select_profile(mode="CHANGE")
        elif d == "CREATE":
            while True:
                try:
                    profile = profiles(1)
                except FileExistsError: 
                    print("Profile name already exists. Please choose another profile name.")

def main_menu(profile):
    if (
        profile == None
    ):  # if user hasn't selected profile yet, this conditional will select a profile.
        return "CREATE"
    sel = input(
        "1. Add purchase\n2. View data\n3. Change profile\n4. Calculate something\n5. Exit\nSelection: "
    )
    match (sel):
        case "1":
            print(etc.render_text("+------+\nAdd Purchase\n+------+", font="chunky"))
            add_purchase(profile)
        case "2":
            while True:
                try:
                    year = int(input("Year      : "))
                    month = int(input("Month     : "))
                    sel: int = int(
                        input("\n1. Table format\n2. Bar graph\nSelection: ")
                    )
                    if sel == 1:
                        print(show_data(profile, year, month, mode="table"))
                    elif sel == 2:
                        show_data(profile, year, month, mode="bar")
                    else:
                        print("Please select 1 or 2.")
                    break
                except ValueError:
                    print("Please input an integer. For month, please use 1 - 12.")
                except FileNotFoundError:
                    print("Data not found.")

        case "3":
            return "CHANGE_PROFILE"
        case "4":
            while True:
                try:
                    sel: int = int(input("1. Subtract\n2.Subtraction\n3.Multipllication\n4.Division\n5. Exit"))
                    x:float = float(input("First number: "))
                    y:float = float(input("Second number: "))

                    match(sel):
                        case 1:
                            Calculator.add(x, y)
                        case 2:
                            Calculator.subtract(x, y)
                        case 3:
                            Calculator.multiply(x, y)
                        case 4:
                            Calculator.divide(x, y)
                        case 5:
                            break
                        case _:
                            print("Invalid operation!")

                except ValueError:
                    print("Must be a number!")
        case "5":
            exit()
        case _:
            print("Please select a valid option.")


def add_purchase(profile_name: str): 
    """
    Adds item purchase to the CSV file.
    """
    item_name: str = input("Item name: ")
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    while True:
        try:
            price: float = float(input("Price: "))
            break
        except ValueError:
            print("Price must be an integer or a floating point number!")

    i = 0
    try:
        with open(
            f"user_profiles/{profile_name}/budget_{year}/{month}.csv", "r"
        ) as file:
            for _ in file:
                i += 1  # i is the number of item.

    except FileNotFoundError:  # create the file
        if not os.path.exists(f"user_profiles/{profile_name}/budget_{year}"):
            os.mkdir(f"user_profiles/{profile_name}/budget_{year}")
            sleep(1)
            print("Adding...")
        with open(
            f"user_profiles/{profile_name}/budget_{year}/{month}.csv", "w"
        ) as file:
            file.write("no,item_name,item_price,purchase_date\n")
            i = 1

            sleep(1)

    with open(
        f"user_profiles/{profile_name}/budget_{year}/{month}.csv", "a", newline=""
    ) as file:
        file.write(f"{i},{item_name},{price},{str(datetime.date.today())}\n")
        sleep(1)
        print("Purchase added.")
        sleep(1)


def select_profile(mode: str = "NORMAL"):
    if mode == "NORMAL":
        global profile
        if profile != None:
            return profile

    print("\nProfiles:")
    print_user_profiles()  # prints user profile
    print("Type 'CREATE' to create a new profile.")

    while True:
        sel: str = input("Select profile: ")
        if sel.upper() == "CREATE":
            return profiles()  # create a new profile

        elif os.path.exists(f"user_profiles/{sel}"):
            break

        else:
            sel: str = input("Profile not found. Create profile? (Y/N): ").lower()
            if sel == "y":  # create a profile if no profile is found.
                return None  # goes back to main()
            else:
                pass
    return sel

def profiles(create: int = 0):
    """
    Function to create profile, with 'create' optional argument, used specifically on the first bootup.
    """
    if (
        create == 1
    ):  # ONLY create a profile when profile create mode on (usually on first start)
        while True:
            try:
                profile_name: str = input("New profile name: ")
                if not profile_name.isalnum():
                    raise ValueError
                os.mkdir(f"user_profiles/{profile_name}")
                print(f'New profile "{profile_name}" made.')
                sleep(0.3)
                return profile_name
            except ValueError:
                print("Profile name must be alphanumeric!")

    print(etc.render_text("+------+\n  | Profiles|\n+------+", font="chunky"))
    profiles = os.listdir("user_profiles")
    print("User profiles: ")
    print_user_profiles()
    while True:
        user_input: str = input(
            "\n1. Create new profile\n2. Change profile name\n3. Delete profile\n4. Return to menu\nSelection: "
        )
        match (user_input):
            case "1":  # case: create new profile
                while True:
                    try:
                        profile_name: str = input("New profile name: ")
                        if not profile_name.isalnum():
                            raise ValueError
                        os.mkdir(f"user_profiles/{profile_name}")
                        print(f'New profile "{profile_name}" made.')
                        sleep(0.3)
                        break
                    except ValueError:
                        print("Profile name must be alphanumeric!")

            case "2":  # case: change profile name
                print_user_profiles()
                old_name = input("Profile to rename: ")
                if old_name in profiles:
                    while True:
                        try:
                            new_name: str = input("New profile name: ")
                            if not new_name.isalnum():
                                raise ValueError
                            os.rename(
                                f"user_profiles/{old_name}", f"user_profiles/{new_name}"
                            )
                            print(f"Profile {old_name} renamed to {new_name}")
                            sleep(0.3)
                            break
                        except ValueError:
                            print("Profile name must be alphanumeric!")

            case "3":  # case: delete profile
                print_user_profiles()
                profile_to_delete: str = input(
                    "Select the profile you would like to delete:  "
                )
                if profile_to_delete in profiles:
                    sel = input(
                        f"You are about to delete '{profile_to_delete}'. Continue? (Y/N): "
                    ).lower()
                    if sel == "y":
                        print("Deleting profile...")
                        sleep(1)
                        shutil.rmtree(f"user_profiles/{profile_to_delete}")
                        print("Profile has been successfully deleted.")
                        sleep(0.3)
                    else:
                        print("[i] Profile not found.")
                        break
            case "4":
                return None
            case _:
                print("Please type a valid input.")

def show_data(
    profile_name: str, year: int, month: int, mode: str = "table"
):  # shows the user profile data
    df = pd.read_csv(f"user_profiles/{profile_name}/budget_{year}/{month}.csv")
    if mode == "table":
        return tabulate.tabulate(
            df,
            headers=["Number", "Item Name", "Item Price", "Purchase Date"],
            tablefmt="0pretty",
            showindex=False,
        )
    else:
        plt.figure(figsize=(15, 6))
        plt.bar(df["purchase_date"], df["item_price"], color="skyblue")
        plt.xlabel("Purchase Date")
        plt.ylabel("Daily Spend")
        plt.title("Spending Trends")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()
    monthly_sum, average = daily_average(profile_name, year, month)
    print(f"Spent on this month: {monthly_sum:,.2f}")
    print(f"Daily average: {average:,.2f}")

def print_user_profiles():
    for profile_name in os.listdir("user_profiles"):
        print(f"►", profile_name)

def sum_monthly(profile_name: str, year: int, month: int):
    df = pd.read_csv(f"user_profiles/{profile_name}/budget_{year}/{month}.csv")
    total = 0
    for price in df["item_price"]:
        total += price

    return total

def daily_average(profile_name: str, year: int, month: int):
    days = float(monthrange(year, month)[1])
    total = float(sum_monthly(profile_name, year, month))

    return total, (total / days)

class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"

if __name__ == "__main__":
    greet()
    etc.exit_confirmation(
        main
    )  # try & except statements for KeyboardInterrupt (see etc.py)