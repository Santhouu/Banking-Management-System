class BankAccount:
    """Class to handle bank account operations."""
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    # deposit method 
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        self.save()
        print(f"Deposited {amount}. Current balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        self.save()
        print(f"Withdrew {amount}. Current balance: {self.balance}")
    
    def save(self):
        """Save account details to file."""
        with open("account.txt", "w") as f:
            f.write(f"{self.account_number},{self.name},{self.balance}")
    
    @classmethod
    def load(cls):
        """Load account details from file."""
        try:
            with open("account.txt", "r") as f:
                data = f.readline().strip().split(",")
                return cls(data[0], data[1], float(data[2]))

        except FileNotFoundError:
            return None


def main():
    """Main function to execute banking operations."""
    account = BankAccount.load()
    if not account:
        account_number = input("Enter account number to create: ")
        name = input("Enter account holder's name: ")
        account = BankAccount(account_number, name, 0)
        account.save()
        print("Account successfully created.")
    else:
        print(f"Welcome back, {account.name}!")

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            try:
                account.deposit(amount)
            except ValueError as e:
                print(e)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            try:
                account.withdraw(amount)
            except ValueError as e:
                print(e)

        elif choice == "3":
            print(f"Current balance: {account.balance}")

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
