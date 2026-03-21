import psycopg2
from config import load_config

def delete_by_name(name):
    config = load_config()
    sql = "DELETE FROM contact_name WHERE name = %s"
    
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name,))
                
                rows_deleted = cur.rowcount
                print("Successfully deleted: ", rows_deleted)
                
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
if __name__ == '__main__':
    delete_by_name('John Wick')
