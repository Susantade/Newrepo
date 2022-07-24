from mysql_connection import database_connection
from datetime import datetime
        
def create_table():
    try:
        connection = database_connection()
        if connection.is_connected():
            print('DATABASE CONNECTED')
            query = '''
                    create table python(
                        id int auto_increment,
                        first_name varchar(10),
                        last_name varchar(10),
                        date_time datetime,
                        primary key(id)
                        )'''
            cursor = connection.cursor()
            cursor.execute(query)
            print("Table Sucessfully Created")
    except Error as err:
        print("An error has occured:", err)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Database Connection Closed.")

def insert_many_records(table_name, records):
    try:
        connection = database_connection()
        if connection.is_connected():
            query = '''
                    insert into {0}(first_name, last_name, date_time)
                    values (%s, %s, %s)
                '''.format(table_name)
            cursor = connection.cursor()
            cursor.executemany(query, records)
            connection.commit()
            print(f"Total {cursor.rowcount} records inserted.")
    except Error as err:
        print("An error has occured:", err)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Database Conection Closed.")
    


# DRIVER CODE
if __name__ == '__main__':
    #create_database()

    records = [
        ('abc', 'bcc', datetime.now()),
        ('mnm', 'nnn', datetime.now()),
        ('lkio', 'pop', datetime.now())
        ]
    insert_many_records('python', records)
