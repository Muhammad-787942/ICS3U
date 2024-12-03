filename = "smiley_emoji_mod.xpm"
fh = open(filename, "r")
colorData = fh.readline() # file handle must be open
colorData.strip() 

print(colorData)

rows, cols, numColors = colorData.split()

numColors=int(numColors)

colorDefs = []
for i in range(numColors):
    colorData = fh.readline()
    colorData.strip()
    [sym, c, color] = colorData.split()
    if (sym == '~'):
        sym = " "
    colorDefs.append([sym, color])
    print(i, sym, color)

print(colorDefs)
