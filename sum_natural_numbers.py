def sumnatural(n):
       if n==1:
              return 1
       else:
              return sumnatural(n-1) + (n)
       # count = int (input("Enter number of integer: "))
       # i =1
       # while count>= i:
       #        num1 = int(input("Enter number: "))
       #        count = count -1
       

a = sumnatural(5)
print(a)