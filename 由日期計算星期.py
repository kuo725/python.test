while True:  
    num = list(map(int,input().split(",")))  
        
    for j in range(0,len(num),2):     
        m = num[j]     
        d = num[j+1]  
        if m == 1 and 1<=d<=31:  
            if d%7==1:  
                print("Sunday")  
            if d%7==2:  
                print("Monday")  
            if d%7==3:  
                print("Tuesday")  
            if d%7==4:  
                print("Wednesday")  
            if d%7==5:  
                print("Thursday")  
            if d%7==6:  
                print("Friday")  
            if d%7==0:  
                print("Saturday")  
        elif m == 2 and 1<=d<=28:              
            if d%7==1:  
                print("Wednesday")  
            if d%7==2:  
                print("Thursday")  
            if d%7==3:  
                print("Friday")  
            if d%7==4:  
                print("Saturday")  
            if d%7==5:  
                print("Sunday")  
            if d%7==6:  
                print("Monday")  
            if d%7==0:  
                print("Tuesday")    
        elif m == 3 and 1<=d<=31:              
            if d%7==1:  
                print("Wednesday")  
            if d%7==2:  
                print("Thursday")  
            if d%7==3:  
                print("Friday")  
            if d%7==4:  
                print("Saturday")  
            if d%7==5:  
                print("Sunday")  
            if d%7==6:  
                print("Monday")  
            if d%7==0:  
                print("Tuesday")     
        elif m == 4 and 1<=d<=30:              
            if d%7==1:  
                print("Saturday")  
            if d%7==2:  
                print("Sunday")  
            if d%7==3:  
                print("Monday")  
            if d%7==4:  
                print("Tuesday")  
            if d%7==5:  
                print("Wednesday")  
            if d%7==6:  
                print("Thursday")  
            if d%7==0:  
                print("Friday")  
        elif m == 5 and 1<=d<=31:              
            if d%7==1:  
                print("Monday")  
            if d%7==2:  
                print("Tuesday")  
            if d%7==3:  
                print("Wednesday")  
            if d%7==4:  
                print("Thursday")  
            if d%7==5:  
                print("Friday")  
            if d%7==6:  
                print("Saturday")  
            if d%7==0:  
                print("Sunday")  
        elif m == 6 and 1<=d<=30:              
            if d%7==1:  
                print("Thursday")  
            if d%7==2:  
                print("Friday")  
            if d%7==3:  
                print("Saturday")  
            if d%7==4:  
                print("Sunday")  
            if d%7==5:  
                print("Monday")  
            if d%7==6:  
                print("Tuesday")  
            if d%7==0:  
                print("Wednesday")  
        elif m == 7 and 1<=d<=31:              
            if d%7==1:  
                print("Saturday")  
            if d%7==2:  
                print("Sunday")  
            if d%7==3:  
                print("Monday")  
            if d%7==4:  
                print("Tuesday")  
            if d%7==5:  
                print("Wednesday")  
            if d%7==6:  
                print("Thursday")  
            if d%7==0:  
                print("Friday")  
        elif m == 8 and 1<=d<=31:              
            if d%7==1:  
                print("Tuesday")  
            if d%7==2:  
                print("Wednesday")  
            if d%7==3:  
                print("Thursday")  
            if d%7==4:  
                print("Friday")  
            if d%7==5:  
                print("Saturday")  
            if d%7==6:  
                print("Sunday")  
            if d%7==0:  
                print("Monday")  
        elif m == 9 and 1<=d<=30:              
            if d%7==1:  
                print("Friday")  
            if d%7==2:  
                print("Saturday")  
            if d%7==3:  
                print("Sunday")  
            if d%7==4:  
                print("Monday")  
            if d%7==5:  
                print("Tuesday")  
            if d%7==6:  
                print("Wednesday")  
            if d%7==0:  
                print("Thursday")  
        elif m == 10 and 1<=d<=31:  
            if d%7==1:  
                print("Sunday")  
            if d%7==2:  
                print("Monday")  
            if d%7==3:  
                print("Tuesday")  
            if d%7==4:  
                print("Wednesday")  
            if d%7==5:  
                print("Thursday")  
            if d%7==6:  
                print("Friday")  
            if d%7==0:  
                print("Saturday")  
        elif m == 11 and 1<=d<=30:              
            if d%7==1:  
                print("Wednesday")  
            if d%7==2:  
                print("Thursday")  
            if d%7==3:  
                print("Friday")  
            if d%7==4:  
                print("Saturday")  
            if d%7==5:  
                print("Sunday")  
            if d%7==6:  
                print("Monday")  
            if d%7==0:  
                print("Tuesday")   
        elif m == 12 and 1<=d<=31:              
            if d%7==1:  
                print("Friday")  
            if d%7==2:  
                print("Saturday")  
            if d%7==3:  
                print("Sunday")  
            if d%7==4:  
                print("Monday")  
            if d%7==5:  
                print("Tuesday")  
            if d%7==6:  
                print("Wednesday")  
            if d%7==0:  
                print("Thursday")        
        else:  
            print("Error")
