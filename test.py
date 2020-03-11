usr_ipt=""
count=0
while(usr_ipt!= "Exit"):
    usr_ipt=input()
    count+=1

    print("Serial"'\t''Name''\t'"Type"'\t'"Value")

    #print(usr_ipt)
    for i in range (len(usr_ipt)):

       
    
        if(usr_ipt[i]=='='):
            usr_ipt=usr_ipt[:-1]
            f_li=usr_ipt.split("=")
            li=f_li[0].split(" ")
            print(count,'\t',li[1],'\t',li[0],'\t',f_li[1],"\n")
            break

        elif(usr_ipt[i]==';'):
            usr_ipt=usr_ipt[:-1]
            li=usr_ipt.split(" ")
            print(count,'\t',li[1],'\t',li[0],'\t',"NULL","\n")

        elif(usr_ipt[i]==","):
            f_li=usr_ipt.split(",")
            space_split=usr_ipt.split(" ")
            stringcount=len(f_li)
            j=0
            while(j<stringcount):
                for k in range(len(f_li[j])):
                    if(f_li[j][k]=='='):
                        usr_ipt=usr_ipt[:-1]
                        p_li=usr_ipt.split("=")
                        li=p_li[0].split(" ")
                        print(count,'\t',li[1],'\t',space_split[0],'\t',p_li[1],"\n")
                        count+=1
                        break
                    elif(f_li[j][k]!="="):
                        usr_ipt=usr_ipt[:-1]
                        li=f_li[j].split(" ")
                        print(count,'\t',li[1],'\t',space_split[0],'\t',"NULL","\n")
                        count+=1
                        break
                j+=1
            break

        
        
    

    
        
    
