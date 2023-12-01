import os
import re
import datetime
import csv
from striprtf.striprtf import rtf_to_text

def extract_gala_distributions(rtfd_path, output_csv_path):
    # Read the RTF file from the RTFD bundle
    rtfd_bundle = os.listdir(rtfd_path)
    rtf_file = [file for file in rtfd_bundle if file.endswith('.rtf')][0]
    with open(os.path.join(rtfd_path, rtf_file), 'r') as file:
        rtf_content = file.read()

    # Convert the RTF content to plain text
    text = rtf_to_text(rtf_content)
    
    # Initialize the data list
    data = []
    
    # Prompt the user for the starting date
    date_input = input("Please enter the starting date (MM/DD/YYYY): ")
    month, day, year = map(int, date_input.split('/'))
    current_date = datetime.datetime(year, month, day)
    
    # Extract the pattern for GALA amount
    pattern_gala = r"You received ([\d,]+) GALA"
    matches_gala = re.findall(pattern_gala, text)
    
    # Add the matches to the data list and decrement the date for each match
    for amount in matches_gala:
        formatted_date = current_date.strftime("%m/%d/%Y 21:%M:%S")
        data.append([formatted_date, "", "", "", "GALA", amount.replace(',', ''), "", "", "Income", "", ""])
        current_date -= datetime.timedelta(days=1)


    
    # Write the data to a CSV file
    with open(output_csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date (UTC)", "Platform (Optional)", "Asset Sent", "Amount Sent", "Asset Received", "Amount Received", "Fee Currency (Optional)", "Fee Amount (Optional)", "Type", "Description (Optional)", "TxHash (Optional)"])  # header
        writer.writerows(data)

# Prompt the user for the path of the RTFD bundle
rtfd_path_input = input("Please enter the path of the RTFD file: ")
output_csv_path = '/Users/flint/Desktop/output.csv'  # You can modify this if you want to prompt for the output path as well

# Call the function
extract_gala_distributions(rtfd_path_input, output_csv_path)
