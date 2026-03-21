import psycopg2
from config import load_config

def update_contact_name(phone_id, contact_name):
    updated_row_count = 0
    
    sql = """
    UPDATE contact_name
        SET name = %s
        WHERE phone_id = %s
    """
    config = load_config()
    
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (contact_name, phone_id))
                updated_row_count = cur.rowcount
                
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return updated_row_count

if __name__ == '__main__':
    update_contact_name(1, "John Wick")