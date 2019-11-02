room = []

for x in range(0, 7):
  room.append(["#"] * 7)

def print_room(room):
  for row in room:
    print " ".join(row)

def openchest(y, x):
  print "CHEST BOI"
  chest_4_4.openingchest()
  global user_input
  global xcoord
  global ycoord
  rebound(y, x)

room[1][3] = "W"
room[2][3] = "W"
room[3][3] = "W"
room[4][3] = "W"

motion = False

inv = []
chestque = ""

class chest(object):
  def __init__(self, y, x, things):
    self.y = y
    self.x = x
    self.things = things
    
  def chestplace(self):
    room[self.y][self.x] = "C"
    
  def openingchest(self):
    print self.things
    global chestque
    aredone = 0
    passo = False
    tradedone = 0
    while aredone == 0:
      chestque = raw_input("What do you want?")
      for i in self.things:
        passo = False
        print i + " debug"
        if chestque == i:
          global inv
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
            aredone = 1
          else:
            pass
        else:
          print "Guess you're not done????"
        
chest_4_4 = chest(4, 4, ["torch", "apple", "stick", "banana"])
chest_4_4.chestplace()

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
      
ycoord = 2
xcoord = 2
room[xcoord][ycoord] = "G"

print_room(room)

def testspot(yco, xco):
  if room[yco][xco] == "#":
    room[yco][xco] = "G"
    print_room(room)
  elif room[yco][xco] == "C":
    openchest(yco, xco)
  else:
    print "WALL BOI"
    global user_input
    global xcoord
    global ycoord
    rebound(yco, xco)  

running = 0
death = False
def turn(run):
    global running
    running += 1
    global user_input
    user_input = raw_input("Enter: ")
    
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
        room[ycoord][xcoord] = "#"
        ycoord -= 1
        testspot(ycoord, xcoord)
    elif direction == "s":
      if ycoord == 4:
        print "There is no door there."
        print_room(room)
      else:
        room[ycoord][xcoord] = "#"
        ycoord += 1
        testspot(ycoord, xcoord)
    elif direction == "a":
      if xcoord == 0:
        print "There is no door there."
        print_room(room)
      else:
        room[ycoord][xcoord] = "#"
        xcoord -= 1
        testspot(ycoord, xcoord)
    elif direction == "d":
      if xcoord == 4:
        print "There is no door there."
        print_room(room)
      else:
        room[ycoord][xcoord] = "#"
        xcoord += 1
        testspot(ycoord, xcoord)
    else:
      print "lol wut"  

while running >= 0 and death == False:
  turn(8)
  print running
  global user_input
  if user_input == "e":
    break
  elif user_input == "sad":
    death = True
  else:
    move(user_input)
