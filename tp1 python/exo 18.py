nb=int(input("entrez un nombre "))
s=0
tmp=nb
while tmp>0:
    d=tmp % 10
    s+=d**3
    tmp//=10
if nb==s:
    print(nb,"est un nombre armstrong")
else:
    sprint(nb,"n est pas  un nombre armstrong ")
