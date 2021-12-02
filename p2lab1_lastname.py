# CTI 110
# P2LAB1
# test program
# Name
# Date

# Write a program using integers user_num and x as input,
# and output user_num divided by x three times.

user_num = int(input("Enter a number: "))
x = int(input("Enter another number: "))

# Program should divide user_num by x, then again, then again
answer = user_num // x
print(answer)

answer = answer // x
print(answer)

answer = answer // x
print(answer)

