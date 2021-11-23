print("Il faut répondre par oui ou non\n")
rep=input("vous etes adulte ")
if rep!="oui" and rep!="non":
        print("Vous devez répondre par 'oui' ou bien 'non'")
        rep=input("vous etes adulte ")
else:
    print("Au revoir")
