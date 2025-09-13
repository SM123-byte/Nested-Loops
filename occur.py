#

string = input("Enter a word: ")
chars = input("Enter your character: ")

i = 0 
count = 0 

while (i < len(string)):
    if (string[i] == chars):
        count = count + 1
    i = i + 1

print("The total number of times ", chars, " has occured ", count)

