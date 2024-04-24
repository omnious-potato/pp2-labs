import psycopg2
from config import load_config

def create_tables():
    #CREATE command for students table, where provided ID is primary key and everything is regular fields
    commands = (
        """
        CREATE TABLE  students (
            student_ID VARCHAR(32) PRIMARY KEY,
            student_name VARCHAR(255) NOT NULL,
            student_phone VARCHAR(12),
            enroll_year INTEGER NOT NULL
        )
        """,)
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()