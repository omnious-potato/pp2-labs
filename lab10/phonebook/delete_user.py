import psycopg2
import sys
from config import load_config


def delete_student(name=None, phone=None):
    #update student name/phone based on ID 
    
    deleted_row_count = 0

    if name == None and phone == None:
        return 0
    if name == None:
        qualifier = phone
        sql = """ DELETE FROM students
                WHERE student_phone = %s"""
    else:  
        qualifier = name
        sql = """ DELETE FROM students
                WHERE student_name = %s"""
    
    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                
                # execute the UPDATE statement
                cur.execute(sql, (qualifier,))
                deleted_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return deleted_row_count

if __name__ == '__main__':
    print("Syntax: ./delete_user.py [--name|--phone] <value>")
    if len(sys.argv) < 3:
        sys.exit()
    if sys.argv[1] == "--name":
        print(f"Updated {delete_student(name=sys.argv[2])} rows")
    if sys.argv[1] == "--phone":
        print(f"Updated {delete_student(phone=sys.argv[2])} rows")