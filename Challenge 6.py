from math import sqrt
def function(number):
    return sqrt((10 * number)/3)

list_of_returned = []

inputs = raw_input()
for i in inputs.split(','):
    ref_i = int(function(float(i)))
    list_of_returned.append(ref_i)

print list_of_returned
