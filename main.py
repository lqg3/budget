import matplotlib.pyplot as plt
import pandas as pd
import etc # miscelanious functions, grouped into one file
import datetime
import os
import shutil
from time import sleep
import validator_collection as validate


def main():
    print(etc.render_text('+------+\n  |   Budget  |\n+------+', font='chunky'))
    print("Welcome!")
    print(datetime.date.today(), f"{datetime.datetime.today().hour}:{datetime.datetime.today().minute}:{datetime.datetime.today().second}")
    
    profile = select_profile()
    if profile == None:
        profiles()

    

def select_profile():
    print("\nProfiles:")
    print_user_profiles() # prints user profile
    print("Type 'CREATE' to create a new profile.")

    while True:
        sel: str = input("Select profile: ")
        if sel.upper() == 'CREATE':
            return profiles(1) # create a new profile
        
        elif os.path.exists(f"user_profiles/{sel}"):
            break

        else:
            sel: str = input("Profile not found. Create profile? (Y/N): ").lower()
            if sel == 'y': # create a profile if no profile is found.
                return None
            else:
                pass  
    return sel
    
def profiles(create: int=0):
    if create == 1: # ONLY create a profile when profile create mode on (usually on first start)
        while True:
            try:
                profile_name: str = input("New profile name: ")
                if not profile_name.isalnum():
                    raise ValueError
                os.mkdir(f"user_profiles/{profile_name}")
                print(f'New profile "{profile_name}" made.')
                sleep(.3)
                return profile_name
            except ValueError:
                print("Profile name must be alphanumeric!")

    print(etc.render_text('+------+\n  | Profiles|\n+------+', font='chunky'))
    profiles = os.listdir('user_profiles')
    print("User profiles: ")
    print_user_profiles()
    while True:
        user_input: str = input("\n1. Create new profile\n2. Change profile name\n3. Delete profile\n4. Return to menu\nSelection: ")
        match(user_input):
            case "1": # case: create new profile
                while True:
                    try:
                        profile_name: str = input("New profile name: ")
                        if not profile_name.isalnum():
                            raise ValueError
                        os.mkdir(f"user_profiles/{profile_name}")
                        print(f'New profile "{profile_name}" made.')
                        sleep(.3)
                        break
                    except ValueError:
                        print("Profile name must be alphanumeric!")
                    
            case "2": # case: change profile name
                print_user_profiles()
                old_name = input("Profile to rename: ")
                if old_name in profiles:
                    while True:
                        try:
                            new_name: str = input("New profile name: ")
                            if not new_name.isalnum():
                                raise ValueError
                            os.rename(f"user_profiles/{old_name}",f"user_profiles/{new_name}")
                            print(f"Profile {old_name} renamed to {new_name}")
                            sleep(.3)
                            break
                        except ValueError:
                            print("Profile name must be alphanumeric!")
                

            case "3": # case: delete profile
                print_user_profiles()
                profile_to_delete: str = input("Select the profile you would like to delete:  ")
                if profile_to_delete in profiles:
                    sel = input(f"You are about to delete '{profile_to_delete}'. Continue? (Y/N): ").lower()
                    if sel == 'y':
                        print("Deleting profile...")
                        sleep(1)
                        shutil.rmtree(f'user_profiles/{profile_to_delete}')
                        print("Profile has been successfully deleted.")
                        sleep(.3)
                    else:
                        print("[i] Profile not found.")
                        break
            case "4":
                return None
            case _:
                print("Please type a valid input.")

def show_data(profile_name, year, month): # shows the user profile data
    df = pd.read_csv(f"user_profiles/{profile_name}/budget_{year}/{month}.csv")
    plt.figure(figsize=(12, 6))
    plt.bar(df['purchase_date'], df['item_price'], color='skyblue')
    plt.xlabel('Purchase Date')
    plt.ylabel('Daily Spend')
    plt.title('Spending Trends')
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()
    plt.show()

def print_user_profiles():
    for profile_name in os.listdir('user_profiles'):
        print(f"►", profile_name)

if __name__ == '__main__':
    etc.exit_confirmation(main) # try & except statements for KeyboardInterrupt (see etc.py) 
