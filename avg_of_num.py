# count = int(input("Enter count of Total Number: "))
# i = 0
# sum =0
# for i in range(count):
#        x = int(input("Enter an integer: "))
#        sum = sum + x
# avg = sum/count
# print("The average is", avg)
# ---------------------------------------------------------------------------------------------
# x=0
# for i in range(0,5):
#        x = x+1
# print(x)
# ---------------------------------------------------------------------------------------------------

count = int(input("Enter count of Total Number: "))
i = 0
sum = 0
while i<=count:
       if i == count: 
              break   
       x = int(input("Enter an integer: "))
       sum = sum + x
       i += 1
avg = sum/count
print("The average is", avg)
