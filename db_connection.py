import pyodbc

def get_db_connection():
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=192.168.0.107;'
        'DATABASE=TestDB;'
        'UID=sa;'
        'PWD=@Felimu21;'
    )
    return connection
