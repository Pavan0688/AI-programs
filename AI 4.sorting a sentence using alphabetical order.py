print("enter the string:")
str=input()

wrds=str.split()
wrds.sort()

sortedwrds=""
for wrd in wrds:
    sortedwrds=sortedwrds+wrd+""
    
print(sortedwrds)
