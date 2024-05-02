CREATE OR REPLACE FUNCTION paginated_query(
    page_limit INTEGER, 
    page_offset INTEGER
)
RETURNS TABLE(student_id UUID, student_name VARCHAR, student_phone VARCHAR, enroll_year INTEGER) AS
$$
BEGIN
    RETURN QUERY EXECUTE format(
        'SELECT student_id, student_name, student_phone, enroll_year FROM students LIMIT %s OFFSET %s',
        page_limit,
        page_limit * (page_offset - 1)
    );
END;
$$
LANGUAGE plpgsql;