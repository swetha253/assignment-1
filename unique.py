string=input("string1 = ")
unique=set(string)
len=len(unique)
print("uniqueLetters =",end=" ")
for i in unique:
    print(i,end="")
    if len-1>0:
        print(",",end="")
        len=len-1

