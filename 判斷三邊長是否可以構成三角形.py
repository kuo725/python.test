t = int(input())   
   
   
for i in range(t):   
    ans1 = 0   
    ans2 = 0   
    long = list(map(int,input().split(',')))   
    for j in range(0,len(long),3):   
        a = long[j]   
        b = long[j+1]   
        c = long[j+2]   
       
        if a+b>c and b+c>a and a+c>b:   
            ans1 += 1   
        else:   
            ans2 += 1   
    print(ans1,",",ans2,sep="") 
