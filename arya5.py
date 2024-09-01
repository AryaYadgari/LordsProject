# x=0
# def add(x):
#     x+=1
#     return x

# def add():
#     x=0
#     def nasted():
#         nonlocal x
#         x+=1
#         return x
#     return nasted 
# func1=

    

def bank():
    ramze_kart='12345'
    mojoodieHesab=200_000

    def enteghal():
        shomareKartUser=input('shomare karte maghsad ra vared konid:')
        mablaghUser=input('mablagh ra vared konid:')
        ramzeKartUser=input('ramze kart ra varerd konid:')
        nonlocal mojoodieHesab
        mojoodieHesab-=int(mablaghUser)
               
     
    def mojoodi():
        nonlocal mojoodieHesab
        print(mojoodieHesab)
        return

    def bardasht():
        mablaghUser=input('mablagh ra vared konid:')
        nonlocal mojoodieHesab
        mojoodieHesab-=int(mablaghUser)
        print('movafagh')
        return

    def variz():
        mablaghUser=input('mablagh ra vared konid:')
        nonlocal mojoodieHesab
        mojoodieHesab+=int(mablaghUser)
        print('movafagh')
        return


    while(True):
        print('1.enteghal')
        print('2.mojoodi')
        print('3.bardasht')
        print('4.variz')
        usreChoice=input('entekhab konid:')
        if(usreChoice=='1'):
            enteghal()
        elif(usreChoice=='2'):
            mojoodi()
        elif(usreChoice=='3'):
            bardasht()
        elif(usreChoice=='4'):
            variz()

bank()





