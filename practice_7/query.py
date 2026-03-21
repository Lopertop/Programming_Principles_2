import psycopg2
from config import load_config

# fetchone() function
def get_contacts():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT phone_id, name FROM contact_name ORDER BY name")
                print("The number of rows: ", cur.rowcount)
                row = cur.fetchone()
                
                while row is not None:
                    print(row)
                    row = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
# fetchall() function
def get_kz_ru_phone_numbers():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT phone_id, phone_number FROM phone_numbers WHERE phone_number LIKE '+7%'")
                rows = cur.fetchall()
                print("The number of rows: ", cur.rowcount)
                for row in rows:
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
# fetchmany() function
def iter_row(cursor, size=2):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def get_numbers_of_two_people():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT name, phone_number
                    FROM contact_name
                    INNER JOIN phone_numbers
                    ON contact_name.phone_id = phone_numbers.phone_id
                    ORDER BY name      
                    """)
                for row in iter_row(cur, 2):
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
if __name__ == '__main__':
    get_numbers_of_two_people()
    