from csv import reader, writer

with open("file_io/fighters.csv") as f:
    csv_reader = reader(f)
    fighters = [[data.upper() for data in row] for row in csv_reader]

print(f"Fighters - {fighters}")

with open("file_io/fighters2.csv", "w", newline='') as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)
