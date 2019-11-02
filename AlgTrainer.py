from random import randint

tester = True

def turn():
  listofsetups = ["R' L R L'", "L R' L' R", "U' R U R'", "U L' U' L", "R U' R' U", "L' U L U'", "R' L R L2' U L U'", "L R' L' R2 U' R' U"]
  buffering = raw_input("Hit Enter for new alg.")
  if buffering == "break":
    global tester
    tester = False
  else: pass
  queue = randint(0, len(listofsetups) - 1)
  return listofsetups[queue]

while tester == True:
  print turn()
