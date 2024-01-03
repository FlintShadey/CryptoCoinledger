import csv
import os
import datetime

def extract_gala_distributions(csv_path, output_csv_path):
    # Open the CSV file
    with open(csv_path, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        # Initialize the data list
        data = []

        # Iterate over the rows in the CSV file
        for row in reader:
            description, date, quantity, currency, *rest = row

            # Check if the currency is GALA[GC]
            if currency == "GALA[GC]":
                # Format the date
                date_obj = datetime.datetime.fromisoformat(date)
                formatted_date = date_obj.strftime("%m/%d/%Y %H:%M:%S")

                # Set the type to "Mining"
                type_value = "Mining"
                currency = "GALA"

                # Append the necessary information to the data list
                data.append([formatted_date, "", "", "", currency, quantity, "", "", type_value, description, ""])

    # Write the data to a CSV file
    with open(output_csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date (UTC)", "Platform (Optional)", "Asset Sent", "Amount Sent", "Asset Received", "Amount Received", "Fee Currency (Optional)", "Fee Amount (Optional)", "Type", "Description (Optional)", "TxHash (Optional)"])
        writer.writerows(data)

# Get the CSV path input from the user
csv_path_input = input("Please enter the path of the CSV file: ")

# Set the output CSV path
output_csv_dir = os.path.dirname(csv_path_input)
output_csv_path = os.path.join(output_csv_dir, 'GALA_output.csv')

# Call the function
extract_gala_distributions(csv_path_input, output_csv_path)

print("New CSV file saved to: " + output_csv_path)
