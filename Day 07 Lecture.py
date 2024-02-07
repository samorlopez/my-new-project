import csv
import json

sample_csv_data = [
    ['NAME', 'AGE', 'CITY'],
    ['Samuel', 19, 'Seattle'],
    ['Lei Ann', 19, 'Tacoma'],
    ['Thomas', 21, 'Des Moines'],
    ['Eliot', 19, 'San Francisco'],
]

with open("in_class_csv_file.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(sample_csv_data)

