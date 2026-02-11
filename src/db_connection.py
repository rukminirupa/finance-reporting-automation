import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="finance_db",
        user="sampathchiluka",
        password=""
    )
    return conn