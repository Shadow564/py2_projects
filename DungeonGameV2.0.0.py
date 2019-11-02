print "Welcome to Dungeon Moving v.1.0 (since I started counting)"
print "w is up, a is left, s is down, d is right, e is end, and i is open your inventory"

#Sets up room and door system unique to these versions
allrooms = []
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
        self.r1x = r1x
        self.rly = r1y
        self.r2x = r2x
        self.r2y = r2y
        self.islocked = islocked

class chest(object):
  def __init__(self, roomin, y, x, things):
    self.roomin = roomin
    self.y = y
    self.x = x
    self.things = things

  def chestplace(self):
    allrooms[roomin].layout[self.y][self.x] = "C"

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


def openchest(r, y, x):
  print "CHEST BOI"
  for i in allrooms[roomin].chestlist:
    if i.y == y and i.x == x:
      i.openingchest()
  global xcoord
  global ycoord
  rebound(y, x)
  
#player info
inv = []
roomin = 0

#set up first room
 #r01Layout
r01Layout = []
for x in range(0, 7):
  r01Layout.append(["#"] * 7)
nerds = [0, 6]
for le in nerds:
  for i in range(0, 7):
    r01Layout[le][i] = "B"
    r01Layout[i][le] = "B" 
r01Layout[3][6] = "D"
r01Layout[2][1] = "W"
r01Layout[2][2] = "W"
r01Layout[2][3] = "W"
r01Layout[2][4] = "W"
 #setup doors
door_1_3_6 = doors(3, 6, None, None, False)
r01Doors = [door_1_3_6]
 #setup Chests
chest_1_1_1 = chest(0, 1, 1, ["apples", "stick"])
r01Chests = [chest_1_1_1]
 #setup Printing
def printR01(var):
  global r01Layout
  for row in r01Layout:
    print " ".join(row)
 #finalize room
roomN1 = rooms(r01Layout, r01Doors, r01Chests, True, 7, 7, printR01)
allrooms.append(roomN1)

#Places Chest and Guy
chest_1_1_1.chestplace()
ycoord = 3
xcoord = 3
allrooms[roomin].layout[ycoord][xcoord] = "G"
roomN1.comoprinter(8)

#Needs changed
def rebound(yco, xco):
  global ycoord
  global xcoord
  if user_input == "w":
      yco += 1
      ycoord += 1
      allrooms[roomin].layout[yco][xco] = "G"
      allrooms[roomin].comoprinter(8)
  elif user_input == "s":
      yco -= 1
      ycoord -= 1
      allrooms[roomin].layout[yco][xco] = "G"
      allrooms[roomin].comoprinter(8)  
  elif user_input == "a":
      xco += 1
      xcoord += 1
      allrooms[roomin].layout[yco][xco] = "G"
      allrooms[roomin].comoprinter(8)
  elif user_input == "d":
      xco -= 1
      xcoord -= 1
      allrooms[roomin].layout[yco][xco] = "G"
      allrooms[roomin].comoprinter(8)

#Needs changed
def testspot(yco, xco):
  if allrooms[roomin].layout[yco][xco] == "#":
    allrooms[roomin].layout[yco][xco] = "G"
    allrooms[roomin].comoprinter(8)
  elif allrooms[roomin].layout[yco][xco] == "C":
    openchest(roomin, yco, xco)
  else:
    print "WALL BOI"
    global user_input
    global xcoord
    global ycoord
    rebound(yco, xco)

#Basic moving engine
def move(direction):
    global ycoord
    global xcoord
    global motion
    motion = True
    if direction == "w":
      if ycoord == 0:
        print "There is no door there."
        print_room(room)
      else:
        allrooms[roomin].layout[ycoord][xcoord] = "#"
        ycoord -= 1
        testspot(ycoord, xcoord)
    elif direction == "s":
      if ycoord == (7 - 1):
        print "There is no door there."
        print_room(room)
      else:
        allrooms[roomin].layout[ycoord][xcoord] = "#"
        ycoord += 1
        testspot(ycoord, xcoord)
    elif direction == "a":
      if xcoord == 0:
        print "There is no door there."
        print_room(room)
      else:
        allrooms[roomin].layout[ycoord][xcoord] = "#"
        xcoord -= 1
        testspot(ycoord, xcoord)
    elif direction == "d":
      if xcoord == (7 - 1):
        print "There is no door there."
        print_room(room)
      else:
        allrooms[roomin].layout[ycoord][xcoord] = "#"
        xcoord += 1
        testspot(ycoord, xcoord)
    else:
      print "lol wut"  

running = 0
death = False
def turn(run):
    global running
    running += 1
    global user_input
    user_input = raw_input("Enter: ")

while running >= 0 and death == False:
  turn(8)
  print running
  global user_input
  if user_input == "e":
    break
  elif user_input == "sad":
    death = True
  elif user_input == "i":
    inv.sort()
    print inv
  else:
    move(user_input)
