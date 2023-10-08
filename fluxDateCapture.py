import re
from PyPDF2 import PdfReader

def extract_dates_from_pdf(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        
        # Initialize an empty string to store the content of the PDF
        content = ""
        
        # Extract text from each page
        for page in reader.pages:
            content += page.extract_text()
        
        # Regular expression pattern to match the date format
        pattern = r"Mined (\w+ \d+, \d{4} (\d{1,2}:\d{2}:\d{2}) (AM|PM))"
        
        # Find all matches
        matches = re.findall(pattern, content)
        
        # Convert the matched dates to the desired format
        for match in matches:
            date_str, time, meridiem = match
            hour, minute, second = map(int, time.split(':'))
            
            # Convert to 24-hour format
            if meridiem == "PM" and hour != 12:
                hour += 12
            elif meridiem == "AM" and hour == 12:
                hour = 0
            
            month_name, day, year = re.search(r"(\w+) (\d+), (\d{4})", date_str).groups()
            month_number = {
                'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
                'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
            }.get(month_name, '00')
            
            formatted_date = f"{month_number}/{day}/{year} {hour:02}:{minute:02}:{second:02}"
            print(formatted_date)

if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF: ")
    extract_dates_from_pdf(pdf_path)
