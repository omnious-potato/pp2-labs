import psycopg2
import sys
from config import load_config


def insert_student(student_ID, student_name, student_phone, enroll_year):
    #insert one row (one student respectively)

    sql = """INSERT INTO students(student_ID, student_name, student_phone, enroll_year)
             VALUES(%s, %s, %s, %s) RETURNING student_ID;"""
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (student_ID, student_name, student_phone, enroll_year,))

                # get the generated id back                
                rows = cur.fetchone()
                if rows:
                    student_ID = rows[0]

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return student_ID

if __name__ == '__main__':
    print(len(sys.argv))
    if len(sys.argv) == 1:
        print("Insufficient arguments! Use \"--help\".")
        sys.exit()
    if sys.argv[1] == "--help":
        print("This program inserts one entry to \"students\" table.\nPrimary key - student ID\nSecondary fields - name, phone, enroll year")
        sys.exit()
    if sys.argv[1] == "--test":
        insert_student("23Bbruh001", "Zhmyshenko Valeriy Albertovich", "+777228ABOBA", "2018")
    else:
        insert_student(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])