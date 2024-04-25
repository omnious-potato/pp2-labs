import psycopg2
from config import load_config

def create_tables():
    #CREATE command for students table, where provided ID is primary key and everything is regular fields
    commands = (
        """
        CREATE TABLE  users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            pass_hashed VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE  user_score (
            score_id SERIAL PRIMARY KEY, 
            user_id INTEGER REFERENCES users(user_id),
            high_score INTEGER,
            score INTEGER,
            level INTEGER,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
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