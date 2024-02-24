<h1 align="center"> PDF Data Extraction and Rapid Prototyping</h1>
<h2 align="center"> Below is an example of a simple web application built using Flask for the backend and HTML/CSS for the frontend. The application allows users to upload a PDF file, extracts data using the script, and displays the extracted data on the webpage. </h2>

### Approach:
#### Backend (Flask):
- Utilize Flask to create a web server.
- Implement a route for handling file uploads and data extraction.
- Use PyPDF2 library to extract data from the uploaded PDF file.
- Process the extracted data and pass it to the frontend.

#### Frontend (HTML/CSS):
- Create a simple HTML form for file upload.
- Use CSS for minimal styling.
- Display the extracted data in a user-friendly format on the webpage.

### How to Run:
1. Navigate to the directory containing app.py.
2. Run python app.py in the terminal.
3. Open your web browser and go to http://127.0.0.1:5000/.
4. Upload a PDF file using the provided form.
5. The extracted data will be displayed on the webpage.

### Challenges:
- **Handling PDF Data:** Extracting data from PDF files can be challenging, especially when dealing with complex layouts and structures. In this example, we assume a simple structure for the PDF.
- **File Upload:** Managing file uploads and processing them securely on the backend requires careful consideration, especially in a production environment. We'll keep it simple for this example.
- **Displaying Data:** Formatting and displaying the extracted data in a user-friendly manner on the webpage can require some effort, especially if the data is unstructured.
