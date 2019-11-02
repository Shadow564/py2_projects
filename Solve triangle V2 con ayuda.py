def get_side(name):
    try:
        side = float(input("Side %s: " % name))
        if side > 0: return side
        else: raise ValueError
    except ValueError:
        get_side(name)

def get_angle(name):
  try:
    angle = float(input("Angle %s: " % name))
    if 0 < angle < 180: return angle
    else: raise ValueError
  except ValueError:
        get_angle(name)

sidea = get_side("a")
sideb = get_side("b")
sidec = get_side("c")

anglea = get_angle("A")
angleb = get_angle("B")
anglec = get_angle("C")

def side_inequal(a, b, c):
  if c < b or b < a:
    return False
  else:
    if (b - a) < c < (a + b):
      return True
    else:
      return False

def check_angles(angles): 
	return sum(angles) == 180

    
print side_inequal(sidea, sideb, sidec)

angle_list = [anglea, angleb, anglec]

print check_angles(angle_list)

