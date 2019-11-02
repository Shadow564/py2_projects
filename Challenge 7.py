dimensions = [x for x in raw_input("Enter: ").split(',')]
dim1 = int(dimensions[0])
dim2 = int(dimensions[1])

grand_row = []
for i in range(0, dim1):
    row = []
    for j in range(0, dim2):
            row.append(j * i)
    grand_row.append(row)

for row in grand_row:
    print row
        
    
