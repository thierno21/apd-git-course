
x=int(input("entrez un nombre "))
y=int(input("entrez un nombre "))
if x>y:
    max= x
else:
    max= y
for i in  range(1,min+1):
    if x% i==0 and y% i==0:
              pgdc=1
print("le pgdc de ",x," et ",y, " est :",pgdc)
