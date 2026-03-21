import psycopg2
from config import load_config
import csv

def insert_contact(name, phone_number):
    sql ="""
    WITH ins_phone AS (
        INSERT INTO phone_numbers (phone_number)
        VALUES (%s)
        ON CONFLICT (phone_number) DO UPDATE SET phone_number = EXCLUDED.phone_number
        RETURNING phone_id
    )
    INSERT INTO contact_name (phone_id, name)
    SELECT phone_id, %s FROM ins_phone
    ON CONFLICT (phone_id) DO UPDATE SET name = EXCLUDED.name;
    """
    
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (phone_number, name))
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
def insert_from_csv(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    insert_contact(row[0].strip(), row[1].strip())
    except FileNotFoundError as error:
        print(error)
    
if __name__ == '__main__':
    insert_contact("Aleksey", "+7(999) 001-11-34")
    
    insert_from_csv('data.csv')