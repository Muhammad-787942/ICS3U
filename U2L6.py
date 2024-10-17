#1
S = "#"
for i in range(10, 0, -1):
    print(S * i)


#2
S = "#"
space_count = 5
for i in range(1, 10, 2):
    print(" " * space_count, S * i)
    space_count -=1


#3
S = "#"
space_count = 5
for i in range(1, 12, 2):
    print(" " * space_count, S * i)
    space_count -=1
space_count = 1
for i in range(9, 0, -2):
    print(" " * space_count, S * i)
    space_count +=1
