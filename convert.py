# Decimal to Binary Conversion 

n = int(input("Enter a number: "))
result = ""

# Using modulus and division to list binary numbers

while n > 0:
    n1 = n
    n = int(n/2)
    r = n1 % 2

    # Code used to concatenate the strings 

    result = (str(r) + str(result))

print(f"The binary conversion for your number is: {result}")
    
    
    

