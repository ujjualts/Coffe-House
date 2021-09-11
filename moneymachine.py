class MoneyMachine:
  currency="$"
  COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
  def __init__(self):
    self.profit=0
    self.money_recieved=0
  
  def report(self):
    print(f'Money: {self.currency} {self.profit}')
  
  def process_coins(self):
    for coin in self.COIN_VALUES:
      self.money_recieved+=int(input(f'How many {coin}'))*self.COIN_VALUES[coin]
    return self.money_recieved
  
  def make_payment(self,cost):
    self.process_coins()
    if self.money_recieved >= cost:
      change=round(self.money_recieved-cost,2)
      self.profit+=cost
      return True
    else:
      print("Sorry thats not enough money.")
      self.money_recieved=0
      return False
