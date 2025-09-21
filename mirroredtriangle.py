# Mirrored Triangle

rows = int(input("Enter the number of rows: "))

# For the object right angle triangle 

for i in range(rows):
    for j in range(i+1):
        print("*", end=' ')
    print()

# For dashed line in mirroring  

length = rows * 2
dashed_line = "-" * length
print(dashed_line)

# For the image right angle triangle 

for i in range(rows):
    for j in range(i, rows):
        print("*", end=' ')
    print()
    