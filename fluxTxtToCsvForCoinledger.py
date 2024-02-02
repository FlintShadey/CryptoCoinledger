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
    
    # Extract the datetime and FLUX amount from the text using regex
    pattern = r"Mined (\w{3} \d{1,2}, \d{4} \d{1,2}:\d{2}:\d{2} [APM]{2}).+?CONFIRMATIONS (\d+\.\d+)"
    matches = re.finditer(pattern, text, re.DOTALL)

    for match in matches:
        extracted_datetime_str, flux_amount = match.groups()
        # Parse the extracted datetime string
        current_date = datetime.datetime.strptime(extracted_datetime_str, "%b %d, %Y %I:%M:%S %p")

        formatted_date = current_date.strftime("%m/%d/%Y %H:%M:%S")
        data.append([formatted_date, "", "", "", "FLUX", 2.8125, "", "", "Mining", "", ""])

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

print("New CSV file saved to: " + output_csv_path)
