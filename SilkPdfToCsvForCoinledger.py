from pdf2image import convert_from_path
import pytesseract
import re
import datetime
import csv

def extract_silk_distributions(pdf_path, output_csv_path):
    # Convert the PDF to images
    images = convert_from_path(pdf_path)
    
    # Initialize the data list
    data = []
    
    # Prompt the user for the starting date
    date_input = input("Please enter the starting date (MM/DD/YYYY): ")
    month, day, year = map(int, date_input.split('/'))
    current_date = datetime.datetime(year, month, day)
    
    # Extract text from each image using pytesseract
    for image in images:
        text = pytesseract.image_to_string(image)
        
        # Extract the pattern for SILK amount
        pattern_silk = r"(0.\d{1,6}) SILK"
        matches_silk = re.findall(pattern_silk, text)
        
        # Add the matches to the data list and decrement the date for each match
        for amount in matches_silk:
            formatted_date = current_date.strftime("%m/%d/%Y %H:%M:%S")
            data.append([formatted_date, "", "", "", "SILK", amount, "", "", "Income", "", ""])
            current_date -= datetime.timedelta(days=1)
    
    # Write the data to a CSV file
    with open(output_csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date (UTC)", "Platform (Optional)", "Asset Sent", "Amount Sent", "Asset Received", "Amount Received", "Fee Currency (Optional)", "Fee Amount (Optional)", "Type", "Description (Optional)", "TxHash (Optional)"])  # header
        writer.writerows(data)

# Prompt the user for the path of the PDF
pdf_path_input = input("Please enter the path of the PDF file: ")

# Set the output CSV path to "/Users/flint/Desktop/SILKoutput.csv"
output_csv_path = "/Users/flint/Desktop/SILKoutput.csv"

# Call the function
extract_silk_distributions(pdf_path_input, output_csv_path)
