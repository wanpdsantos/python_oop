### SINGLE RESPONSABILITY EXAMPLES ###
# Ex. 1 - BAD DESIGN
class Payment:
  def __init__(self, user, total_value, items):
    self.user = user
    self.total_value = total_value
    self.items = items

  def checkout(self):
    print('process payment')
    return
  
  def update_stock(self):
    print('update stock items')
    return

  def send_confirmation_email(self):
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
    self.items_sold = sell.items_sold
  
  def update_stock(self):
    print(f'Items to remove from stock: {self.items_sold}')
    return

class PaymentManager:
  def __init__(self, sell):
    self.customer = sell.customer
    self.total_value = sell.total_value

  def checkout(self):
    print(f'Process payment for user: {self.customer}')
    return

class NotificationManager:
  def __init__(self, sell):
    self.customer = sell.customer
    self.total_value = sell.total_value
    self.items = sell.items_sold
  
  def send_confirmation_email(self):
    print('send email notification')
    return

### TEST FUNCTIONS ###
def test_ex_1_case_1():
  new_sell = Sell(1155, 10.50, [{'4940291':2, '204931':3}])
  PaymentManager(new_sell).checkout()
  StockManager(new_sell).update_stock()
  NotificationManager(new_sell).send_confirmation_email()
  return

def test_ex_1_case_2():
  new_sell = Sell(2291, 20.50, [{'4940291':10, '204931':20}])
  PaymentManager(new_sell).checkout()
  StockManager(new_sell).update_stock()
  NotificationManager(new_sell).send_confirmation_email()
  return

def main():
  SELECTED_EXAMPLE = 'Ex2'
  EXAMPLES = {
    'Ex1': test_ex_1_case_1,
    'Ex2': test_ex_1_case_2
  }
  return EXAMPLES[SELECTED_EXAMPLE]()

if __name__ == '__main__':
  main()