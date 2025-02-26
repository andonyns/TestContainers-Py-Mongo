class Customer:
    def __init__(self, cust_id, name, email):
        self.id = cust_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"Customer : {self.id}, Name: {self.name}, Email:{self.email}"

    def __repr__(self):
        return str(self)