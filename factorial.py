#type1
num=int(input("find the factorial of number : "))
# i=1
# fact=1
# if num == 0:
#     print("factorial of {} is {}".format(num, 1))
# elif num < 0:
#     print("this is an invalid number")
# else:
#     while i <= num:
#         fact=fact*i
#         i+=1
#     print("factorial of {} is {}".format(num, fact))

#type2
#this method is ashort solution

# def factorial(num):
#     return 1 if (num==1 or num==0) else num*factorial(num-1)
#
# print("factorial of {} is {}".format(num,factorial(num)))

#type3
def factorial(num):
    if num == 0 or num==1:
        return 1
    elif num < 0:
        return 0
    else:
        fact=1
        while num>1:
            fact*=num
            num-=1
        return fact

print("factorial of {} is {}".format(num,factorial(num)))