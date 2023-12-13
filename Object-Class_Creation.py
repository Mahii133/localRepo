class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            print("Hello, how would you like to proceed?")
            print("1. Enter 1 to create pin")
            print("2. Enter 2 to deposit")
            print("3. Enter 3 to withdraw")
            print("4. Enter 4 to check balance")
            print("5. Enter 5 to exit")

            user_input = input("Enter your choice: ")

            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Thank you for using the ATM. Goodbye!")
                break  # Exit the loop and end the program
            else:
                print("Invalid input. Please enter a valid option.")

    def create_pin(self):
        self.pin = input("Enter your new PIN: ")
        print("PIN created successfully.")

    def deposit(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            amount = int(input("Enter the amount to deposit: "))
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Invalid PIN.")

    def withdraw(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            amount = int(input("Enter the amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Incorrect PIN.")

    def check_balance(self):
        temp = input("Enter your PIN: ")
        if temp == self.pin:
            print(f"Your balance is: {self.balance}")
        else:
            print("Invalid PIN.")

# Creating an instance of the ATM class
sbi_atm = Atm()
