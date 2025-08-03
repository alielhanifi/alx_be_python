# bank_account.py

class BankAccount:
    """
    A class to represent a simple bank account.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes the BankAccount with an optional starting balance.
        
        Args:
            initial_balance (float, optional): The starting balance. Defaults to 0.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if amount > 0:
            self.account_balance += amount
            print(f"Successfully deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deducts the amount from the balance if funds are sufficient.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Returns:
            bool: True if withdrawal was successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Successfully withdrew: ${amount:.2f}")
            return True
        else:
            print("Withdrawal failed: Insufficient funds.")
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")

# --- Example Usage ---
if __name__ == '__main__':
    # Create a new account with an initial balance of $1000
    my_account = BankAccount(1000)
    my_account.display_balance()  # Expected: Current Balance: $1000.00

    print("-" * 20)

    # Deposit $500
    my_account.deposit(500)
    my_account.display_balance()  # Expected: Current Balance: $1500.00

    print("-" * 20)

    # Withdraw $200 (successful)
    was_successful = my_account.withdraw(200)
    print(f"Withdrawal status: {was_successful}")
    my_account.display_balance()  # Expected: Current Balance: $1300.00

    print("-" * 20)

    # Attempt to withdraw $2000 (insufficient funds)
    was_successful = my_account.withdraw(2000)
    print(f"Withdrawal status: {was_successful}")
    my_account.display_balance()  # Expected: Current Balance: $1300.00