import csv
from datetime import datetime

# Prompt the user for the path to the CSV file
csv_path = input("Enter the path to the CSV file: ")

# Read the CSV file
with open(csv_path, 'r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Trim spaces from column names
    csv_reader.fieldnames = [name.strip() for name in csv_reader.fieldnames]

    # Prepare to write to the new CSV file
    with open('/Users/flint/Desktop/POKT output.csv', 'w', newline='') as output_file:
        fieldnames = ["Date (UTC)", "Platform (Optional)", "Asset Sent", "Amount Sent", "Asset Received", "Amount Received", "Fee Currency (Optional)", "Fee Amount (Optional)", "Type", "Description (Optional)", "TxHash (Optional)"]
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for row in csv_reader:
            # Convert the date column
            date_format = "%m/%d/%Y %H:%M:%S"
            date_str = datetime.strptime(row['Date'], '%Y-%m-%d %H:%M:%S').strftime(date_format)

            # Prepare the new row
            new_row = {
                "Date (UTC)": date_str,
                "Asset Received": "POKT",
                "Type": "Income"
            }

            if row["Transaction Type"] == "Rewards Rollover":
                new_row["Amount Received"] = row["Amount"]

            csv_writer.writerow(new_row)

print("New CSV file saved to /Users/flint/Desktop/POKT output.csv")
