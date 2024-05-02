CREATE OR REPLACE PROCEDURE insert_user(
    u_name VARCHAR,
    u_phone VARCHAR,
    u_year INTEGER
)
AS $$
DECLARE
    current_year INTEGER;
    current_month INTEGER;
    study_year INTEGER;
    count INTEGER;
BEGIN
    SELECT EXTRACT(YEAR FROM CURRENT_DATE) INTO current_year;
    SELECT EXTRACT(MONTH FROM CURRENT_DATE) INTO current_month;

    IF current_month < 9 THEN 
        study_year := current_year - 1;
    ELSE 
        study_year := current_year;
    END IF;

    IF u_year IS NULL THEN
        u_year := study_year;
    END IF;


    SELECT COUNT(*) INTO count
    FROM students
    WHERE student_name = u_name AND enroll_year = u_year;
    
    RAISE NOTICE 'count of entries: %', count;

    
    IF count = 0 THEN   
        --New entry
        INSERT INTO students(student_name, student_phone, enroll_year)
        VALUES (u_name, u_phone, u_year);
    ELSE 
        IF count = 1 THEN
            --Existing row
            UPDATE students
            SET student_phone = u_phone
            WHERE student_name = u_name AND enroll_year = u_year;
        ELSE
            RAISE NOTICE 'Table contains duplicate/ambigious entries!';
        END IF;
    END IF;

    IF FOUND THEN 
        RAISE NOTICE 'User has been added/updated!';
    ELSE 
        RAISE NOTICE 'Insert/update has failed!';
    END IF;
END;
$$
LANGUAGE plpgsql;