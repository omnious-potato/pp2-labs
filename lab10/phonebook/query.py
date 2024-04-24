import psycopg2
from config import load_config

def get_students():
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT student_ID, student_name, student_phone, enroll_year FROM students ORDER BY student_name")
                print("The number of students: ", cur.rowcount)
                rows = cur.fetchall()

                for row in rows:
                    print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    get_students()