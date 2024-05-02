-- Add new user into students table
CREATE OR REPLACE PROCEDURE insert_user(
    student_name VARCHAR,
    student_phone VARCHAR,
    enroll_year INTEGER
)
RETURNS VOID
AS $$
DECLARE
    current_year INTEGER;
    current_month INTEGER;
    study_year INTEGER;
BEGIN
    SELECT EXTRACT(YEAR FROM CURRENT_DATE) INTO current_year;
    SELECT EXTRACT(MONTH FROM CURRENT_DATE) INTO current_month;

    IF current_month < 9 THEN 
        study_year := current_year - 1;
    ELSE 
        study_year := current_year;
    END IF;

    IF enroll_year IS NULL
        enroll_year := study_year
    END IF;

    INSERT INTO students(student_name, student_phone, enroll_year)
    VALUES (student_name, student_phone, enroll_year)
    ON CONFLICT (student_name, enroll_year) DO UPDATE
    SET student_phone = EXCLUDED.student_phone;


    IF FOUND THEN 
        RAISE NOTICE 'User has been added/updated!';
    ELSE 
        RAISE NOTICE 'Insert/update has failed!';
    END IF;
END;
$$
LANGUAGE plpgsql;