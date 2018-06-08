import random
def getNumber(number):
 if number == 1:
  return "e o numero 1"
 elif number == 2:
  return "e o numero 2"
 elif number == 3:
  return "e o numero 3"
 elif number == 4:
  return "e o numero 4"
 elif number == 5:
  return "e o numero 5"
 elif number == 6:
  return "e o numero 6"
 elif number == 7:
  return "e o numero 7"
 elif number == 8:
  return "e o numero 8"
 elif number == 9:
  return "e o numero 9"
r = random.randint(1,9)
sorteio = getNumber(r)
print(sorteio)
