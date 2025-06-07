Task 1:

stu1={'Ram':480,'sham':450,'Amit':280,'Vikram':410}
name = input("enter student name :")

if name in stu1:
 
 print(name,"is mark",stu1[name])
else:
 print('Student is not found')


Task 2: Demonstrate List Slicing 




List_number=[]

for a in range(10):
    x=int(input("my_list:"))
    List_number.append(x)
print("original list",List_number)

my_list=[]
for i in List_number[0:5]:
    s= i 
    my_list.append(s)
print("first five elements from list",my_list)
my_list.reverse()
print("reverse extraacted number",my_list)