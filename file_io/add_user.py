"""For this exercise, you'll be working with a file called users.csv. Each row of data consists of two columns:
a user's first name, and a user's last name.Implement the following function: 
    add_user : Takes in a first name and a last name and adds a new user to the users.csv file."""
"""
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
"""
from csv import writer


filename = "users.csv"


def add_user(first, last):
    with open(filename, "a", newline="") as f:
        csv_writer = writer(f)
        csv_writer.writerow([first, last])
