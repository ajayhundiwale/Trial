num =int(input("Enter number: "))
prime = True
for i in range (2, num):
       if (num%i==0):
              prime = False
if prime:
       print (num, "is prime number")
else:
       print (num, "is not a prime number")


