"""
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
"""
import csv


def delete_users(first, last):
    filename = "users.csv"
    with open(filename) as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)

    count = 0

    with open(filename, "w", newline="") as file:
        csv_writer = csv.writer(file)
        for row in rows:
            if row[0] == first and row[1] == last:
                count += 1
            else:
                csv_writer.writerow(row)

    return f"Users deleted: {count}."

print(delete_users("Grace", "Hopper"))