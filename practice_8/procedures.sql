CREATE OR REPLACE PROCEDURE ins_contact(c_name text, c_phone text)
LANGUAGE plpgsql
AS $$
DECLARE
    r_id INT;
BEGIN
    SELECT phone_id INTO r_id FROM contact_name WHERE name = c_name;

    IF r_id IS NOT NULL THEN
        UPDATE phone_numbers
        SET phone_number = c_phone
        WHERE phone_id = r_id;
    ELSE
        INSERT INTO phone_numbers (phone_number)
        VALUES (c_phone)
        RETURNING phone_id INTO r_id;

        INSERT INTO contact_name (phone_id, name)
        VALUES (r_id, c_name);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE ins_contacts(IN names text[], IN phones text[],
INOUT incorrect_data text[] DEFAULT ARRAY[]::text[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
    r_id INT;
BEGIN
    FOR i IN 1 .. array_upper(names, 1) LOOP
        IF phones[i] !~ '^\+' THEN
            incorrect_data := array_append(incorrect_data, names[i] || ': ' || phones[i]);
            CONTINUE;
        END IF;

        CALL ins_contact(names[i], phones[i]);
    END LOOP;
END;
$$;

CREATE OR REPLACE PROCEDURE del_contact(c_name text DEFAULT NULL, c_phone text DEFAULT NULL)
LANGUAGE plpgsql
AS $$
DECLARE
    r_id INT;
BEGIN
    IF c_name IS NOT NULL THEN
        SELECT phone_id INTO r_id FROM contact_name WHERE name = c_name;
    ELSIF c_phone IS NOT NULL THEN
        SELECT phones_id INTO r_id FROM phone_numbers WHERE phone_number = c_phone;
    END IF;

    IF r_id IS NOT NULL THEN
        DELETE FROM contact_name WHERE phone_id = r_id;
        DELETE FROM phone_numbers WHERE phone_id = r_id;
    END IF;
END;
$$;