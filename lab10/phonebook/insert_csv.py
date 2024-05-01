import psycopg2
import os, sys
import csv
from config import load_config



def csv_to_list(csv_path):
    #converting csv data to python list, this assumes that csv file is already in corresponding column sstructure 
    data = []
    with open(csv_path, 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader, None) # skip header
        for row in csv_reader:
            data.append(row)

    return data

def insert_students_csv(student_list):
    sql = """INSERT INTO students(student_name, student_phone, enroll_year)
             VALUES(%s, %s, %s) RETURNING *"""
    config = load_config()
    rows = []

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the INSERT statement
                cur.executemany(sql, student_list)

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return rows


if __name__ == '__main__':
    print(len(sys.argv))
    if len(sys.argv) == 1:
        print("Assuming default \"students.csv\" is present for import")

        data = csv_to_list("./students.csv")
        insert_students_csv(data)
    else:
        
        if os.path.exists(sys.argv[1]):
            data = csv_to_list(str(sys.argv[1]))
        else:
            print("No such file")
            sys.exit()
        
        insert_students_csv(data)