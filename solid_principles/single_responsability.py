### SINGLE RESPONSABILITY 
# Ex. 1 - BAD DESIGN
class Payment:
  def __init__(self, user, total_value, items):
    self.user = user
    self.total_value = total_value
    self.items = items

  def checkout():
    print('process payment')
    return
  
  def update_stock(self):
    print('update stock items')
    return

  def send_confirmation_email():
    print('send a confirmation email to the user')
    return 

# BETTER DESIGN
class Sell:
  def __init__(self, customer, total_value, items_sold):
    self.customer = customer
    self.total_value = total_value
    self.items_sold = items_sold
  
class StockManager:
  def __init__(self, sell):
    self.items = sell.items_sold
  
  def update_stock(self):
    print('update stock items')
    return

class PaymentManager:
  def __init__(self, sell):
    self.user = sell.user
    self.total_value = sell.total_value

  def checkout():
    print('process payment')
    return

class NotificationManager:
  def __init__(self, sell):
    self.user = sell.user
    self.total_value = sell.total_value
    self.items = sell.items_sold
  
  def send_confirmation_email(self):
    print('send email notification')
    return