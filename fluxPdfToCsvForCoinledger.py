import re
import os
import datetime
import csv

def extract_flux_distributions_from_text(txt_path, output_csv_path):
    # Read the text file
    with open(txt_path, 'r') as file:
        text = file.read()

    # Initialize the data list
    data = []
    
    # Extract the datetime from the text using regex
    pattern_datetime = r"Mined (\w{3} \d{1,2}, \d{4} \d{1,2}:\d{2}:\d{2})"
    match_datetime = re.search(pattern_datetime, text)

    if match_datetime:
        extracted_datetime_str = match_datetime.group(1)
        # Parse the extracted datetime string
        current_date = datetime.datetime.strptime(extracted_datetime_str, "%b %d, %Y %I:%M:%S")
        
        # Extract the pattern for FLUX amount
        pattern_flux = r"TIONS (\d+\.\d+)"
        matches_flux = re.findall(pattern_flux, text)
        
        # Add the matches to the data list using the captured date
        for amount in matches_flux:
            formatted_date = current_date.strftime("%m/%d/%Y %H:%M:%S")
            data.append([formatted_date, "", "", "", "FLUX", amount, "", "", "Income", "", ""])

    # Write the data to a CSV file
    with open(output_csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date (UTC)", "Platform (Optional)", "Asset Sent", "Amount Sent", "Asset Received", "Amount Received", "Fee Currency (Optional)", "Fee Amount (Optional)", "Type", "Description (Optional)", "TxHash (Optional)"])  # header
        writer.writerows(data)

# Prompt the user for the path of the text file
txt_path_input = input("Please enter the path of the text file: ")

# Set the output CSV path to 'FLUX_output.csv' in the same directory as the input text file
output_csv_dir = os.path.dirname(txt_path_input)
output_csv_path = os.path.join(output_csv_dir, 'FLUX_output.csv')

# Call the function
extract_flux_distributions_from_text(txt_path_input, output_csv_path)

print("New CSV file saved to Desktop  - FLUX output.csv")