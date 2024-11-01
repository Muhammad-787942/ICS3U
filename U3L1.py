progname = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis in."
print(progname) 
print(progname[0]) 
count = 0
for c in progname: 
    print(c, end="")
                             
print()

for c in range(len(progname)):
    if (progname[c]==" "):
      count = count+1
      
print ("There are,",count ,"spaces in the text")
