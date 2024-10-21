import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)

while (y != 0):
  print("Now deciding if", y, "is a factor of", x, "...")
  rem = x % y
  if rem == 0:
    print("Yes!", y, "is a factor of", x)
    y = 0
  else:
    print("no!", y,  " is not a factor of", x)
    y = 0
print("end")

