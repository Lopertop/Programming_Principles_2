import psycopg2
from config import load_config

def create_tables():
    commands = (
        """
        CREATE TABLE phone_numbers (
            phone_id SERIAL PRIMARY KEY,
            phone_number VARCHAR(100) NOT NULL
        )
        """,
        """
        CREATE TABLE contact_name (
            phone_id INTEGER PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            FOREIGN KEY (phone_id)
            REFERENCES phone_numbers (phone_id)
            ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
    )

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()
