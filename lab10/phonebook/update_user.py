import psycopg2
import sys
from config import load_config


def update_student(studentID, name=None, phone=None):
    #update student name/phone based on ID 
    
    updated_row_count = 0

    if name == None and phone == None:
        return 0
    if name == None:
        qualifier = phone
        sql = """ UPDATE students
                SET student_phone = %s
                WHERE student_ID = %s"""
    else:  
        qualifier = name
        sql = """ UPDATE students
                SET student_name = %s
                WHERE student_ID = %s"""
    
    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                
                # execute the UPDATE statement
                cur.execute(sql, (qualifier, studentID))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count

if __name__ == '__main__':
    print("Syntax: ./update_user.py <ID> [--name|--phone] <value>")
    if len(sys.argv) < 3:
        sys.exit()
    if sys.argv[2] == "--name":
        print(update_student(sys.argv[1], name=sys.argv[3]))
    if sys.argv[2] == "--phone":
        print(f"Updated {update_student(sys.argv[1], phone=sys.argv[3])} rows")