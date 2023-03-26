class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(f"Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Current balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. Current balance: {self.balance}")

    def transfer_money(self, amount, recipient, pin):
        if self.pin != pin:
            print("Incorrect PIN")
            return False
        if amount > self.balance:
            print("Insufficient funds")
            return False
        self.balance -= amount
        recipient.balance += amount
        print("Transfer successful")
        return True

    def request_money(self, amount, recipient, recipient_pin, password):
        if recipient.pin != recipient_pin:
            print("Incorrect recipient PIN")
            return False
        if self.password != password:
            print("Incorrect password")
            return False
        if amount > recipient.balance:
            print("Recipient has insufficient funds")
            return False
        recipient.balance -= amount
        self.balance += amount
        print("Request successful")
        return True


""" Driver Code for Task 1 """
bob = User("Bob", 1234, "password")
print(f"Name: {bob.name}\nPIN: {bob.pin}\nPassword: {bob.password}")

""" Driver Code for Task 2 """
alice = BankUser("Alice", 5678, "password123")
print(f"Name: {alice.name}\nPIN: {alice.pin}\nPassword: {alice.password}\nBalance: {alice.balance}")
alice.name = "Alice Johnson"
alice.pin = 4321
alice.password = "newpassword"
print(f"Name: {alice.name}\nPIN: {alice.pin}\nPassword: {alice.password}\nBalance: {alice.balance}")


""" Driver Code for Task 3"""
john = BankUser("John", 9876, "password456")
print(f"Name: {john.name}\nPIN: {john.pin}\nPassword: {john.password}\nBalance: {john.balance}")

""" Driver Code for Task 4"""
eve = BankUser("Eve", 2468, "password789")
eve.show_balance()
eve.deposit(500)
eve.show_balance()
eve.withdraw(200)
eve.show_balance()

""" Driver Code for Task 5"""
mary = BankUser("Mary", 1357, "passwordabc")
jane = BankUser("Jane", 579, "passworddef")