writeFile = open("fixed.txt", "w")
readFile = open("alleghenyMap.txt", "r")
for i in readFile:
    writeFile.write(i.upper())
