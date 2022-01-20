#Hopeson Ehizele

import sqlite3

conn = sqlite3.connect('md-vaccinations.sqlite3')
cursor = conn.cursor()

resp = int(input('Please enter a number that represents one of these choices: \n'
        '1. AMERICAN INDIAN OR ALASKAN NATIVE\n'
        '2) BLACK OR AFRICAN AMERICAN\n'
        '3) ASIAN\n'
        '4) NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER\n'
        '5) TWO OR MORE RACES\n'
        '6) WHITE\n'
        'Enter a number: '))

if resp == 1:
    race = "AMERICAN INDIAN OR ALASKAN NATIVE"
elif resp == 2:
    race = "BLACK OR AFRICAN AMERICAN"
elif resp == 3:
    race = "ASIAN"
elif resp == 4:
    race = "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER"
elif resp == 5:
    race = "TWO OR MORE RACES"
elif resp == 6:
    race = "WHITE"
else: 
    raise ValueError("Invalid input")

query = """SELECT SUM(second_dose_daily + single_dose_daily AS Dose)
            FROM vaccinations
            WHERE race= :r"""

cursor.execute(query, {'r': race})
print(f"The total number of vaccinations for the '{race}' racial group in Maryland is {cursor.fetchall()}")