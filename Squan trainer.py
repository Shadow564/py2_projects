from random import randint 


def go():
  buffer = raw_input("Press Enter to get new algs: ")
  co = ["1-1", "adj-adj", "dia-dia", "adj-dia", "dia-adj"]
  eo = ["1-1", "L-L", "3-3", "line-line", "L-line", "4-4", "line-L"]
  cp = ["dia-dia", "null-adj", "adj-dia", "dia-dia", "null-dia", "adj-null", "dia-null", "adj-adj"]
  ep = ["cwu-", "ccwu-", "z-", "h-", "-h", "-z", "adj-adj", "oppo-oppo", "-cwu", "-ccwu", "ccwo-oppo", "ccwo-oppo", "adj-"]
  fco = co[randint(0, len(co) - 1)] 
  feo = eo[randint(0, len(eo) - 1)] 
  fcp = cp[randint(0, len(cp) - 1)] 
  fep = ep[randint(0, len(ep) - 1)]
  print fco
  print feo
  print fcp
  print fep

while True:
  go()
