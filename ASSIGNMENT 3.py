def Factoriyal():
   
   num = int(input('enter number:'))
   fact =1

   if( num == 0):
        print("Factoriyal number enter number {} ".format(num,fact))
   else:

     for i in range(1,num+1):
        fact=fact * i
        i=i+1

   print("enter number of faco {} of {}'" .format(num,fact))

Factoriyal()



number=int(input('enter your choice number:'))
import math
print(math.ceil(number))

print(math.factorial(number))
print(math.sqrt(number))
print(math.log(number))
print(math.radians(number))
