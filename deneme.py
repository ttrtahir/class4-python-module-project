class Atm:
    def __init__(self, account_list):
        self.account_list = account_list
        self.loop()

    def open_a_bank_account(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        self.account_list.append( Account(name, password) )

    def login(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        for obj in self.account_list:
            if obj.name == name and obj.password == password:
                is_del = obj.loop(account_list)
                if is_del == True:
                    account_list.remove(obj)

    def loop(self):
        while(1):
            temp = input("""Welcome:
            1) Open a bank account
            2) Login
            3) Exit""")

            if temp == '1':
                self.open_a_bank_account()
            elif temp == '2':
                self.login()
            elif temp == '3':
                return 0
            else:
                pass

class Account:
    def __init__(self, name, password, balance):
        self.name = name
        self.password = password
        self.balance = balance

    def withdraw(self):
        amount = int(input("Set the amount: "))
        self.balance -= amount

    def deposit(self):
        amount = int(input("Set the amount: "))
        self.balance = str(int(self.balance) + amount)

    def get_balance(self):
        print(self.balance)

    def transfer(self):   ###need fix
        name = input("Who would you like to transfer to: ")
        amount = int(input("Set the amount: "))

        for obj in self.account_list:
            if obj.name == name:
                self.balance = str(int(self.balance) - amount)
                obj.balance = str(int(obj.balance) + amount)
                return


    def change_account_information(self):
        name = input("Enter your new name: ")
        password = input("Enter your new password: ")
        self.name = name
        self.password = password

    def loop(self, account_list):
        self.account_list = account_list
        while(1):
            temp = input("""This is your account:
            1) withdraw
            2) deposit
            3) get balance
            4) transfer money
            5) change account information
            6) delete account
            7) return to main menu""")
            if temp == '1':
                self.withdraw()
            elif temp == '2':
                self.deposit()
            elif temp == '3':
                self.get_balance()
            elif temp == '4':
                self.transfer()
            elif temp == '5':
                self.change_account_information()
            elif temp == '6':
                return 1
            elif temp == '7':
                return 0

def set_account_list(account_file):
    account_list = []
    for lines in account_file.readlines():
        account_data = lines.split(",")     #name pass balance
        account_list.append( Account(account_data[0], account_data[1], account_data[2][:-1]) ) #"\n"
    return account_list

def end_account_file(account_file, account_list):
    account_file.seek(0)
    for i in account_list:
        account_file.write(f"{i.name},{i.password},{i.balance}\n")


if __name__ == "__main__":
    with open("./accounts.txt", "r+") as account_file:
        account_list = set_account_list(account_file)
    Atm(account_list)
    with open("./accounts.txt", "w+") as account_file:
        end_account_file(account_file, account_list)

















