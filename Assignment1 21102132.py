#Q1 Program to find average of three numbers entered by user

n1=int(input("Enter the first number"))
n2=int(input("Enter the second number ="))
n3=int(input("Enter the third number ="))
avg=(n1+n2+n3)/3
print("The average of three numbers =",avg)

#Q2 Program to compute a person's income tax

grossincome=int(input("enter gross income"))
dependent=int(input("number of dependent"))
taxincome=gross_income-10000-(dependent*3000)
tax=0.2*taxincome  #Tax rate is 20%
print("The person has to pay",tax)

#Q3 Program to store different data types values into a list

n1=int(input("Number of students"))
lts=["Sid","Name","Gender","CourseName","CGPA"]
for i in range(n1):
    kllst=[]
    Sid=int(input("Enter sid:"))
    Name=input("Enter name :")
    Gender=input("Enter the gender:")    #Gender should be F/M and U for unknown
    cname=input("Enter the Course Name:")
    cg=float(input("Enter CGPA:"))
    kllst.append(Sid)
    kllst.append(Name)
    kllst.append(Gender)
    kllst.append(cname)
    kllst.append(cg)
    print(lts)
    print(kllst)

#Q4 Program to enter marks of 5 students into a list and display them in sorted manner

l1=float(input("Enter marks of first student:"))
l2=float(input("Enter marks of second student:"))
l3=float(input("Enter marks of third student:"))
l4=float(input("Enter marks of fourth student:"))
l5=float(input("Enter marks of fifth student:"))
slst=[l1,l2,l3,l4,l5]
slst.sort()
print(slst)

#Q5
   #(a)
color=["Red","Green","White","Black","Pink","Yellow"]
color.pop(3)
print(color)
   #(b)
color[3]="Purple"
print(color)