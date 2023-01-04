while True:  
    s, e, d = map(int,input().split())  
    sum=0  
    if s<e:      
        for i in range(s,e+1,d):  
            sum = sum+i  
        print(sum)  
    else:  
        print("Error") 
