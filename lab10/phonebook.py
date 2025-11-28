import psycopg2
import csv
from config import config

# 1. Connect and Create Table
def create_tables():
    """ Create table in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255),
            phone VARCHAR(50) NOT NULL UNIQUE
        )
        """,
    )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        print("Table created successfully")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# 2. Insert Data (Console & CSV)
def insert_console():
    sql = """INSERT INTO phonebook(first_name, last_name, phone)
             VALUES(%s, %s, %s) RETURNING id;"""
    conn = None
    try:
        # User Input
        f_name = input("Enter First Name: ")
        l_name = input("Enter Last Name: ")
        phone = input("Enter Phone: ")

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (f_name, l_name, phone))
        item_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        print(f"Inserted item with ID: {item_id}")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_from_csv(filename):
    sql = "INSERT INTO phonebook(first_name, last_name, phone) VALUES(%s, %s, %s)"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader) # Skip header
            for row in reader:
                cur.execute(sql, (row[0], row[1], row[2]))
            
        conn.commit()
        cur.close()
        print("CSV Data Uploaded")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    except FileNotFoundError:
        print("File not found")
    finally:
        if conn is not None:
            conn.close()

# 3. Update Data
def update_contact():
    sql = "UPDATE phonebook SET first_name = %s WHERE phone = %s"
    conn = None
    try:
        phone_key = input("Enter Phone of user to update: ")
        new_name = input("Enter New First Name: ")
        
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (new_name, phone_key))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
        print(f"Updated {updated_rows} rows")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# 4. Query Data
def get_contacts():
    sql = "SELECT first_name, last_name, phone FROM phonebook"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        print("\n--- PhoneBook ---")
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# 5. Delete Data
def delete_contact():
    sql = "DELETE FROM phonebook WHERE phone = %s"
    conn = None
    try:
        phone_key = input("Enter Phone to delete: ")
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (phone_key,))
        deleted_rows = cur.rowcount
        conn.commit()
        cur.close()
        print(f"Deleted {deleted_rows} rows")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()
    while True:
        print("\n1. Add (Console)\n2. Add (CSV)\n3. Update Name\n4. Show All\n5. Delete\n6. Exit")
        choice = input("Choice: ")
        if choice == '1': insert_console()
        elif choice == '2': 
            f = input("Filename: ")
            insert_from_csv(f)
        elif choice == '3': update_contact()
        elif choice == '4': get_contacts()
        elif choice == '5': delete_contact()
        elif choice == '6': break