def finddigital(s):      
    result = "".join(filter(lambda s:s in '0123456789',b))  
    return result  
  
while True:  
    s = input().split(",")  
    for i in range(len(s)):         
        b = s[i]  
        print(finddigital(s))  
