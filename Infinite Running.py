room = []

for x in range(0, 5):
  room.append(["#"] * 5)

def print_room(room):
  for row in room:
    print " ".join(row)

ycoord = 2
xcoord = 2
                                     
nerd = room[xcoord][ycoord]
room[xcoord][ycoord] = "G"

print_room(room)

running = 0
death = False
def turn(run):
    global running
    running += 1
    global user_input
    user_input = raw_input("Enter: ")

def move(direction):
    if direction == "w":
      room[ycoord][xcoord] = "#"
      nerd = room[ycoord - 1][xcoord]
      room[ycoord - 1][xcoord] = "G"
      print_room(room)
    elif direction == "s":
      room[ycoord][xcoord] = "#"
      nerd = room[ycoord + 1][xcoord]
      room[ycoord + 1][xcoord] = "G"
      print_room(room)
    elif direction == "a":
      room[ycoord][xcoord] = "#"
      nerd = room[ycoord][xcoord - 1]
      room[ycoord][xcoord - 1] = "G"
      print_room(room)
    elif direction == "d":
      room[ycoord][xcoord] = "#"
      nerd = room[ycoord][xcoord + 1]
      room[ycoord][xcoord + 1] = "G"
      print_room(room)
    else:
      print "lol wut"  

while running >= 0 and death == False:
  turn(8)
  print running
  global user_input
  if user_input == "end":
    break
  elif user_input == "sad":
    death = True
  else:
    move(user_input)  

