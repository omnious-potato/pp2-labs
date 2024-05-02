import psycopg2
from config import load_config
from connect import connect
from psycopg2 import Error

def delete_user(name=None, phone=None):
    if name == None and phone == None:
        return
    """Call the insert_user procedure."""
    connection = None
    try:
        config = load_config()
        connection = connect(config)
        cursor = connection.cursor()
        
        if name == None:
            cursor.execute("CALL delete_user(NULL, %s)", (phone,))
        else:
            cursor.execute("CALL delete_user(%s, NULL)", (name,))
    
        connection.commit()
    except Error as e:
        print("Error while deleting user:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    delete_user('Mark Gruen')
    delete_user(None, '+7777228')
