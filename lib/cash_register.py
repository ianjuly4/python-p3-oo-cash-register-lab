#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0):
    self.total = total
    self.discount = discount
    self.items = []
    self.transactions = []


  @property
  def total(self):
    return self._total
  @property
  def discount(self):
    return self._discount
  
  @total.setter
  def total(self, total):
    self._total = total
  @discount.setter
  def discount(self, discount):
    self._discount = discount
  
  def add_item(self, title, price, quantity=1):
    transaction = (title, price, quantity)  # Store the transaction as a tuple
    self.transactions.append(transaction)  # Add the transaction to the list
    self.total += (price * quantity)
    self.items.extend([title] * quantity)

  def apply_discount(self):
    if self.discount > 0:
      discount = self.discount * 0.01
      discounted = discount * self.total
      discounted_total = self.total - discounted
      self.total = round(discounted_total)
      print(f"After the discount, the total comes to ${self.total}.")
      return discounted_total
    else:
      print("There is no discount to apply.")
  
  def items_list_without_multiples(self):
    items = []
    for item in self.items:
      title, _ = item  # We only need the title, ignoring the price
      if title not in items:
        items.append(title)
    return list(map(str, items))
  
  def items_list_with_multiples(self):
    items = []
    for item in self.items:
      title, _ = item  # We only need the title, ignoring the price
      items.append(title)  # Add the item title to the items list
    return list(map(str, items))
  
  def void_last_transaction(self):
    if self.transactions:
      last_transaction = self.transactions.pop()  # Remove last transaction from the transactions list
      _, price, quantity = last_transaction  # Unpack the transaction tuple
      self.total -= (price * quantity)  # Subtract the amount from the total
    else:
      print("No transactions to void.")
    
cash_register = CashRegister()
print(cash_register.apply_discount())
