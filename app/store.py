# import time

from db.connection import get_connection
from app.customers import Customer

class Store:
    def create_table(self):
        print("Getting connection")
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE customers (
                        id serial PRIMARY KEY,
                        name varchar not null,
                        email varchar not null unique)
                    """)
                conn.commit()

    def create_customer(self, name, email):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO customers (name, email) VALUES (%s, %s)", (name, email))
                conn.commit()


    def get_all_customers(self) -> list[Customer]:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers")
                # time.sleep(60)
                return [Customer(cid, name, email) for cid, name, email in cur]


    def get_customer_by_email(email) -> Customer:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, name, email FROM customers WHERE email = %s", (email,))
                (cid, name, email) = cur.fetchone()
                return Customer(cid, name, email)


    def delete_all_customers():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM customers")
                conn.commit()