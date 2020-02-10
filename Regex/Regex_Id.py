num=input('Enter Your Id:' )

check=0

if len(num)==9:


    if num[0:3]=='011':

        if num[3]  and num [4]in "0123456789":
            if num[5] in '123':

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