# Loop example - using the index


# for num in range -- "num" is the index

print("This program prints numbers and their squares.")

first = int(input("Number to start at: "))
last = int(input("Number to end at: "))
last = last + 1 # because of how ranges work

print("number\tnumber squared")
print("_" * 20)
for num in range(first, last):
    squared = num * num
    print (num, "\t", squared) 
