import math

def testiffloat(part):
    if str(part) == part:
      try:
        part = float(raw_input('Leg %i' % (part)))
      except ValueError:
        return False
    else:
      return True

sidea = "red"
sideb = "blue"
hyp = "green"

while testiffloat(sidea) == False:
  sidea = raw_input("Leg A: ")

while testiffloat(sideb) == False:
  sideb = raw_input("Leg B: ")
  
while testiffloat(sidehyp):
  sidehyp = raw_input("Hyp: ")

while sidehyp < sidea or sidehyp < sideb:
  print "Hyp is too small."
  sidehyp = float(raw_input("Hyp: "))
test_hyp(sidehyp)
