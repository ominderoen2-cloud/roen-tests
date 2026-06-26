import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()
def connect_db():
    return psycopg2.connect(os.getenv("DATABASE_URL") , sslmode = "require")
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS enneclub (id text PRIMARY KEY , name TEXT , credit INTEGER)""")
    conn.commit()
    conn.close()
def add_member(member_id ,name, credit_score):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO enneclub (  id , name , credit) VALUES (%s,%s,%s)" ,( member_id ,name , credit_score))
        conn.commit()
        return True
    except psycopg2.IntegrityError:
        return False

    
    finally :
        conn.close()
def get_all_members():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT  id , name , credit FROM enneclub")
    rows = cursor.fetchall()
    return[
        {"id":r[0] , "name":r[1] , "credit":r[2]}
        for r in rows
    ]
def update_member_data(name , credit_score , member_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE  enneclub SET name = %s , credit= %s  WHERE id = %s ", (name , credit_score ,member_id,))
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    return updated > 0
def delete_member(member_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM enneclub WHERE id = %s", (member_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    return deleted > 0
