x = int(input("how many items are you entering"))
items = []
for i in range(x):
  y = input("what items go on the list")
  items[len(items):] = [y]
print ("you have entered", x ,"items")
for c in range (len(items)):
  print(items[c])
