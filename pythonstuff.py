n = int(input("Enter the number of terms "))  
n1 = 0  
n2 = 1  
c = 0  
if n <= 0:  
    print("ANY VALUES LESS OR EQUAL TO ZERO  ARE NOT ALLOWED !!!")  
 
elif n == 1:  
    print("The Fibonacci Sequnce is : ")  
    print(n)  

else:  
    print("The Fibonacci Sequence is :")  
    while c < n:  
        print(n1)  
        n3 = n1 + n2  
      
        n1 = n2  
        n2 = n3  
        c += 1  