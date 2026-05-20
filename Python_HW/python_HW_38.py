class BankAccount:
    """
    A simple bank account class that supports deposits, withdrawals,
    balance validation, and transaction history tracking.

    Attributes:
        _owner_name (str):
            Name of the account owner.

        _history (list):
            Stores transaction history entries.

    Private Attributes:
        __current_balance (float | int):
            Current account balance.
    """
    def __init__(self, owner_name, current_balance):
        self._owner_name = owner_name
        self.__validate_balance(current_balance)
        self.__current_balance = current_balance
        self._history = []

    @property
    def name(self):
        """
        Get the account owner's name.

        Returns:
            str:
                The owner's name.
        """
        return self._owner_name

    @property
    def history(self):
        """
        Get a copy of the transaction history.

        Returns:
            list:
                A copy of the transaction history list.
        """
        return self._history.copy()

    @property
    def balance(self):
        """
        Get the current account balance.

        Returns:
            float | int:
                The current balance.
        """
        return self.__current_balance

    @balance.setter
    def balance(self, new_balance):
        """
        Set a new account balance after validation.

        Args:
            new_balance (float | int):
                The new balance value.

        Raises:
            ValueError:
                If the new balance is negative.
        """
        self.__validate_balance(new_balance)
        self.__current_balance = new_balance

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount (float | int):
                Amount to deposit. Must be positive.

        Raises:
            ValueError:
                If the deposit amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount
        self._history.append(f"\t\tWithdraw: {amount}\n"
                             f"\t\tCurrent balance: {self.balance}")

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Args:
            amount (float | int):
                Amount to withdraw. Must be positive and
                less than or equal to the current balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        # if amount > self.balance:
        #     raise ValueError("Insufficient funds.")

        self.balance -= amount
        self._history.append(f"\t\tWithdraw: {amount}\n"
                             f"\t\tCurrent balance: {self.balance}")

    @staticmethod
    def __validate_balance(balance):
        """
        Validate that a balance is non-negative.

        Args:
            balance (float | int):
                Balance value to validate.

        Raises:
            ValueError:
                If the balance is negative.
        """
        if balance < 0:
            raise ValueError("Insufficient funds. Balance must be positive, as do you.")

client = BankAccount("Barsik", 10)
print(client.balance)
print(client.name)

client.deposit(500)

print(client.balance)

client.withdraw(104)

print(client.balance)

print("Operating history:")
for operation in client.history:
    print(f"{operation}\n")

