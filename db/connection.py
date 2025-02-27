import os

from testcontainers.mongodb import MongoDbContainer

mongo = MongoDbContainer("mongo:7.0.17-jammy")

class Connection:
    def __init__(self):
        self.setup()

    def setup(self):
        mongo.start()

    def get_connection(self):
        return mongo.get_connection_client().test