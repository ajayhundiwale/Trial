class Cal:
       def __init__(self, a,b):
              self.a = a
              self.b = b

       def __mul__(self, a, b):
              return Cal (self.a + self.b)

       def __str__(self):
              return f"{self.a * self.b}"

               
num = Cal(3,4)

print(num)

