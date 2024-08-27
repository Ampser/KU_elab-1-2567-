class Coin:
  def __init__(self, value = 1):
    self.value = value

  def __str__(self):
    return f'{self.value} Baht Coin'

class BankNote:
  def __init__(self, value = 20):
    self.value = value

  def __str__(self):
    return f'{self.value} Baht Banknote'
  
money = int(input("Input amount : "))
list_bank=[BankNote(1000),
           BankNote(500),
           BankNote(100),
           BankNote(50),
           BankNote(20)
           ]
list_coin=[Coin(10),
           Coin(5),
           Coin(2),
           Coin(1)]
for i in range (len(list_bank)):
    if(money >=list_bank[i].value):
        print(f'You get {money//list_bank[i].value} of {list_bank[i].value} Baht Banknote')
        money%=list_bank[i].value
    else: pass
for i in range (len(list_coin)):
    if(money >=list_coin[i].value):
        print(f'You get {money//list_coin[i].value} of {list_coin[i].value} Baht Coin')
        money%=list_coin[i].value
    else: pass