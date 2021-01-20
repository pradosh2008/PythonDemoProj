def maximum(a,b):
    if a>=b:
        return a
    else:
        return b


a=input("enter first number:")
b=input("enter second number:")
print("max number is : {}".format(maximum(a,b)))