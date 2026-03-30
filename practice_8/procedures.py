import psycopg2
from config import load_config

def deploy(conn, file):
    with open(file, 'r') as f:
        sql_script = f.read()
    with conn.cursor() as cur:
        cur.execute(sql_script)
        
def ins_contact(name, phone):
    params = load_config()
    
    conn = None
    try:
        conn = psycopg2.connect(**params)
        with conn.cursor() as cur:
            cur.execute('CALL ins_contact(%s, %s)', (name, phone))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

def ins_contacts(contact_list):
    params = load_config()
    
    names = [c[0] for c in contact_list]
    phones = [c[1] for c in contact_list]
    
    conn = None
    try:
        conn = psycopg2.connect(**params)
        deploy(conn, 'procedures.sql')
        
        with conn.cursor() as cur:
            cur.execute('CALL ins_contacts(%s, %s, %s)', (names, phones, []))
            
            errors = cur.fetchone()[0]
            
            if errors:
                for err in errors:
                    print(err)
            else:
                print("Added")
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
    
def del_contact(name=None, phone=None):
    params = load_config()
    conn = None
    try:
        conn = psycopg2.connect(**params)
        with conn.cursor() as cur:
            cur.execute('CALL del_contact(%s, %s)', (name, phone))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
            

if __name__ == '__main__':
    contacts = [('Alex', '+7993463556'),
                ('Rim', '+48 090908'),
                ('Masha', '56546')]
    
    ins_contacts(contacts)
    ins_contact('Roma', '+7098090906')
    
    del_contact(name='Rim')
    