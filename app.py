from flask import Flask, render_template, request
import PyPDF2
import re
import csv


app = Flask(__name__)

def extract_data_from_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    num_pages = pdf_reader.numPages

    extracted_data = []

    for page_num in range(num_pages):
        page = pdf_reader.getPage(page_num)
        text = page.extractText()
        
        # Extract key-value pairs using regular expressions
        key_value_pairs = re.findall(r'([^\n:]+)\s*:\s*([^\n]+)', text)
        extracted_data.extend(key_value_pairs)

    return extracted_data

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')
        
        file = request.files['file']
        
        if file.filename == '':
            return render_template('index.html', error='No selected file')

        if file:
            data = extract_data_from_pdf(file)
            return render_template('index.html', data=data)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


def extract_key_value_pairs(text):
    key_value_pairs = {}
    lines = text.split('\n')
    for line in lines:
        if ':' in line:
            key, value = map(str.strip, line.split(':', 1))
            key_value_pairs[key] = value
    return key_value_pairs

def extract_table_data(text):
    # You may implement table extraction using tabula-py or other libraries here
    pass

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def main(pdf_file, csv_file):
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    num_pages = pdf_reader.numPages

    all_data = []



if __name__ == "__main__":
    pdf_file_path = "sample1.pdf"  # Provide the path to your PDF file
    #csv_file_path = "output.csv"   # Provide the desired output CSV file path
    main(pdf_file_path,) #csv_file_path)
