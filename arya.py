

def tabdilDama(dama):
    c2f=(1.8*dama)+32
    f2c=(dama-32)/1.8
    return "f: "+str(c2f),"c : "+str(f2c)


while(True):
    choice=input("1.c2f and 2.f2c")
    if(choice=="1"):
        print(tabdilDama(int(input("dama ra vared konid: "))))
    else:
        print(tabdilDama(int(input("dama ra vared konid: "))))
        



