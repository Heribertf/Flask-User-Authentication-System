# Flask-User-Authentication-System

Prerequisites

Python 3.8+
Basic understanding of Python
Basic knowledge of web development concepts
SQL Server installed
ODBC Driver for SQL Server

Project Setup

1. Project Structure
   Create the following directory structure:

flask_user_system/
├── app.py
├── db_connection.py
├── templates/
│ ├── base.html
│ ├── login.html
│ ├── register.html
│ └── home.html

2. Dependencies

# Install required packages

pip install flask bcrypt pyodbc

3. Database Preparation
   Before running the application, you'll need to set up your SQL Server database:

Create a database named UserSystemDB(or any name of your choice)
Create a Users table:

CREATE TABLE Users (
UserID INT IDENTITY PRIMARY KEY,
Username NVARCHAR(50) UNIQUE NOT NULL,
PasswordHash NVARCHAR(255) NOT NULL,
CreatedAt DATETIME DEFAULT GETDATE()
);

4. Database Connection (db_connection.py)

5. Application Code (app.py)

6. HTML Templates
   templates/base.html
   This serves as the base template for consistent layout.

templates/login.html
templates/register.html
templates/home.html

7. Running the Application
   a. Run the Flask app:
   python app.py

b. Access the system in your browser at http://127.0.0.1:5000.
