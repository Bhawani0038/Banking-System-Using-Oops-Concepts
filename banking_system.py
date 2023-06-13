# banking_system.py

from database import Database
from user import User

class BankingSystem:
    def __init__(self):
        self.database = Database()

    def login(self):
        user_id = input("User ID: ")
        password = input("Password: ")
        user = User(user_id, password)

        if user.check_password(self.database):
            self.user_menu(user)
        else:
            print("Wrong Password")

    def signup(self):
        name = input("Name: ")
        password = input("Set Password: ")
        phone_no = int(input("Phone No: "))

        choice = input('''
        1: Deposit Money now
        2: Set Zero Balance
        ''')

        if choice == "1":
            balance = self.deposit_money_into_new_account()
        elif choice == "2":
            balance = 0
        else:
            print("Invalid Choice")
            return

        insert_query = "INSERT INTO data(password, Name, Account_Balance, Phone_no) values(%s,%s,%s,%s)"
        values = (password, name, balance, phone_no)
        self.database.execute_query(insert_query, values)
        self.database.commit()

        select_query = f"SELECT id FROM data WHERE Name='{name}' and password='{password}'"
        self.database.execute_query(select_query)
        x = self.database.fetch_one()
        id = x[0]
        print(f"Your Generated ID is: {id}")

    def user_menu(self, user):
        while True:
            choice = input('''
            1: Check Balance
            2: Update Your Info
            3: Withdraw Money
            4: Deposit Money
            5: See Info
            6: Exit
            ''')

            if choice == "1":
                self.check_balance(user)
            elif choice == "2":
                self.update_user_info(user)
            elif choice == "3":
                self.withdraw_money(user)
            elif choice == "4":
                self.deposit_money(user)
            elif choice == "5":
                self.see_info(user)
            elif choice == "6":
                break
            else:
                print("Wrong Selection")

    def deposit_money_into_new_account(self):
        balance = eval(input("How much money to deposit: "))
        return balance

    def check_balance(self, user):
        query = f"SELECT Account_Balance FROM data WHERE id = {user.id}"
        self.database.execute_query(query)
        x = self.database.fetch_one()
        print(f"Current Balance: {x[0]}")

    def withdraw_money(self, user):
        try:
            amount = eval(input("How much money to withdraw: "))
            balance = user.withdraw_money(self.database, amount)

            if balance is not None:
                print(f"Money Withdrawn Successfully\nAvailable Balance: {balance}")
            else:
                print("Insufficient Balance")
        except:
            print("Amount should be a numerical +ve value")

    def deposit_money(self, user):
        try:
            amount = eval(input("How much money to deposit: "))
            balance = user.deposit_money(self.database, amount)

            if balance is not None:
                print(f"Money Deposited Successfully\nAvailable Balance: {balance}")
        except:
            print("Amount should be a positive numerical value")

    def update_user_info(self, user):
        user_info = user.get_info(self.database)

        print(f'''
        Id        : {user_info[0]}
        Name      : {user_info[2]}
        Phone No  : {user_info[4]}
        Balance   : {user_info[3]}
        Password  : {user_info[1]}
        ''')

        while True:
            choice = input('''
            1: Modify Name
            2: Modify Phone Number
            3: Modify Password
            4: Exit
            ''')

            if choice == "1":
                new_name = input("Enter new name: ")
                user.update_name(self.database, new_name)
                print("Name updated")
            elif choice == "2":
                new_phone_no = input("Enter new phone number: ")
                user.update_phone_no(self.database, new_phone_no)
                print("Phone number updated")
            elif choice == "3":
                new_password = input("Enter new password: ")
                user.update_password(self.database, new_password)
                print("Password updated")
            elif choice == "4":
                break

    def see_info(self, user):
        user_info = user.get_info(self.database)

        print(f'''
        Id        : {user_info[0]}
        Name      : {user_info[2]}
        Phone No  : {user_info[4]}
        Balance   : {user_info[3]}
        Password  : {user_info[1]}
        ''')

    def run(self):
        while True:
            try:
                choice = eval(input('''
                1: Existing User
                2: New User
                3: Exit
                '''))
            except:
                print("Invalid Data")

            if choice == 1:
                self.login()
            elif choice == 2:
                self.signup()
            elif choice == 3:
                self.database.close_connection()
                break
            else:
                print("Invalid Choice")
if __name__ == "__main__":
    banking_system = BankingSystem()
    banking_system.run()
