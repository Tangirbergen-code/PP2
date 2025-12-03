import psycopg2
from config import config

# --- SQL SECTION: Stored Procedures & Functions ---
sql_create_functions = """
-- 1. Search by pattern (Name, Surname, or Phone)
CREATE OR REPLACE FUNCTION get_users_by_pattern(pattern_text VARCHAR)
RETURNS TABLE (id INTEGER, first_name VARCHAR, last_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.first_name, p.last_name, p.phone
    FROM phonebook p
    WHERE p.first_name ILIKE '%' || pattern_text || '%'
       OR p.last_name ILIKE '%' || pattern_text || '%'
       OR p.phone ILIKE '%' || pattern_text || '%';
END;
$$ LANGUAGE plpgsql;

-- 2. Add User (Update phone if user exists, otherwise Insert)
CREATE OR REPLACE PROCEDURE add_or_update_user(
    p_first_name VARCHAR, 
    p_last_name VARCHAR, 
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_first_name AND last_name = p_last_name) THEN
        -- User exists: Update phone
        UPDATE phonebook SET phone = p_phone WHERE first_name = p_first_name AND last_name = p_last_name;
    ELSE
        -- User new: Insert
        INSERT INTO phonebook (first_name, last_name, phone) VALUES (p_first_name, p_last_name, p_phone);
    END IF;
END;
$$;

-- 3. Insert List with Validation (Returns invalid data)
CREATE OR REPLACE FUNCTION insert_many_users(
    first_names VARCHAR[], 
    last_names VARCHAR[], 
    phones VARCHAR[]
)
RETURNS TABLE (bad_first_name VARCHAR, bad_last_name VARCHAR, bad_phone VARCHAR, error_msg VARCHAR) AS $$
DECLARE
    i INTEGER;
    len INTEGER;
    chk_phone VARCHAR;
BEGIN
    len := array_length(phones, 1);
    
    FOR i IN 1..len LOOP
        chk_phone := phones[i];
        
        -- Validation: Phone must be digits only and length >= 10
        IF (chk_phone ~ '^[0-9]+$') AND (length(chk_phone) >= 10) THEN
            CALL add_or_update_user(first_names[i], last_names[i], chk_phone);
        ELSE
            -- Invalid data: Return it
            bad_first_name := first_names[i];
            bad_last_name := last_names[i];
            bad_phone := chk_phone;
            error_msg := 'Invalid Phone Format';
            RETURN NEXT;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- 4. Get users with Pagination
CREATE OR REPLACE FUNCTION get_users_paginated(limit_val INTEGER, offset_val INTEGER)
RETURNS TABLE (id INTEGER, first_name VARCHAR, last_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.first_name, p.last_name, p.phone
    FROM phonebook p
    ORDER BY p.id ASC
    LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;

-- 5. Delete User by Name or Phone
CREATE OR REPLACE PROCEDURE delete_user_proc(criteria VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook 
    WHERE first_name = criteria 
       OR last_name = criteria 
       OR phone = criteria;
END;
$$;
"""

# --- PYTHON SECTION ---

def init_db_functions():
    """Create all SQL functions in Database"""
    conn = None
    try:
        conn = psycopg2.connect(**config())
        cur = conn.cursor()
        cur.execute(sql_create_functions)
        conn.commit()
        cur.close()
        print("SQL Functions created successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn: conn.close()

# Task 1: Search
def search_user():
    pattern = input("\nSearch (name/phone): ")
    sql = "SELECT * FROM get_users_by_pattern(%s);"
    try:
        conn = psycopg2.connect(**config())
        cur = conn.cursor()
        cur.execute(sql, (pattern,))
        rows = cur.fetchall()
        print(f"\nMatches found: {len(rows)}")
        for row in rows:
            print(row)
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Task 2: Procedure Add/Update
def add_user_proc():
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
    phone = input("Phone: ")
    
    sql = "CALL add_or_update_user(%s, %s, %s);"
    try:
        conn = psycopg2.connect(**config())
        cur = conn.cursor()
        cur.execute(sql, (f_name, l_name, phone))
        conn.commit()
        print("User saved via Procedure.")
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Task 3: Insert List
def insert_list_mode():
    # Test Data: 2 valid, 2 invalid
    names_f = ["Alice", "Bob", "Charlie", "David"]
    names_l = ["Wonder", "Builder", "Chocolate", "Error"]
    phones  = ["87771112233", "wrong_phone", "87015556677", "123"] 
    
    print(f"\nProcessing list of {len(names_f)} users...")

    sql = "SELECT * FROM insert_many_users(%s, %s, %s);"
    try:
        conn = psycopg2.connect(**config())
        cur = conn.cursor()
        cur.execute(sql, (names_f, names_l, phones))
        incorrect_data = cur.fetchall()
        conn.commit()
        
        if incorrect_data:
            print("--- Skipped Invalid Data ---")
            for row in incorrect_data:
                print(f"Error: {row[0]} {row[1]} ({row[2]}) -> {row[3]}")
        else:
            print("All data valid and inserted.")
            
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Task 4: Pagination
def query_pagination():
    try:
        limit = int(input("Limit (rows): "))
        offset = int(input("Offset (skip): "))
    except ValueError:
        return

    sql = "SELECT * FROM get_users_paginated(%s, %s);"
    try:
        conn = psycopg2.connect(**config())
        cur = conn.cursor()
        cur.execute(sql, (limit, offset))
        rows = cur.fetchall()
        print(f"\n--- Page Result ---")
        for row in rows:
            print(row)
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Task 5: Delete
def delete_user_proc():
    criteria = input("Delete by Name/Phone: ")
    sql = "CALL delete_user_proc(%s);"
    try:
        conn = psycopg2.connect(**config())
        cur = conn.cursor()
        cur.execute(sql, (criteria,))
        conn.commit()
        print("Delete executed.")
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# --- MAIN ---
if __name__ == '__main__':
    # Initialize SQL procedures first
    init_db_functions()
    
    while True:
        print("\n--- MENU ---")
        print("1. Search (Function)")
        print("2. Add/Update (Procedure)")
        print("3. Insert List (Loop/Check)")
        print("4. Pagination")
        print("5. Delete (Procedure)")
        print("6. Exit")
        
        choice = input("Choice: ")
        
        if choice == '1': search_user()
        elif choice == '2': add_user_proc()
        elif choice == '3': insert_list_mode()
        elif choice == '4': query_pagination()
        elif choice == '5': delete_user_proc()
        elif choice == '6': break