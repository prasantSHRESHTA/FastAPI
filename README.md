# FastAPI CSV Upload and SQLite Storage
This project demonstrates a simple FastAPI application that allows users to upload a CSV file, select columns for "Name" and "Age," and store the data in an SQLite database. The project utilizes FastAPI for the backend, SQLite for data storage, and Jinja templates for the frontend.

# Features
1. CSV Upload: Users can upload a CSV file through the web interface.
2. Column Selection: Users can specify the columns for "Name" and "Age" during the CSV upload.
3. SQLite Storage: The data from the CSV file is stored in an SQLite database with a "Users" table.

# Prerequisites
1. Python 3.7 or later
2. FastAPI
3. SQLite
4. Jinja2

# Installation
1. Clone the repository:

           git clone https://github.com/prasantSHRESHTA/FastAPI.git
   
3. Install the dependencies:

           pip install -r requirements.txt

4. Run the FastAPI application:

           uvicorn main:app --reload

5. Open your web browser and navigate to http://127.0.0.1:8000/ to access the application.

# Usage
1. Access the web interface at http://127.0.0.1:8000/.
2. Upload a CSV file and specify the columns for "Name" and "Age." ( A sample csv file(content.csv) is included ).
3. Click the submit button to store the data in the SQLite database.
4. View the database content at http://127.0.0.1:8000/users/.
