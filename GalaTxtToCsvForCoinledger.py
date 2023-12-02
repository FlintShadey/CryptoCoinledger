import os
import re
import datetime
import csv

def extract_gala_distributions(txt_path, output_csv_path):
    # Read the text file
    with open(txt_path, 'r') as file:
        text = file.read()
    
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


# Prompt the user for the path of the text file
txt_path_input = input("Please enter the path of the text file: ")

# Set the output CSV path to 'GALA_output.csv' in the same directory as the input text file
output_csv_dir = os.path.dirname(txt_path_input)
output_csv_path = os.path.join(output_csv_dir, 'GALA_output.csv')

# Call the function
extract_gala_distributions(txt_path_input, output_csv_path)

print("New CSV file saved to Desktop - GALA output.csv")
