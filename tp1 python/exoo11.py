Python 3.10.0 (ags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

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
        
        
