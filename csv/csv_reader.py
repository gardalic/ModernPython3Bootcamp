from csv import reader, DictReader

with open("file_io/fighters.csv") as f:
    csv_reader = reader(f)
    print("Opened and read with reader()")
    for row in csv_reader:
        print(row)


with open("file_io/fighters.csv") as f:
    csv_reader = DictReader(f)
    print("Opened and read with DictReader()")
    for row in csv_reader:
        print(row['Name'])