import sqlite3
import pandas as pd

def create_connection():
    conn = sqlite3.connect("petrol_sales.db")
    return conn

def load_data_to_db(df):
    conn = create_connection()
    df.to_sql("sales_data", conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()

def run_query(query):
    conn = create_connection()
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result
