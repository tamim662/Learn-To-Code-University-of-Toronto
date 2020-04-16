def regex_1():
    num=input('Enter Your Id:' )

    check=0

    if len(num)==9:


        if num[0:3]=='011':

            if num[3]  and num [4]in "0123456789":
                if num[5] in '123' and num[6:] != '000':

                    print("your Id: "+num)  
                else:
                    check=-1   
            else:
                check=-1               
        else:
                check=-1
    else:
                check=-1
   
    if check <0:
        print('Invalid Input')
    
    

def regex_2():
    a=input("Enter Complex Number: ")
    flag, flag2 , flag3 = 0, 0, 0
   
    s=len(a)
    

    for i in range(s):
       if a[i]=="+":
           index=i
           for j in range(index,s):
               if a[j]=="i":
                   flag=1
    

    

    if flag == 1:
        print("Accepted")
    else:
         print("Not accepted")

def regex_3():
    flag = 0
    x = input("Enter Expression: ")
    if len(x)<3 :
       finish()
    if x[0] >= '0' or x[0] <= 9:
        if x[1].isupper() :
            if not x[2].isalpha():
                flag = 1
            else:
                flag = 0
        else:
            flag = 0
    else:
        flag = 0

    if flag == 1:
        print("Accepted.")
    else:
        print("Not Accepted.")

def regex_4():
    flag , z = 1 , 1

    number = input("Enter a no: ")
    x= len(number)
    if number[x-1] == '.':
        print("Not accepted")
        exit()
    for i in range (x):
        if (number[i] >= 'A' and number[i] <= 'Z') or (number[i] >= 'a' and number[i] <= 'z'):
            flag = 0
        elif number[i] == '.':
            if number[i+1]>= '0' and number[i+1]<= '9':
                z=0
            else:
                z=5
    if flag == 0 : print("Not accepted.")
    elif z==0 : print("Accepted")
    elif z==5 : print("Not accepted")
    else: print("Accepted")


def regex_5():
    flag, flag1, flag2, flag3 = 0 , 0 , 0, 0
    a = input("Enter password: ")
    temp = 1
    b = len(a)
    if len(a)<8:
        temp = 0

    for i in range(len(a)):
        if a[i]>='A' and a[i] <= 'Z':
            flag=1
        if a[i] >= 'a' and a[i] <= 'z':
            flag1=1
        if a[i] >= '0' and a[i] <= '9':
            flag2=1
    if a[b-1] == '@' or a[b-1] == '#' or a[b-1] == '$' or a[b-1] == '&':
            flag3=1
    if flag == 1 and flag1 == 1 and flag2 == 1 and temp ==1 and flag3 ==1:
        print("Accepted")
    else:
        print("Not accepted")


choice=""

while not(choice=='exit' or choice=='EXIT'  or choice=='Exit'):
    choice=input("Enter Youe Choice or to leave write exit:")
    if choice =='1':
        regex_1()
        
        
    elif choice =='2':
        regex_2()
    elif choice=='3':
        regex_3()
    elif choice=='4':
        regex_4()
    elif choice=='5':

        regex_5()

print('See you in Next assignment')