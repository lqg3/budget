# Budget
### Video Demo: [https://youtu.be/DNoCb7E8RLM](https://youtu.be/DNoCb7E8RLM)

## Definition
This project is an application to help users to track their finances monthly, with features like tabulate and matplotlib's bar graph.

### Project Structure
1. project.py
2. test_project.py
3. etc.py
4. README.md
5. requirements.txt

_____

## Libraries
- **Matplotlib** - A Python library to visualize data, used to visualize monthly spending in this project specifically.
- **Tabulate** - A library to turn visualize data into a table in the command line interface.
- **Pandas** - A Python library to manipulate, add, and control data in Python efficiently.
- **Datetime** - A library to get the date for recordkeeping.
- **Calendar** - (only `monthrange` used) used to calculate average daily spending on a specific month.
- **OS & Shutil** - To control file writing and removal in the system itself.

## How to install library
To install library, you can simply run the `pip` command from the command line center. 

`pip install -r requirements.txt`

This will install all the required libraries (if not installed yet).

_____

<details>
<summary><code>python project.py</code></summary>
<br>
```shell
   __                                               __   
 _|  |_ ______ ______ ______ ______ ______ ______ _|  |_ 
|_    _|______|______|______|______|______|______|_    _|
  |__|                                             |__|  
   __     ______           __               __      __ 
  |  |   |   __ \.--.--.--|  |.-----.-----.|  |_   |  |
  |  |   |   __ <|  |  |  _  ||  _  |  -__||   _|  |  |
  |  |   |______/|_____|_____||___  |_____||____|  |  |
  |__|                        |_____|              |__|
   __                                               __
 _|  |_ ______ ______ ______ ______ ______ ______ _|  |_
|_    _|______|______|______|______|______|______|_    _|
  |__|                                             |__|

Welcome!
2024-01-27 6:51:13

Profiles:
► bills
► johnson
► PROFILE
► profile1
► profile29
Type 'CREATE' to create a new profile.
Select profile:
```
Select any profile by the profile name, and you'll be taken to the main menu.
</details>

## Functions & Classes | *PROJECT.PY*
The main `project.py` file has ten functions and one class.

### `greet()` `function`
This function will ONLY be called once to greet the user with PyFiglet's ASCII art.

On the 
```py
if __name__ == '__main__':
```
conditional, greet() is only called once, then main() is tried multiple times, as per the code in `etc.py` until `KeyboardInterrupt` (CTRL + C) is caught.

### `main()` `function`

Checks if the user has selected a profile, then if they haven't, the program will call `select_profile()` and if they have, the `main_menu()` function will be called.

### `main_menu()` `function`
Main menu will prompt the user to select a feature:
1. Add a purchase
2. View data
3. Change profile
4. Mini-calculator
5. Exit
This will select which feature to use and call the appropriate function with a match case (thus Python 3.10 is required.)

### `add_purchase()` `function`
This function will add a purchase to the selected profile; also prompts the user for item name, and item price.

This function will also add the date of which the user has inputted the data.

### `select_profile(mode="NORMAL")` `function`
This function validates and select a profile in the profile base.

Modes: 
* Normal
* (any other string)
If someone uses this function with a different mode other than "NORMAL", (this is used typically on first startup when no profiles have been created) in which it will skip the global `profile` variable conditional and won't return the profile.

### `profiles(create: int = 0)`  `function`
This function will select a profile and have a user prompt in which a user can manipulate profiles with these features:
1. Profile creation
2. Profile name change
3. Profile deletion
4. Returning to menu


### `show_data(profile_name: str, year: int, month: int, mode: str = "table")` `function`

This function will show the table in a format, with profile_name, year, and month to select which profile to use and which month and year to use it. `mode` keyword will select which mode will be shown, in which there exists 2:
* Matplotlib's bar graph
* Tabulate

### `print_user_profiles()`  `function`
This helper function is used to print user profiles.

### `sum_monthly(profile_name: str, year: int, month: int)`  `function`
This function will sum the user's monthly spend.

### `daily_average()` `function`
This function will average the user spending each day in a month.

### `Calculator` `class`