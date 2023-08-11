#Game Introduction

print("Dobrodosli na ostrvo sa blagom\nVasa misija je da pronadjete blago na ostrvu")

korak_jedan = input("Idete li Levo ili Desno? L/D\n")
#Anything else than "L" is a lost
if korak_jedan != "L":
    print("Pali ste u rupu. Game over")
else:
    korak_dva = input("Plivate ili cekate? P/C\n")
    #Anything else than "C" is a lost
    if korak_dva != "C":
        print("Pojela te ajkula. Game over")
    else:
        korak_tri = input("Na koja vrata ulazite? Plava, Crvena ili Zuta? P/C/Z\n")
        # "P", "C", "Anything else" is a lost. Z is a win
        if korak_tri == "P":
            print("Pojela vas je zivujka. Game over")
        elif korak_tri == "C":
            print("Izgoreli ste u vatri. Game over")
        elif korak_tri == "Z":
            print("Pobedili ste")
        else:
            print("Game over")