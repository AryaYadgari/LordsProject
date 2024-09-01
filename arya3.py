# x=int(input('adad aval ra vared konid:'))
# y=int(input('adad dovom ra vared konid:'))
# def add(x,y):
#     return x*y
# print(add(x,y))





# def funcOutter():
#     def funcInner1():
#         return 1
#     def funcInner2():
#         return 10
#     return funcInner1,funcInner2
# func1 , func2 = funcOutter()
# print(func1())
# print(func2())




# def funcOtter(h):
#     def funcMiddle(y):
#         def funcInner(z):
#             return z+y+h
#         return funcInner
#     return funcMiddle
# print(funcOtter(2)(5)(8))



def calculator(x,y):
    def taghsim():
        return x/y
    def zarb():
        return x*y
    def jam():
        return x+y
    def menha():
        return x-y
    return taghsim,zarb,jam,menha
while(True):
    num1=int(input('adad aval ra vared konid:'))
    num2=int(input('adad davom ra vared konid:'))
    amaliat1,amaliat2,amaliat3,amaliat4=calculator(num1,num2)
    choice=input('* / - + entekhab konid:')
    if(choice=="/"):
        print(amaliat1())
    elif(choice=="*"):
        print(amaliat2())
    elif(choice=="+"):
        print(amaliat3())
    elif(choice=="-"):
        print(amaliat4())




