from  random import randrange
x=0
y=randrange(1,100)


while (x!= y):
    X=int(input("devinez un nombre "))
    if x< y :
            print("plus grand")
    elif x> y:
            print("plus petit")
    else :
            print("vous trouvé")
        
        
