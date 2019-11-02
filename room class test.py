class rooms(object):
    def __init__(self, layout, doorlist, chestlist, isloaded, yborder, xborder, comoprinter):
      self.layout = layout
      self.doorlist = doorlist
      self.chestlist = chestlist
      self.loaded = isloaded
      self.yborder = yborder
      self.xborder = xborder
      self.comoprinter = comoprinter

class doors(object):
    def __init__(self, r1x, r1y, r2x, r2y, islocked):
        self.rlx = rlx
        self.rly = r1y
        self.r2x = r2x
        self.r2y = r2y
        self.islocked = islocked

chestque = ""

class chest(object):
  def __init__(self, room, y, x, things):
    self.room = room
    self.y = y
    self.x = x
    self.things = things
    
  def chestplace(self):
    self.roomnumber[self.y][self.x] = "C"
    
  def openingchest(self):
    print self.things
    global chestque
    if self.things == []:
      aredone = 1
    else:
      aredone = 0
    passo = False
    tradedone = 0
    while aredone == 0:
      chestque = raw_input("What do you want?")
      passo = 0
      if chestque == "all":
        tradedone = 1
        global inv
        for ele in self.things:
          print ele + "debug"
          inv.append(ele)
        self.things = []
        print self.things
      elif chestque == "null":
        tradedone = 1
      else:
        for i in self.things:
          passo = False
          print i + " debug"
          if chestque == i:
            tradedone = 1
            inv.append(chestque)
            self.things.remove(chestque)
            print self.things
          else:
            pass
      if tradedone == 1:
          pass
      else:
          print "Not Found"
      if tradedone == 0:
        pass
      else:
        de = raw_input("Are you done? Yes or No?: ")
        if de == "No":
          passo = True
        elif de == "Yes":
          if passo == False:
            print "Thanks for shopping!"
            aredone = 1
          else:
            pass
        else:
          print "Guess you're not done????"
    print "Bye!"
  
chest1_4_4 = chest(room1, 4, 4, ["shirt", "apple", "stick", "banana"])
chest1_4_4.chestplace()

chest1_2_1 = chest(room1, 2, 1, ["flint", "iron", "coal"])
chest1_2_1.chestplace()

list_of_chests = [chest1_4_4, chest1_2_1]

def openchest(y, x):
  print "CHEST BOI"
  global list_of_chests
  for i in list_of_chests:
    if i.y == y and i.x == x:
      i.openingchest()
  global xcoord
  global ycoord
  rebound(y, x)

def rebound(yco, xco):
  global ycoord
  global xcoord
  if user_input == "w":
      yco += 1
      ycoord += 1
      room[yco][xco] = "G"
      print_room(room)
  elif user_input == "s":
      yco -= 1
      ycoord -= 1
      room[yco][xco] = "G"
      print_room(room)  
  elif user_input == "a":
      xco += 1
      xcoord += 1
      room[yco][xco] = "G"
      print_room(room)
  elif user_input == "d":
      xco -= 1
      xcoord -= 1
      room[yco][xco] = "G"
      print_room(room)
      
#The below block sets up room1's layout
global proxy
proxy = []
def roombuilding1(q):
  for x in range(0, 7):
    proxy.append(["#"] * 7)
  nerds = [0, 6]
  for le in nerds:
    for i in range(0, 7):
      proxy[le][i] = "B"
      proxy[i][le] = "B" 
  proxy[3][6] = "D"
  proxy[1][2] = "W"
  proxy[2][2] = "W"
  proxy[3][2] = "W"
  proxy[4][2] = "W"
  return proxy
room1setup = roombuilding1(8)
room1doors = room1setup[3][6]
room1chests
def room1printer(var):
  global proxy
  for row in proxy:
    print " ".join(row)    
room1 = rooms(room1setup, room1doors, room1chests, True, 6, 6, room1printer(8))

room1.comoprinter

