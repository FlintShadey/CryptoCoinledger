from pdf2image import convert_from_path
import pytesseract
import re
import datetime
import csv

def extract_gala_distributions(pdf_path, output_csv_path):
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
        
        # Extract the pattern for GALA amount
        pattern_gala = r"([\d]+\.\d{1,2}) GALA"
        matches_gala = re.findall(pattern_gala, text)
        
        # Add the matches to the data list and decrement the date for each match
        for amount in matches_gala:
            formatted_date = current_date.strftime("%m/%d/%Y %H:%M:%S")
            data.append([formatted_date, "", "", "", "GALA", amount, "", "", "Income", "", ""])
            current_date -= datetime.timedelta(days=1)
    
    # Write the data to a CSV file
    with open(output_csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date (UTC)", "Platform (Optional)", "Asset Sent", "Amount Sent", "Asset Received", "Amount Received", "Fee Currency (Optional)", "Fee Amount (Optional)", "Type", "Description (Optional)", "TxHash (Optional)"])  # header
        writer.writerows(data)

# Prompt the user for the path of the PDF
pdf_path_input = input("Please enter the path of the PDF file: ")
output_csv_path = '/Users/flint/Desktop/output.csv'  # You can modify this if you want to prompt for the output path as well

# Call the function
extract_gala_distributions(pdf_path_input, output_csv_path)
