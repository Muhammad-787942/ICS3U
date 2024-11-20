filename = "smiley_emoji_mod.xpm"
fh = open(filename, "r")
colorData = fh.readline() # file handle must be open
colorData.strip() 

print(colorData)

rows, cols, numColors = colorData.split()

numColors=int(numColors)

colorDefs = [[0] * 2] * numColors 
for i in range(numColors):
    colorData = fh.readline()
    colorData.strip()
    sym, c, color = colorData.split()
    colorDefs[i][0] = sym
    colorDefs[i][1] = color
    colorDefs[i][1] = c
print(colorData.split())
