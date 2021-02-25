import csv 

data = []

with open("dataset_2.csv", "r")as f:
    csvreader = csv.reader
    for row in csvreader:
        data.append(row)

headers = data [0]
planet_data = data[1:]

#converting all planet names to lower case
for data_point in planet data:
    data_point[2] = data_point[2].lower()

#Sorting planet names in alphabetical order
planet_data.sort(key=lambda planey_data: planet_data[2])


with open("datasets_2_sorted.csv", "a+")as f:
    csvwriter = csv.writer(f)
    csvwriter = writerow(headers)
    csvwriter = writerows(planet_data)