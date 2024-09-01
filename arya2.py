

def zarb(_adad1,_adad2):
    return adad1*adad2


def taghsim(_adad1,_adad2):
    return adad1/adad2



def jam(_adad1,_adad2):
    return adad1+adad2



def tafrigh(_adad1,_adad2):
    return adad1-adad2


while(True):
    adad1=int(input('adad aval ra vard kon: '))
    adad2=int(input('adad dovom ra vared kon: '))

    choice=input("*  and  /  and  +  and  -")
    if(choice=="*"):
        print(zarb(adad1,adad2))
    elif(choice=="/"):
        print(taghsim(adad1,adad2))
    elif(choice=="+"):
        print(jam(adad1,adad2))
    elif(choice=="-"):
        print(tafrigh(adad1,adad2))
        
