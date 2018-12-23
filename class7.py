# def canyoudriveacar():
#     x = input("what is your name")
#     y = int(input("what is your age"))
#     if y >= 18:
#         return" You are eligble to drive a car"
#     else:
#         return" You can not eligble drive a car"
# print(canyoudriveacar())  


# def leapyear():
#     x = int(input("which year is going on"))
#     if x%4 ==0:
#         return "that year is a leap year"
#     else:
#         return "that year is not a leap year"  
# print(leapyear())      


def hello_f(greetings = "hi",name="you"):
    return "{}{}".format(greetings,name)
print(hello_f("hi,amogh"))    