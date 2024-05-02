import psycopg2
from config import load_config
from connect import connect
from psycopg2 import Error

def insert_user(name, phone, year = None):
    """Call the insert_user procedure."""
    connection = None
    try:
        config = load_config()
        connection = connect(config)
        cursor = connection.cursor()
        
        cursor.execute("CALL insert_user(%s, %s, %s)", (name, phone, year))
        connection.commit()
    except Error as e:
        print("Error while inserting user:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    insert_user("Mark Rowen", "+7777228", "1999")
    insert_user("Mark Rowen", "+7777228", "1999")
    insert_user("Mark Gruen", "+49WAFFLING")
