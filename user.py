# user.py

class User:
    def __init__(self, user_id, password):
        self.id = user_id
        self.password = password

    def check_password(self, database):
        query = f"SELECT password FROM data WHERE id = {self.id}"
        database.execute_query(query)
        x = database.fetch_one()

        if x is not None:
            database_password = x[0]
            return database_password == self.password

        return False

    def get_info(self, database):
        query = f"SELECT id, password, Name, Account_Balance, Phone_no FROM data WHERE id = {self.id}"
        database.execute_query(query)
        return database.fetch_one()

    def update_name(self, database, new_name):
        update_query = f"UPDATE data SET Name = '{new_name}' WHERE id = {self.id}"
        database.execute_query(update_query)
        database.commit()

    def update_phone_no(self, database, new_phone_no):
        update_query = f"UPDATE data SET Phone_no = '{new_phone_no}' WHERE id = {self.id}"
        database.execute_query(update_query)
        database.commit()

    def update_password(self, database, new_password):
        update_query = f"UPDATE data SET password = '{new_password}' WHERE id = {self.id}"
        database.execute_query(update_query)
        database.commit()

    def deposit_money(self, database, amount):
        if amount >= 0:
            select_query = f"SELECT Account_Balance FROM data WHERE id = {self.id}"
            database.execute_query(select_query)
            x = database.fetch_one()
            balance = x[0]
            balance += amount
            update_query = f"UPDATE data SET Account_Balance = '{balance}' WHERE id = {self.id}"
            database.execute_query(update_query)
            database.commit()
            return balance

    def withdraw_money(self, database, amount):
        select_query = f"SELECT Account_Balance FROM data WHERE id = {self.id}"
        database.execute_query(select_query)
        x = database.fetch_one()
        balance = x[0]

        if amount <= balance and amount > 0:
            balance -= amount
            update_query = f"UPDATE data SET Account_Balance = '{balance}' WHERE id = {self.id}"
            database.execute_query(update_query)
            database.commit()
            return balance

        return None
