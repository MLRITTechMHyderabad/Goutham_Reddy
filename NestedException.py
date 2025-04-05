class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount < 0:
                raise ValueError("Amount cannot be negative")
            elif amount > self.balance:
                raise InsufficientFundsError("Insufficient funds")
            else:
                self.balance -= amount
                return f"Remaining balance: {self.balance}"
        except ValueError as ve:
            return f"Error: {ve}"
        except InsufficientFundsError as ie:
            return f"Error: {ie}"
        except Exception as e:
            return f"Error: {e}"

account = BankAccount(100)
print(account.withdraw(150))
print(account.withdraw(-10))
print(account.withdraw(50))
