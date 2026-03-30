CREATE OR REPLACE FUNCTION get_contacts(pattern text)
RETURNS TABLE(name VARCHAR, phone_number VARCHAR) AS
$$
BEGIN
    RETURN QUERY
    SELECT contact_name.name, phone_numbers.phone_number
    FROM contact_name
    INNER JOIN phone_numbers ON contact_name.phone_id = phone_numbers.phone_id
    WHERE contact_name.name ILIKE '%' || pattern || '%'
    OR phone_numbers.phone_number ILIKE '%' || pattern || '%';
END; $$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_with_pagination(p_limit int DEFAULT 4, p_offset int DEFAULT 3)
RETURNS TABLE(name VARCHAR, phone_number VARCHAR) AS
$$
BEGIN
    RETURN QUERY
    SELECT contact_name.name, phone_numbers.phone_number
    FROM contact_name
    INNER JOIN phone_numbers ON contact_name.phone_id = phone_numbers.phone_id
    LIMIT p_limit OFFSET p_offset;
END; $$
LANGUAGE plpgsql;