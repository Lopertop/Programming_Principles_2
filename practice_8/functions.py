import psycopg2
from config import load_config

def sync_funcs(cur, file):
    with open(file, 'r') as f:
        cur.execute(f.read())

def get_data(pattern=None, pagination=False):
    params = load_config()
    data = []
    
    conn = None
    try:
        conn = psycopg2.connect(**params)
        with conn.cursor() as cur:
            sync_funcs(cur, 'functions.sql')
            
            if pagination:
                cur.execute("SELECT * FROM get_with_pagination(4, 3);")
            else:
                cur.execute("SELECT * FROM get_contacts(%s);", (pattern,))
            
            data = cur.fetchall()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
    return data

if __name__ == '__main__':
    res = get_data(pattern='67')
    print(res)
    
    pag_data = get_data(pagination=True)
    print(pag_data)                          
