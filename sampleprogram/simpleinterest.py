
def sinterest(principal,time,interest_rate):
    return (principal*time*interest_rate)/100

#bonus method
#calculate compound interest
def cinterest(principal,time,interest_rate):
    return ((principal*(1+interest_rate/100)**time)-principal)

def main():
    principal =float(input("enter principal amount:"))
    time=float(input("enter time:"))
    interest_rate=float(input("enter interest rate:"))
    print("simple interest is : {}".format(sinterest(principal,time,interest_rate)))
    print("compound interest is : {}".format(cinterest(principal, time, interest_rate)))

if __name__ == "__main__":
    main()





