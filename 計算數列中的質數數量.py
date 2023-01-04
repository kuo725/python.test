import math  
while True:  
    num = list(map(int,input().split()))   
    n=0    
    for k in range(0,len(num),1):       
        if num[k] > 1:   
              
            for i in range(2,int(math.sqrt(num[k])+1)):   
                if (num[k] % i) == 0:                  
                    break   
            else:   
                n+=1  
    print(n)  
