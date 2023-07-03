import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    - Connects to studentdb
    - Drops sparkifydb if exists
    - Creates sparkifydb
    
    Returns:
        cur - cursor to sparkifydb
        conn - connection to sparkifydb
    """
    
    # connect to default database
    try:
        conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    except psycopg2.Error as e:
        print("Error: Unable to create connection to Postgres database - studentdb")
        print(e)
    
    # set the session autocommit = true
    try:
        conn.set_session(autocommit=True)
    except psycopg2.Error as e:
        print("Error: Unable to set autocommit to Postgres database - studentdb")
        print(e)

    # get the cursor
    try:
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("Error: Unable to create cursor to Postgres database - studentdb")
        print(e)
    
    # drop database sparkifydb if exists
    try:
        cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    except psycopg2.Error as e:
        print("Error: Unable to drop database - sparkifydb")
        print(e)

    # create sparkify database with UTF8 encoding
    try:
        cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")
    except psycopg2.Error as e:
        print("Error: Unable to create database - sparkifydb")
        print(e)


    # close connection to default database
    try:
        conn.close()    
    except psycopg2.Error as e:
        print("Error: Unable to close the connection to database - studentdb")
        print(e)

    # connect to sparkify database
    try:
        conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    except psycopg2.Error as e:
        print("Error: Unable to connect to database - sparkifydb")
        print(e)

    # get cursor to sparkifydb
    try:
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("Error: Unable to get cursor to database - sparkifydb")
        print(e)

    # return to caller with cur (cursor) and conn (connection)
    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    Parameters:
        cur: cursor to sparkifydb
        conn: connection to sparkifydb
    
    Returns:
        Nothing
    """
    try:
        for query in drop_table_queries:
            cur.execute(query)
            conn.commit()
    except psycopg2.Error as e:
        print("Error: Unable to drop tables - sparkifydb")
        print(e)


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    Parameters:
        cur: cursor to sparkifydb
        conn: connection to sparkifydb
    
    Returns:
        Nothing
    """
    try:
        for query in create_table_queries:
            cur.execute(query)
            conn.commit()
    except psycopg2.Error as e:
        print("Error: Unable to create tables - sparkifydb")
        print(e)

def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()