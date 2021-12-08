def greatest (num1, num2, num3):
       if num1 > num2:
               f1 = num1
       else:
               f1 = num2
       if num3 > num2:
              f2 = num3
       else:
              f2 = num2
       if f1>f2:
              print (f1, "is gretest")
       else:
              print (f2, "is gretest")
       return greatest

a = greatest (60,70,90)
print (a)