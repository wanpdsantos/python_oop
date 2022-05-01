### OPEN/CLOSE EXAMPLES ###
# Ex. 1 - BAD DESIGN - IF WE NEED TO INCLUDE NEW FILTERS, WE WILL NEED TO CHANGE THE CUSTOMER
# CLASS TO INSERT NEW METHODS FOR NEW FILTERS.
class Ex1Customer:
  def __init__(self, name, cpf, city):
    self._name = name
    self._cpf = cpf
    self._city = city

  def print_cpf(self):
    print(self.cpf)

  @property
  def cpf(self):
    return self._cpf
  
  @cpf.setter
  def cpf(self, cpf):
    if not cpf.isdecimal():
      raise Exception("CPF accept only numbers")
    if len(cpf) != 11:
      raise Exception("CPF must have 11 digits")
    self._cpf = cpf
  
  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, name):
    if not name.isalpha():
      raise Exception("Only letter is allowed for name.")
    self._name = name

  @property
  def city(self):
    return self._city

  @name.setter
  def city(self, city):
    if not city.isalpha():
      raise Exception("Only letter is allowed for city.")
    self._city = city

  @staticmethod
  def filter_by_name(customers, name):
    for customer in customers:
      if name in customer.name:
        yield customer
  
  @staticmethod
  def filter_by_cpf(customers, cpf):
    for customer in customers:
      if cpf in customer.name:
        yield customer

#BETTER DESIGN - In this next example, for new filters, it will required just to inherit from
# specification and declare new filter condition. Current classes will not change.
class Ex2Customer:
  def __init__(self, name, cpf, city):
    self._name = name
    self._cpf = cpf
    self._city = city

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, name):
    if not name.isalpha():
      raise Exception("Only letter is allowed for name.")
    self._name = name

  @property
  def cpf(self):
    return self._cpf
  
  @cpf.setter
  def cpf(self, cpf):
    if not cpf.isdecimal():
      raise Exception("CPF accept only numbers")
    if len(cpf) != 11:
      raise Exception("CPF must have 11 digits")
    self._cpf = cpf

  @property
  def city(self):
    return self._city

  @city.setter
  def city(self, city):
    if not city.isalpha():
      raise Exception("Only letter is allowed for city.")
    self._city = city

class Specification:
  def is_satisfied(self, customer):
    pass

class CustomerFilter:
  def filter(self, customers, specification):
    pass

class CitySpecification(Specification):
  def __init__(self, city):
    self.city = city

  def is_satisfied(self, element):
    return element.city == self.city

class ImprovedCustomerFilter(CustomerFilter):
  def filter(self, customers, specification):
    for customer in customers:
      if specification.is_satisfied(customer):
        yield customer

def test_case_1():
  customers_data = [
    {'name':'Andre', 'cpf': '11111111111', 'city': 'Salvador'},
    {'name':'Felipe', 'cpf': '22222222222', 'city': 'Salvador'},
    {'name':'Fernando', 'cpf': '33333333333', 'city': 'Salvador'},
  ]
  customers = [Ex2Customer(
    customer_data['name'],
    customer_data['cpf'],
    customer_data['city'] 
  ) for customer_data in customers_data]

  filter_customers = Ex1Customer.filter_by_name(customers, 'Fe')
  
  for filtered_customer in filter_customers:
    print(f'nome: {filtered_customer.name} - CPF: {filtered_customer.cpf}')

def test_case_2():
  customers_data = [
    {'name':'Andre', 'cpf': '11111111111', 'city': 'Salvador'},
    {'name':'Felipe', 'cpf': '22222222222', 'city': 'Salvador'},
    {'name':'Fernando', 'cpf': '33333333333', 'city': 'Salvador'},
  ]
  customers = [Ex2Customer(
    customer_data['name'],
    customer_data['cpf'],
    customer_data['city'] 
  ) for customer_data in customers_data]

  city_specifiction = CitySpecification('Salvador')
  filter_customers = ImprovedCustomerFilter()
  filter_customers = filter_customers.filter(customers, city_specifiction)
  
  for filtered_customer in filter_customers:
    print(f'nome: {filtered_customer.name} - CPF: {filtered_customer.cpf}')

def main():
  SELECTED_EXAMPLE = 'Ex2'
  EXAMPLES = {
    'Ex1': test_case_1,
    'Ex2': test_case_2,
  }
  return EXAMPLES[SELECTED_EXAMPLE]()

if __name__ == '__main__':
  main()
      