
class BankAccount:
  def __init__(self):
    balance = int(input("Enter your current balance:\n"))
    self._balance = balance

  @property
  def balance(self):
    return self._balance

  @balance.setter
  def balance(self, new_balance):
    if new_balance < self._balance and new_balance > 0:
      raise ValueError("New balance can't be less than current balance.")
    elif new_balance == self._balance:
      raise ValueError("Value can't be same")
    elif new_balance == 0:
      raise ValueError("Value can't be zero")
    elif new_balance < 0:
      raise ValueError("Value can't be negative")

    self._balance = new_balance

a = BankAccount()
print(f"Current balance is: {a.balance}")

try:
  new_amount = int(input("Enter your new balance:\n"))
  a.balance = new_amount
  print(f"New balance is: {a.balance}")
except ValueError as e:
  print(f"Error: {e}")
