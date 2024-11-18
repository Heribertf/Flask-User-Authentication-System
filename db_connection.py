import pyodbc

def get_db_connection():
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=your_server_name;'
        'DATABASE=UserSystemDB;'
        'UID=your_username;'
        'PWD=your_password;'
    )
    return connection
