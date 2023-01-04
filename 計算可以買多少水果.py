while True:      
    n,money = map(int,input().split())  
    list1 =[]  
    for i in range (n):  
        a0,a1 = list(map(int,input().split()))  
        d =a1/a0  
        list1.append(d)  
         
    g = min(list1)      
    print(int(money/g))
