import re
import datetime
import csv
import os

def parse_gala_rewards(txt_path, output_csv_path):
    # Simplified pattern to capture any line mentioning GALA rewards
    pattern = r"You received ([\d,\.]+) GALA"
    
    # Read the text file
    with open(txt_path, 'r') as file:
        text = file.read()

    # Find all matches for GALA rewards
    matches = re.finditer(pattern, text)

    # Initialize the data list and a counter for days back
    data = []
    days_back = 0  # Initialize to 0 to adjust on the first match

    # Today's date
    today = datetime.date.today()

    for match in matches:
        days_back += 1  # Increment for each GALA entry found
        amount = match.group(1).replace(',', '')  # Remove commas
        
        date = today - datetime.timedelta(days=days_back)
        
        formatted_date = date.strftime("%m/%d/%Y")  # Assuming date only
        
        # Append the necessary information to the data list
        data.append([formatted_date, "", "", "", "GALA", amount, "", "", "Mining", "", ""])

    # Write the data to a CSV file
    with open(output_csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date (UTC)", "Platform (Optional)", "Asset Sent", "Amount Sent", "Asset Received", "Amount Received", "Fee Currency (Optional)", "Fee Amount (Optional)", "Type", "Description (Optional)", "TxHash (Optional)"])
        writer.writerows(data)

# Ask the user for the path of the text file
txt_path_input = input("Please enter the path of the text file: ")

# Set the output CSV path to the user's Desktop
output_csv_path = os.path.join("/Users/flint/Desktop", "gala_rewards_data.csv")

# Call the function
parse_gala_rewards(txt_path_input, output_csv_path)

print("GALA rewards data has been parsed and saved to:", output_csv_path)
