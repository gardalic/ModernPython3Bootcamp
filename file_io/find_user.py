"""find_user : Takes in a first name and a last name and searches for a user with that first and last name in the users.csv file. 
If the user is found, find_user returns the index where the user is found. Otherwise it returns a message stating that the user wasn't found."""
'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''
import csv

def find_user(first, last):
    filename = "users.csv"

    with open(filename) as f:
        csv_reader = csv.reader(f)
        pos_name = False
        # Can separate header, but not really needed
        for (index, row) in enumerate(csv_reader):
            # print(index, row)
            if (row[0], row[1]) == (first, last):
                pos_name = index
                break
        if pos_name:
            print(index)
        else:
            print(first + " " + last + " not found.")

find_user("Colt", "Steele")