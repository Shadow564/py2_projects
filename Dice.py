from random import randint
total = 0
def roll(number_of_d6):
    global total
    for i in range(0, int(number_of_d6)):
      total += randint(1, 6)
    return total

numderoll = int(raw_input("Number of Six Sided Dice: "))

suma = roll(numderoll)

print float(suma) / float(numderoll)
