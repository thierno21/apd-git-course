a=int(input('entrez un nombre !'))
sda=0
for i in range(1,a):
     if(a%i==0):
        sda=sda+i
        i=i+1
if(sda == a):
    print(a,'est un nombre parfait')
else:
    print(a,'n est pas un nombre parfait')

