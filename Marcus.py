name_list = ["Jihee", "jihee", "Marcel", "marcel", "Sebastian", "sebastian"]
nor_List = ["Marcus"]

x = 0

while(x<10):
    name = input("Bitte gib deinen Vornamen ein\n")
    if name in name_list:
        print("Hallo" , name , "schön dich hier zu sehen :)")

    elif name in nor_List:
        print(name+"?", "\nWas willst du denn?\nFür Kinder kein Zutritt!")
    x=x+1
    

