def n_to_d(num,n):  
    num = "".join(reversed(str(num)))  
    result = 0  
    for i in range(len(num)):  
        result += (n**i)*int(num[i])  
    return result  
  
def d_to_n(num,n):  
    k=''  
    while True:  
        k = str(num%n)+k  
        num = num//n  
        if num<n:  
            k=str(num)+k  
            break  
    return int(k)  
  
while True:  
    n, num1, num2 = input().split(",")  
    n = int(n)  
    num1 = int(num1)  
    num2 = int(num2)  
    print(d_to_n(n_to_d(num1,n)+n_to_d(num2,n),n))
