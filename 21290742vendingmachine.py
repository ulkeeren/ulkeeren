def machin(): #Gets input from user to how much money they want to load.
    global money
    money = float(input("Load Money"))
    print("You loaded "+str(money) + " amount of money")
def menu(): #Prints the products in the vending machine
    global urunler
    global urunKodu
    global urunSayisi
    global menu
    global urunIndexi
    global urunUcreti
    urunler = ["Coca Cola", "Lays", "Ruffles", "Dokuz Kat Tat Rulokat", "Fanta", "Pepsi", "Capri Sun"]
    urunKodu = ["1.", "2.", "3.", "4.", "5.", "6.", "7."]
    urunIndexi = [1, 2, 3, 4, 5, 6, 7]
    urunSayisi = [5, 5, 5, 5, 5, 5, 5]
    urunUcreti = [3.75, 8.0, 8.0, 7.95, 8.9, 5.9, 2.1]

    for d in range(len(urunler)):
        print(urunKodu[d], urunler[d], "\t"+str(urunUcreti[d]))
def pick(): #Gets a product number from user to choose which product they want to get.
    global al
    global z
    global t
    global money
    al = int(input("Enter the product code of the product you want to get: "))
    o = 0

    while True:

        if 0 <= al <= 7:
            if al == urunIndexi[o]:
                if urunSayisi[o]>0:

                    if money >= urunUcreti[o]:

                        money -= urunUcreti[o]
                        urunSayisi[o] -= 1
                        print("You purchased a " + urunler[o] + ".")
                        print(str(urunSayisi[o]) + " " + urunler[o] + " and " + str(money) + " remaining.")
                        a = str(input("Do you want to purchase anyting more? Y/N"))
                        if a == "N":
                            break
                        else:
                            pick()




                    else:
                        print("Insufficent fund. Please load " + str(urunUcreti[o] - money) + " more money.")
                        h = str(input("Do you wish to load more money? Y/N"))
                        if h == "N":
                            print("Leaving vending machine.")
                        else:
                            machin()
                            pick()

                        break
                else:
                    print("There aren't any of the product left that you have chose. ")
                    l = input("Do you want to continue? Y/N")
                    if l == "N":
                        break
                    else:
                        pick()





        else:
            print("Invalid product code. ")
            break
        o += 1



machin()
menu()
pick()

