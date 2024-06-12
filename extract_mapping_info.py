import os
import csv

def extract_info(file_path):
    """
    Extracts the number of input reads, uniquely mapped reads number,
    and uniquely mapped reads percentage from a STAR log file.

    Parameters:
    file_path (str): The path to the log file.

    Returns:
    dict: A dictionary containing the extracted information.
    """
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

def process_log_files(directory):
    """
    Processes all STAR log files in the specified directory to extract
    mapping information and write it to a CSV file.

    Parameters:
    directory (str): The path to the directory containing the log files.
    """
    data = []
    for filename in os.listdir(directory):
        if filename.endswith("Log.final.out"):
            file_path = os.path.join(directory, filename)
            file_info = extract_info(file_path)
            data.append(file_info)

    csv_file = os.path.join(directory, "mapping_summary.csv")
    fieldnames = ["Filename", "Number of input reads", "Uniquely mapped reads number", "Uniquely mapped reads %"]

    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

    print(f"Data successfully written to {csv_file}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extract mapping information from STAR log files.")
    parser.add_argument("directory", help="The directory containing the STAR log files.")
    args = parser.parse_args()

    process_log_files(args.directory)
