print "Welcome to Dungeon Moving v.2.0 (since I started counting)"
print "w is up, a is left, s is down, d is right, e is end, and i is open your inventory"

#player info
inv = []
roomin = 0

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
    def __init__(self, r1, r2, r1y, r1yin, r1x, r1xin, r2y, r2yin, r2x, r2xin, islocked,):
        self.r1 = r1
        self.r2 = r2
        self.r1y = r1y
        self.r1yin = r1yin
        self.r1x = r1x
        self.r1xin = r1xin
        self.r2y = r2y
        self.r2yin = r2yin
        self.r2x = r2x
        self.r2xin = r2xin
        self.islocked = islocked

    #self, r1, r2, r1y, r1yin, r1x, r1xin, r2y, r2yin, r2x, r2xin, islocked,
    def opendoor(self):
       allrooms[self.r1 - 1].layout[self.r1yin][self.r1xin] = "#"
       global ycoord
       global xcoord
       ycoord = self.r2yin
       xcoord = self.r2xin
       allrooms[self.r2 - 1].layout[self.r2yin][self.r2xin] = "G"
       global roomin
       roomin = self.r2 - 1
       allrooms[self.r2 - 1].comoprinter(8)
           
class chest(object):
  def __init__(self, roomin, y, x, things):
    self.roomin = roomin
    self.y = y
    self.x = x
    self.things = things

  def chestplace(self):
    allrooms[self.roomin].layout[self.y][self.x] = "C"

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

#Sets Up Crafting
list_of_recipes = []
list_of_recipes_readable = []
class recipe(object):
  def __init__(self, parts, endresult):
      self.parts = parts
      self.endresult = endresult

  def add_recipe(self):
    global list_of_recipes
    list_of_recipes.append(self)
    global list_of_recpes_readable
    list_of_recipes_readable.append(self.endresult)
    
def scan_for_truth(what_wanted):
    all_parts_had = True #Assumed unless told otherwise
    recipetarget = False
    for recipe in list_of_recipes:
      if recipe.endresult == what_wanted:
        recipetarget = True
        for part in recipe.parts:
          parttester = False
          for element in inv:
            if element == part:
              parttester = True
            else: pass
          if parttester == False:
            all_parts_had = False
          else: pass
        if all_parts_had == False:  
          print "You don't have everything needed."
          allrooms[roomin].comoprinter(8)
        else:
          for part in recipe.parts:
            for element in inv:
              if element == part:
                inv.remove(element)
              else: pass
          inv.append(recipe.endresult)
          print recipe.endresult + "has been crafted!"
          allrooms[roomin].comoprinter(8)
      else: pass  
    if recipetarget == False:
      print "No recipe for that item!"
      allrooms[roomin].comoprinter(8)
    else: pass

fire = recipe(["flint", "steel"], "fire")
fire.add_recipe()
steel = recipe(["coal", "iron"], "steel")
steel.add_recipe()
fruit_salad_one = recipe(["banana", "apple"], "carl's yummy fruit salad")
fruit_salad_one.add_recipe()

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
 #setup doors (self, r1, r2, r1y, rlyin, r1x, rlxin, r2y, r2yin, r2x, rxyin, islocked,)
door_1_3_6 = doors(1, 2, 3, 3, 6, 5, 1, 1, 0, 1, False)
r01Doors = [door_1_3_6]
 #setup Chests
chest_1_1_1 = chest(0, 1, 1, ["shirt", "apple", "stick", "banana"])
r01Chests = [chest_1_1_1]
 #setup Printing
def printR01(var):
  global r01Layout
  for row in r01Layout:
    print " ".join(row)
 #finalize room
roomN1 = rooms(r01Layout, r01Doors, r01Chests, True, 7, 7, printR01)
allrooms.append(roomN1)

#set up second room
 #r02Layout
r02Layout = []
for x in range(0, 5):
  r02Layout.append(["#"] * 9)
nerds = [0, 8]
for le in nerds:
  for i in range(0, 4):
    r02Layout[i][le] = "B"
nerds = [0, 4]
for le in nerds:
  for i in range(0, 9):
    r02Layout[le][i] = "B"
r02Layout[1][0] = "D"
r02Layout[2][8] = "D"
r02Layout[1][2] = "W"
r02Layout[2][2] = "W"
r02Layout[3][4] = "W"
r02Layout[1][6] = "W"
r02Layout[2][6] = "W"
 #setup doors (self, r1, r2, r1y, rlyin, r1x, rlxin, r2y, r2yin, r2x, rxyin, islocked,)
door_2_1_0 = doors(2, 1, 1, 1, 0, 1, 3, 3, 6, 5, False)
door_2_2_8 = doors(2, 1, 2, 2, 8, 7, None, None, None, None, False)
r02Doors = [door_2_1_0, door_2_2_8]
 #setup Chests
chest_2_2_4 = chest(1, 2, 4, ["flint", "iron", "coal"])
r02Chests = [chest_2_2_4]
 #setup Printing
def printR02(var):
  global r02Layout
  for row in r02Layout:
    print " ".join(row)
 #finalize room
roomN2 = rooms(r02Layout, r02Doors, r02Chests, True, 5, 9, printR02)
allrooms.append(roomN2)
roomN2.layout[2][4] = "C"

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
  elif allrooms[roomin].layout[yco][xco] == "D":
      for door in allrooms[roomin].doorlist:
        if door.r1y == yco and door.r1x == xco:
          door.opendoor()
      
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
        allrooms[roomin].comoprinter(8)
      else:
        allrooms[roomin].layout[ycoord][xcoord] = "#"
        ycoord -= 1
        testspot(ycoord, xcoord)
    elif direction == "s":
      if ycoord == (allrooms[roomin].yborder - 1):
        print "There is no door there."
        allrooms[roomin].comoprinter(8)
      else:
        allrooms[roomin].layout[ycoord][xcoord] = "#"
        ycoord += 1
        testspot(ycoord, xcoord)
    elif direction == "a":
      if xcoord == 0:
        print "There is no door there."
        allrooms[roomin].comoprinter(8)
      else:
        allrooms[roomin].layout[ycoord][xcoord] = "#"
        xcoord -= 1
        testspot(ycoord, xcoord)
    elif direction == "d":
      if xcoord == (allrooms[roomin].xborder - 1):
        print "There is no door there."
        allrooms[roomin].comoprinter(8)
      else:
        allrooms[roomin].layout[ycoord][xcoord] = "#"
        xcoord += 1
        testspot(ycoord, xcoord)
    else:
      print "lol wut"
      allrooms[roomin].comoprinter(8)

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
    allrooms[roomin].comoprinter(8)
  elif user_input == "z":
    print "You have waited."
    allrooms[roomin].comoprinter(8)
  elif user_input == "c":
    print list_of_recipes_readable
    qued = raw_input("What do you wanted to craft: ")
    scan_for_truth(qued)
  else:
    move(user_input)
