def pointcounter(string): #credits zu michael dotzer
    if string == "":
        return False
    count = 0
    for x in range(0, len(string)):
        if string[x].isdigit():
            pass
        elif string[x] == "." and count == 0:
            return x          
    if count >= 1:
        if string[0] == ".":
            return count
        else:
            return count

    return False

def inputWOA():
    _woacheck = False
    var2 = input() #eingabe
    _pointcounter = pointcounter(var2)
    var = len(var2) #länge der eingeabe in var
    print(var) #debug
    var3 = list(var2) #setzen der eingabe in eine liste
    for i in reversed(range(var)): #forschleife der maximalen anzahl(var) reversed
        if var3[i] == '.' and i==_pointcounter: #wenn checked char = . und noch kein . dann
            _woacheck = True
        elif var3[i].isdigit() != True: #überprüfung ob getesteter character keine zahl ist
            del var3[int(i)] #entfernung des characters
    var2 = ''.join(var3) #zusammensetzung der liste in einen string
    if _woacheck == True: #wenn WOA = true = float
        if var2[0] == '.':
            var2 = float(var2) #float casting
    elif var2=="":   #sonst int
        print("nothing")
    else:
        var2 = int(var2) #casting des string to int
    return var2 #return to main

# def removenondigits(string):
#     x = len(string)
#     for i in range(0,x):
#         if string[i] == '.' and _woacheck != True:
#             _woacheck = True
#         elif string[i].isdigit() != True:
            # string.replace(string[i],'')




zahl1 = inputWOA() #function call
print(zahl1) #debug ausgabe

# print(removenondigits(input()))

