rows = int(input("Enter the number of rows: "))

if (rows%2) == 0:
    hrow = int(rows/2)
else:
    hrow = int(rows/2)+1

space = hrow - 1

for i in range(1, hrow + 1):
    for j in range(1, space + 1):
        print(end = " ")
    space = space - 1
    num = 1

    for j in range(2*i-1):
        print(end = str(num))
        num = num+1
    
    print()

space = 1

for i in range(1, hrow):
    for j in range(1, space + 1):
        print(end= " " )
    space = space + 1
    num = 1 
    for j in range(1, 2*(hrow - i)):
        print(end= str(num))
        num = num +1 
    print()