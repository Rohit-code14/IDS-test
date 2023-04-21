import csv

# Define the filenames for each column
column1_filename = "accept_mimetypes.txt"
column2_filename = "time_in_millis.txt"
column3_filename = "request_uri.txt"
column4_filename = "ips.txt"
column5_filename = "content_lengths.txt"
column6_filename = "request_types.txt"
column7_filename = "user_agents.txt"
column8_filename = "random_strings.txt"
column9_filename = "safe.txt"

# Define the filename for the CSV file
csv_filename = "logdataset.csv"

# Read the data from each file and store it in a list
with open(column1_filename, "r") as f:
    column1_data = f.read().splitlines()

with open(column2_filename, "r") as f:
    column2_data = f.read().splitlines()

with open(column3_filename, "r") as f:
    column3_data = f.read().splitlines()

with open(column4_filename, "r") as f:
    column4_data = f.read().splitlines()

with open(column5_filename, "r") as f:
    column5_data = f.read().splitlines()

with open(column6_filename, "r") as f:
    column6_data = f.read().splitlines()

with open(column7_filename, "r") as f:
    column7_data = f.read().splitlines()

with open(column8_filename, "r") as f:
    column8_data = f.read().splitlines()

with open(column9_filename, "r") as f:
    column9_data = f.read().splitlines()

# Combine the data from each column into a list of tuples
data = list(zip(column1_data, column2_data, column3_data, column4_data, column5_data, column6_data, column7_data, column8_data, column9_data))

# Write the data to the CSV file
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["mimetype", "timestamp", "request_uri","user_ip", "content_length", "request_type", "user_agent", "message", "is_xss"])
    for row in data:
        writer.writerow(row)

print(f"Successfully generated CSV file {csv_filename} with data from {column1_filename}, {column2_filename}, and {column3_filename}.")
