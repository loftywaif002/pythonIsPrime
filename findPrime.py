def is_prime(n):
    
    flag = False  
    
    k=3
    
    if (n==2 or n==3):
        flag=True
  
    elif (n%2 ==1):  

        while( k < n ):
            
            
            if(n % k ==0):
                flag = False
                    
                break
            else:
                k = k + 2
      
        else:
            flag = True
  
            
        return flag
    
n = int(input('Please enter a positive integer: '))    

for i in range(n):
    if(is_prime(i)):
        print(i)
