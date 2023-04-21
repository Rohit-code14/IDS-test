import csv
import random

# Define input file paths
file1_path = "logstrue.csv"
file2_path = "logdataset.csv"

# Define output file path
output_path = "finaldataset.csv"

# Define a function to check for duplicates
def has_duplicate(row, data):
    for d in data:
        if row == d:
            return True
    return False

# Read in data from both input files
data1 = []
with open(file1_path, "r") as file1:
    csv_reader = csv.reader(file1)
    for row in csv_reader:
        data1.append(row)

data2 = []
with open(file2_path, "r") as file2:
    csv_reader = csv.reader(file2)
    for row in csv_reader:
        data2.append(row)

# Mix up rows from both files
mixed_data = []
for row in data1:
    if not has_duplicate(row, mixed_data):
        mixed_data.append(row)
for row in data2:
    if not has_duplicate(row, mixed_data):
        mixed_data.append(row)

# Write mixed data to output file
with open(output_path, "w", newline="") as output_file:
    csv_writer = csv.writer(output_file)
    for row in mixed_data:
        csv_writer.writerow(row)
