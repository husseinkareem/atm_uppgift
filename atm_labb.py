class Account:
  def __init__ (self, pin, balance): 
    self.pin = pin
    self.balance = balance #Class beskriver egenskaperna på ditt objekt. 

accountsList  = [] #Du har inga konton i början, därför börjar man med en tom lista.

def cashWithdraw(currentBalance): #Dra ut pengar, en funktion som tar emot befintliga saldot som i sin tur minskas beroande på din angivna belopp.  
  amount = int(input("Ange belopp: ")) 
  return currentBalance - amount 

def cashDeposit(currentBalance): #Stoppa in pengar, en funktion som tar emot befintliga saldot som i sin tur utökas beroande på din angivna belopp.
  amount = int(input("Ange belopp du vill sätta in: "))
  return currentBalance + amount  

def menue():
  print("""****HUVUDMENY****
        1. Skapa konto 
        2. Administrera konto 
        3. Avsluta """)

def accountMenue():
    account = None # Vi har ej bestämt vad vi har för konto än. 
    accountPin = int(input("Skriv in ditt kontonummer: "))
    for a in accountsList: 
      if accountPin == a.pin:
        account = a

    if account == None:
      print("Kontot finns inte")
  
    loggedIn = True # När användaren är inloggad i kontomenyn då loopar den. 
    while loggedIn: # variabel behållare. 
      print("""****KONTOMENY**** - Konto: {} 
            1. Ta ut pengar 
            2. Sätt in pengar
            3. Visa saldo
            4. Logga ut """.format(account.pin)) 
      try: # För felhantering. 
        choice = int(input("Ange menyval: "))
        if(choice == 1):
          account.balance = cashWithdraw(account.balance)
        elif(choice == 2):
          account.balance = cashDeposit(account.balance)
        elif(choice == 3):
          print("Ditt nuvarande saldo är: {} kr ".format(account.balance))
        else: loggedIn = False 
      except ValueError: 
        print("Inmatade värdet ska vara ett numeriskt värde.")

def createAccount():
  pin = int(input("Ange kontonummer: "))
  for a in accountsList:
    if(a.pin == pin):
      print("Kontot finns redan, testa igen..")
      createAccount()
      return
  balance = int(input("Ange insättningsbelopp: "))
  accountsList.append(Account(pin, balance))

def main():
  while True:
    menue()
    try: # För felhantering. 
      choice = int(input("Ange menyval: "))
      if choice == 1:
        createAccount()
      elif choice == 2:
        accountMenue()
      elif choice == 3:
        break
      else:
        print("Ogiltigt alternativ")
    except ValueError:
      print("Inmatade värdet ska vara ett numeriskt värde.")

main()


