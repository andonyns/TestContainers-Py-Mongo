import os
import sys
from typing import Any

from app.store import Store

class App:

    def run(self) -> int:
        print("DB Ready")
        store = Store()


        print("Inserting customer...")
        store.create_customer("Test", "user@mail.com")

        print("Inserting customer...")
        store.create_customer("Test 2", "user2@mail.com")

        print("Result:")
        
        print(store.get_all_customers())

        print("Cleaning up...")

        return 0


if __name__ == "__main__":
    app = App()
    
    sys.exit(app.run())
