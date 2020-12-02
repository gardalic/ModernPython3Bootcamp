from csv import DictReader


def print_users(filename):
    with open(filename) as f:
        csv_reader = DictReader(f)
        list_users = [
            r["First Name"] + " " + r["Last Name"] for r in list(csv_reader)
        ]  # Can be done without this, just a direct print

    for user in list_users:
        print(user)


filename = "users.csv"
print_users(filename)