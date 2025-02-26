import os

from testcontainers.postgres import PostgresContainer

postgres = PostgresContainer("postgres:16-alpine")

class Setup_DB:
    def __init__(self):
        self.setup()

    def setup(self):
        postgres.start()
        os.environ["DB_CONN"] = postgres.get_connection_url()
        os.environ["DB_HOST"] = postgres.get_container_host_ip()
        os.environ["DB_PORT"] = postgres.get_exposed_port(5432)
        os.environ["DB_USERNAME"] = postgres.username
        os.environ["DB_PASSWORD"] = postgres.password
        os.environ["DB_NAME"] = postgres.dbname
        print(f"{postgres.username} - {postgres.password} - {os.environ["DB_PORT"]}")

    def teardown(self):
        postgres.stop()