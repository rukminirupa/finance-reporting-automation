import pandas as pd
from src.db_connection import get_connection

def extract_transactions():
    print("Connecting to database...")
    conn = get_connection()
    query = "SELECT * FROM transactions;"
    df = pd.read_sql(query, conn)
    conn.close()
    print("Data extracted successfully")
    return df