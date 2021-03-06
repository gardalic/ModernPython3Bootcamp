"""update_users : Takes in an old first name, an old last name, a new first name, and a new last name. Updates the users.csv file so that any user whose first and last names match the old first and last names are updated to the new first and last names. The function should return a count of how many users were updated."""
"""
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
"""
import csv


def update_users(old_first, old_last, new_first, new_last):
    filename = "users.csv"
    with open(filename) as f:
        csv_reader = csv.reader(f)
        rows = list(csv_reader)

    count = 0
    with open(filename, "w", newline="") as file:
        csv_writer = csv.writer(file)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)
    return f"Users updated {count}"


print(update_users("Grace", "Hopper", "Hello", "World"))
print(update_users("Colt", "Steele", "Boba", "Fett"))
print(update_users("Not", "Here", "Still not", "Here"))
