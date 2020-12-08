from csv import DictReader, DictWriter

def cm_to_inch(cm):
    return float(cm) * 0.393701

filename = 'file_io/fighters.csv'

with open(filename, newline='') as file:
    csv_reader = DictReader(file)
    headers = csv_reader.fieldnames
    records = list(csv_reader)
    headers.append('Height (in in)')

with open(f"new_fighters.csv", 'w', newline='') as file:
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for r in records:
        r['Height (in in)'] = round(cm_to_inch(r['Height (in cm)']), 2)
        csv_writer.writerow(r)
