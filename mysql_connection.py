# Database Connection

from mysql.connector import connect, Error
from configparser import ConfigParser
import os

def read_database_config(file_name):
    if str(file_name).rsplit('.')[1] == 'ini':
        os.chdir("E:\python122")
        parser = ConfigParser()
        parser.read(file_name)
        db = {}
        if parser.has_section('mysql'):
            db['host'] = parser.get('mysql', 'host')
            db['port'] = parser.get('mysql', 'port')
            db['database'] = parser.get('mysql', 'database')
            db['password'] = parser.get('mysql', 'password')
            db['user'] = parser.get('mysql', 'user')
            return db
        else:
            raise SystemExit('MySQL database connection informations are not in your file.')
    else:
        raise SystemExit("Invalid File Extension. File extension must be '*.ini'")
    

def database_connection():
    db_configs = read_database_config("db.ini")
    return connect(**db_configs)
    
