import time

from db.connection import Connection
from app.customers import Customer

connection = Connection()
conn = connection.get_connection()

class Store:

    def create_customer(self, name, email):
        conn.customers.insert_one({"name": name, "email": email})

    def get_all_customers(self) -> list[Customer]:
        time.sleep(60 * 3)
        res = conn.customers.find()
        # print(res[])
        return [Customer(cid, name, email) for cid, name, email in conn]