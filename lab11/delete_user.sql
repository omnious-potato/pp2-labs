CREATE OR REPLACE PROCEDURE delete_user(
    u_name VARCHAR DEFAULT NULL,
    u_phone VARCHAR DEFAULT NULL
)
AS $$
DECLARE
    rc INTEGER;
BEGIN
    DELETE FROM students
    WHERE (student_name = u_name AND u_phone IS NULL) 
    OR (student_phone = u_phone AND u_name IS NULL) 
    OR (student_name = u_name AND student_phone = u_phone);

    GET DIAGNOSTICS rc = ROW_COUNT;
    RAISE NOTICE 'Found % entries.', rc;

    IF rc > 1 THEN
        ROLLBACK;
    END IF;
END;
$$
LANGUAGE plpgsql;