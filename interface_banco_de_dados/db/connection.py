import psycopg2 #pip install psycopg2-binary

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="",
        user="",
        password=""
    )