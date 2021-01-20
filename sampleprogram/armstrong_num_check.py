def check_armstrong_num(num):
    num_len= len(num)
    print(num_len)
    num_list=[a for a in num]
    print(num_list)
    sum=0
    for i in num_list:
        sum=sum+int(i)**len(num)
    print("sum = {}".format(sum))
    if int(num)==sum:
        print("it's an armstrong number")
    else:
        print("OOPS!!it's not an armstrong number")


num=input("enter the number : ")
check_armstrong_num(num)
