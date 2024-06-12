import os
import csv

# Directory containing the log files
log_directory = "log_files"

# List to store the extracted data
data = []

# Function to extract the relevant information from a log file
def extract_info(file_path):
    info = {"Filename": os.path.basename(file_path)}
    with open(file_path, 'r') as file:
        for line in file:
            if "Number of input reads" in line:
                info["Number of input reads"] = line.split('|')[1].strip()
            elif "Uniquely mapped reads number" in line:
                info["Uniquely mapped reads number"] = line.split('|')[1].strip()
            elif "Uniquely mapped reads %" in line:
                info["Uniquely mapped reads %"] = line.split('|')[1].strip()
    return info

# Iterate over all files in the directory
for filename in os.listdir(log_directory):
    if filename.endswith("Log.final.out"):
        file_path = os.path.join(log_directory, filename)
        file_info = extract_info(file_path)
        data.append(file_info)

# CSV file to store the results
csv_file = "mapping_summary.csv"

# Fieldnames for the CSV file
fieldnames = ["Filename", "Number of input reads", "Uniquely mapped reads number", "Uniquely mapped reads %"]

# Write the data to the CSV file
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for entry in data:
        writer.writerow(entry)

print(f"Data successfully written to {csv_file}")
