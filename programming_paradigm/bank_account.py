#!/usr/bin/python3
"""
This module defines the BankAccount class.
"""

class BankAccount:
    """A class to represent a simple bank account."""

    def __init__(self, initial_balance=0):
        """
        Initializes the BankAccount.

        Args:
            initial_balance (float, optional): The starting balance. Defaults to 0.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Adds a positive amount to the account balance.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """
        Deducts a positive amount from the balance if funds are sufficient.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if withdrawal was successful, False otherwise.
        """
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")