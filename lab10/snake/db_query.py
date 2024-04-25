import psycopg2
import hashlib
from config import load_config


def check_user(username):
    query = """
        SELECT user_id FROM users
        WHERE username = %s
    """

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (username,))

                user = cur.fetchone()
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return user

def get_user(username, password):
    hashed_pass = hashlib.sha256(password.encode()).hexdigest()

    lookup_query = """
        SELECT * FROM users
        WHERE username = %s AND pass_hashed = %s
    """

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(lookup_query, (username, hashed_pass))

                user = cur.fetchone()
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return user
        

def add_user(username, password):

    hashed_pass = hashlib.sha256(password.encode()).hexdigest()

    insert_query = """
        INSERT INTO users (username, pass_hashed)
        VALUES (%s, %s) RETURNING *;
    """
    user = None
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(insert_query, (username, hashed_pass))
                
                user = cur.fetchone()
                
                conn.commit()
                

                

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return user

def get_required_scores(user_id):
    recent_game_stats_query = """
        SELECT TOP 1 score, level FROM   user_score
        WHERE user_id = %s
        ORDER BY date ASC
    """

    hi_score_query = """
        SELECT TOP 1 high_score FROM user_score
        WHERE user_id = %s
        ORDER BY high_score DESC
    """

def add_score(user_id, high_score, level, score):
    query = """
        INSERT INTO user_score(user_id, high_score, level, score)
        VALUES (%s, %s, %s, %s) RETURNING *
    """

    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(query, (user_id, high_score, level, score,))

                # get the generated id back                
                rows = cur.fetchone()
                if rows:
                    user_id = rows[0]

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return user_id