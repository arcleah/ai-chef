import sqlite3
from sqlite3 import Error

def create_connection(db_file): # Connect to database
    """ Create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file, check_same_thread=False)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql): # Create a table
    """ Create a table from the create_table_sql statement """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("Table created!")
    except Error as e:
        print(e)

def create_user(conn, user): # Create a user table
    """
    Create a new user in the users table
    :param conn:
    :param user: tuple containing user email, password, name, dietary restrictions, allergies, preferences
    """
    sql = ''' INSERT INTO users(email, password, name, dietary_restrictions, allergies, preferences)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()

    return cur.lastrowid
    
def create_pantry(conn, pantry): # Create an pantry table
    """
    Create a new pantry in the pantry table
    :param conn:
    :param pantry: tuple containing pantry id, food, expiry date, amount
    """
    sql = ''' INSERT INTO pantry(userId, food, expiry_date, amount)
             VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, pantry)
    conn.commit()

    return cur.lastrowid

def main():
    database = r"C:\Users\yo-s-\Documents\GitHub\ai-chef\sqlite\database.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY, 
                                        email text NOT NULL,
                                        password text NOT NULL,
                                        name text NOT NULL,
                                        dietary_restrictions text,
                                        allergies text,
                                        preferences text
                                    ); """
                                    
    sql_create_pantry_table = """ CREATE TABLE IF NOT EXISTS pantry (
                                        id integer PRIMARY KEY, 
                                        userId integer NOT NULL,
                                        food text NOT NULL,
                                        expiry_date date NOT NULL,
                                        amount integer NOT NULL
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_pantry_table)
    else:
        print("Error! cannot create the database connection.")

    # Insert user data (example)
    with conn:
        user_1 = ('johndoe123@gmail.com', '1234', 'John Doe', 'Lactose', 'Peanuts', 'Spicy food')
        # create user
        create_user(conn, user_1)
        
        # create pantry
        pantry_1 = (1, 'milk', '2014-07-28', 1)
        pantry_2 = (1, 'carrots', '2015-06-18', 4)
        pantry_3 = (1, 'steak', '2023-02-15', 1)
        create_pantry(conn, pantry_1)
        create_pantry(conn, pantry_2)
        create_pantry(conn, pantry_3)

if __name__ == '__main__':
    main()

