a = int(input("iki basamaklı bir sayı giriniz"))
c = []
c.append(a//10)
c.append(a-c[0]*10)
def okuma(list):
    if list[0] == 1:
        print("on")
    elif list[0] == 2:
        print("yirmi")
    elif list[0] == 3:
        print("otuz")
    elif list[0] == 4:
        print("kırk")
    elif list[0] == 5:
        print("elli")
    elif list[0] == 6:
        print("altmış")
    elif list[0] == 7:
        print("yetmiş")
    elif list[0] == 8:
        print("seksen")
    elif list[0] == 9:
        print("doksan")
    if list[1] == 1:
        print("bir")
    elif list[1] == 2:
        print("iki")
    elif list[1] == 3:
        print("üç")
    elif list[1] == 4:
        print("dört")
    elif list[1] == 5:
        print("beş")
    elif list[1] == 6:
        print("altı")
    elif list[1] == 7:
        print("yedi")
    elif list[1] == 8:
        print("sekiz")
    elif list[1] == 9:
        print("dokuz")
okuma(c)