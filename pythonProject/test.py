# print("hello")

# a=10
# b=20
# c=a+b
# print(c)

# a,b,c=1,2,3
# print(a,b,c)
# print(id(a),id(b),id(c))

# a,b,c=3,1,2
# print(a,b,c)
# print(id(a),id(b),id(c))

# x=y=z=4
# print(x,y,z)

# x=23
# print(type(x))

# x=10.75
# print(type(x))

# x='A'
# print(type(x))

# Not Allowed 
# 1x=100
# x$1=2000
# x-1=2
# if=1
# print(if)

# _x=10
# print(_x)

# _=20
# print(_)

# import keyword
# # printing all keywords at once using "kwlist()"
# print("The list of keywords is : ")
# print(keyword.kwlist)

# # The list of keywords is : 
# x=['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# count=0
# for i in x:
#     count = count+1
#     print("The Number Of Items in List are: ", count,i)

# Variable are case sensitive
# a=10
# A=20
# print(a)
# print(A)

# List (Mutable)
# a=[1,2,3,4,5,6]
# print(a,type(a),id(a))

# a[0]=2
# print(a,type(a),id(a))

# a[4]=10
# print(a,type(a),id(a))

# a=(1,2,3,4,5,6)
# print(a,type(a),id(a))

# a[0]=2
# print(a,type(a),id(a))

'''
(1, 2, 3, 4, 5, 6) <class 'tuple'> 139800398679776
Traceback (most recent call last):
File "/mnt/e/study-python/udemy-adbul-bari/pythonProject/test.py", line 72, in <module>
    a[0]=2
TypeError: 'tuple' object does not support item assignment
'''

# s="Ashish is a nice man"
# print(s,",","length of string is:",len(s),",",id(s))

# s[15]="A"

'''
Ashish is a nice man , length of string is: 20 , 140279074987488
Traceback (most recent call last):
File "/mnt/e/study-python/udemy-adbul-bari/pythonProject/test.py", line 86, in <module>
    s[15]="A"
TypeError: 'str' object does not support item assignment
'''
# value = bytearray([72, 101, 108, 108, 111])  
# print(value)

# data=b'Hello'
# print(data)

# value = bytearray([75, 110, 115, 125, 254])  
# print(value)

# A = input("Please enter a character: ")     
# print ("The ASCII value of '" + A + "' is ", ord(A))  

'''
ASCII Table
Dec  = Decimal Value
Char = Character

'5' has the int value 53
if we write '5'-'0' it evaluates to 53-48, or the int 5
if we write char c = 'B'+32; then c stores 'b'


Dec  Char                           Dec  Char     Dec  Char     Dec  Char
---------                           ---------     ---------     ----------
0  NUL (null)                      32  SPACE     64  @         96  `
1  SOH (start of heading)          33  !         65  A         97  a
2  STX (start of text)             34  "         66  B         98  b
3  ETX (end of text)               35  #         67  C         99  c
4  EOT (end of transmission)       36  $         68  D        100  d
5  ENQ (enquiry)                   37  %         69  E        101  e
6  ACK (acknowledge)               38  &         70  F        102  f
7  BEL (bell)                      39  '         71  G        103  g
8  BS  (backspace)                 40  (         72  H        104  h
9  TAB (horizontal tab)            41  )         73  I        105  i
10  LF  (NL line feed, new line)    42  *         74  J        106  j
11  VT  (vertical tab)              43  +         75  K        107  k
12  FF  (NP form feed, new page)    44  ,         76  L        108  l
13  CR  (carriage return)           45  -         77  M        109  m
14  SO  (shift out)                 46  .         78  N        110  n
15  SI  (shift in)                  47  /         79  O        111  o
16  DLE (data link escape)          48  0         80  P        112  p
17  DC1 (device control 1)          49  1         81  Q        113  q
18  DC2 (device control 2)          50  2         82  R        114  r
19  DC3 (device control 3)          51  3         83  S        115  s
20  DC4 (device control 4)          52  4         84  T        116  t
21  NAK (negative acknowledge)      53  5         85  U        117  u
22  SYN (synchronous idle)          54  6         86  V        118  v
23  ETB (end of trans. block)       55  7         87  W        119  w
24  CAN (cancel)                    56  8         88  X        120  x
25  EM  (end of medium)             57  9         89  Y        121  y
26  SUB (substitute)                58  :         90  Z        122  z
27  ESC (escape)                    59  ;         91  [        123  {
28  FS  (file separator)            60  <         92  \        124  |
29  GS  (group separator)           61  =         93  ]        125  }
30  RS  (record separator)          62  >         94  ^        126  ~
31  US  (unit separator)            63  ?         95  _        127  DEL
'''

# a=0.00000000001259
# print(a)

# a=12.5E-2
# print(a)

# a=2+5j
# b=1+1j
# c=a+b
# d=a-b
# e=a/b
# print(c,d,e)

# a=int(input("Enter any value: "))
# print(a,type(a))

# a=float(input("Enter any value: "))
# print(a,type(a))

# a=input("Enter any string:")
# print(a,type(a))

# a=123_456_789
# print(a,type(a))

# a=100
# print(bin(a))
# print(oct(a))
# print(hex(a))

# x=0b1111
# print(hex(x))

# x=125
# print(bin(x))

# a=int(input("Enter any binary number: "),2)
# print(a,type(a))

# a=34567
# print(oct(a))

# a=12.56
# print(int(a))
# print(complex(a))
# print(str(a))

# a=True
# print(a,type(a))
# print(int(a))
# print(float(a))
# print(complex(a))
# print(str(a))

# s3=0b10101010
# print(int(s3),2)

# a=(2+3)**5/2*20
# print(a,type(a))

# x=2**3**2
# print(x,type(x))

# Mathematical Expression In Python
# Area of rectangle
# length_of_rectangle=int(input("Enter length of rectangle: "))
# breadth_of_rectangle=int(input("Enter breadth of rectangle: "))
# area_of_rectangle=length_of_rectangle*breadth_of_rectangle
# print("area of rectangle is:",area_of_rectangle,type(area_of_rectangle))

# Area of Triangle
# b=int(input("Enter the base of triangle: "))
# h=int(input("Enter the height of triangle: "))
# area_of_triangle = 1/2*b*h
# print("Area of Triangle is:", area_of_triangle,type(area_of_triangle))

# Area of Trapezium
# b=int(input("Enter the base of triangle: "))
# h=int(input("Enter the height of triangle: "))
# area_of_triangle = 1/2*b*h
# print("Area of Triangle is:", area_of_triangle,type(area_of_triangle))

# Distance displacement in physics
# v=u+a*t
# s=(u*t)+(1/2*a*t**2)

# v=int(input("Enter The final velocity of an object: "))
# u=int(input("Enter The initial velocity of an object: "))
# a=float(input("Enter The acceleration of an object: "))  # 9.80665 m/s²
# time_taken = (v-u)/a
# displacement=(v**2-u**2)/2*a
# print("The time taken for the object will be: ",time_taken)
# print("The displacement for the object will be: ",displacement)

# Area of Circle
# import math
# radius=float(input("Enter the value of radius: "))
# area_of_circle=math.pi*radius*radius
# print("Area of Circle will be: ",area_of_circle)

# Area of Cuboid
# length = float(input('Enter Length: '))
# breadth = float(input('Enter Breadth: '))
# height = float(input('Enter Height: '))
# area = 2 * (length * breadth + length * height + breadth * height)
# print('Total Surface Area of Cuboid is:', area)

# Roots Quadratic Equation
# ax²+ bx + c = 0

# a=int(input("Enter the value of a: "))
# b=int(input("Enter the value of b: "))
# c=int(input("Enter the value of c: "))
# x=(-b+(b**2-4*a*c)**1/2)/(2*a)
# y=(-b-(b**2-4*a*c)**1/2)/(2*a)
# print("The First Root Of the Equation is =",x)
# print("The Second Root Of the Equation is =",y)

# a=int(input("Enter any decimal number a: "))
# b=int(input("Enter any decimal number b: "))
# print("Binary value of a will be:",bin(a))
# print("Binary value of b will be:",bin(b))
# c=a&b
# d=a|b
# e=a^b
# f=~a
# g=a<<1
# h=a>>1
# i=a<<2
# print(c,"Binary value of c a&b will be:",bin(c),type(c))
# print(d,"Binary value of d a|b will be:",bin(d),type(d))
# print(e,"Binary value of e a^b will be:",bin(e),type(e))
# print(f,"Binary value of f ~a will be:",bin(f),type(f))
# print(g,"Binary value of g a<<1 will be:",bin(g),type(g))
# print(h,"Binary value of h a>>1 will be:",bin(h),type(h))
# print(i,"Binary value of i a<<2 will be:",bin(i),type(i))

# Conditional Statement
# a=int(input("Enter any value a: "))
# b=int(input("Enter any value b: "))
# if (a-b)>=0:
#     print(a-b)
# else:
#     print(b-a)

# a=int(input("Enter any value a: "))
# if(a%2==0):
#     print("The number entered",a,"is","even")
# else:
#     print("The number entered",a,"is","odd")

# marks=int(input("Enter Marks of Student: "))
# if marks>=0 and marks<=100:
#     print("Marks entered",marks,"is valid")
# else:
#     print("Marks entered",marks,"is invalid")

# gender=input("Enter the gender of person: ")
# if gender=='m' or gender=='M' or gender=='male' or gender=='Male':
#     print("The gender of the person is Male")
# elif gender=='f' or gender=='F' or gender=='female' or gender=='Female':
#     print("The gender of the person is Female")
# else:
#     print("Enter the correct gender name")

# age=int(input("Enter the age of person: "))
# if age>=18 and age<=60:
#     print("The person of age",age,"is eligible to work")
# else: 
#     print ("The person of age",age,"is not eligible to work")

# sub1=int(input("Enter Marks of Student of in subject1: "))
# sub2=int(input("Enter Marks of Student of in subject2: "))
# sub3=int(input("Enter Marks of Student of in subject3: "))
# total_marks_obtained=sub1+sub2+sub3
# per=(total_marks_obtained/300)*100
# if per >= 40:
#     print("The student getting",per,"is passed")
# else:
#     print("The student getting",per,"percentage is failed")

# Eldest Between Three
# john=float(input("Enter the age of john: "))
# smith=float(input("Enter the age of smith: "))
# ajay=float(input("Enter the age of ajay: "))
# if john>smith and john>ajay:
#     print("john is eldest")
# elif smith>john and smith>ajay:
#     print("smith is eldest")
# else:
#     print("ajay is eldest")

# Calculate Discounted Amount
# amount=float(input("Enter the amount of the items purchased: "))
# if amount<=1000:
#     dis_amount=amount*10/100
#     cost_of_item=amount-(dis_amount)
#     profit=(amount-cost_of_item)/amount*100
#     print("The discounted amount is:",amount)
#     print("The cost of item is:",cost_of_item)
#     print("The percentage of profit on item purchased is:",profit)    
# elif amount>1000 and amount<=5000:
#     dis_amount=amount*20/100
#     cost_of_item=amount-(dis_amount)
#     profit=(amount-cost_of_item)/amount*100
#     print("The discounted amount is:",amount)
#     print("The cost of item is:",cost_of_item)
#     print("The percentage of profit on item purchased is:",profit)
# elif amount>5000 and amount<=10000:
#     dis_amount=amount*30/100
#     cost_of_item=amount-(dis_amount)
#     profit=(amount-cost_of_item)/amount*100
#     print("The discounted amount is:",amount)
#     print("The cost of item is:",cost_of_item)
#     print("The percentage of profit on item purchased is:",profit)
# else:
#     amount>10000
#     dis_amount=amount*50/100
#     cost_of_item=amount-(dis_amount)
#     profit=(amount-cost_of_item)/amount*100
#     print("The discounted amount is:",amount)
#     print("The cost of item is:",cost_of_item)
#     print("The percentage of profit on item purchased is:",profit)

# Leap Year Or Not
# year=int(input("Enter the year: "))

# # divided by 100 means century year (ending with 00)
# # century year divided by 400 is leap year
# if (year % 400 == 0) and (year % 100 == 0):
#     print("{0} is a leap year".format(year))

# # not divided by 100 means not a century year
# # year divided by 4 is a leap year
# elif (year % 4 ==0) and (year % 100 != 0):
#     print("{0} is a leap year".format(year))

# # if not divided by both 400 (century year) and 4 (not century year)
# # year is not leap year
# else:
#     print("{0} is not a leap year".format(year))

# s1="America"
# s2="Brazil"
# print(s1<s2)

# s1="Brazil"
# s2="brazil"
# print(s1<s2)

# s1="America"
# s2="antarctica"
# print(s1<s2)

# s1="Brazil"
# s2="brazil"
# print(s1==s2)

# s1="America"
# s2="Brazil"
# print(s1!=s2)

# print(0 and 6)
# print(6 and 0)
# print(5 and 6)

# print(0 or 6)
# print(6 or 0)
# print(6 or 7)

# print('' or 'hi')
# print('hi' or '')
# print('hi' or 'bye')

# print('hi' and '')
# print('' and 'hi')

# Bitwise Operators
# a=int(input("Enter any decimal number: "))
# print(a,bin(a),a.bit_length())

# a=int(input("Enter any decimal number: "))
# x=int(input("Enter any number that we want to shift Left: "))
# b=a<<x
# print(a,bin(a),a.bit_length())
# print(b,bin(b),b.bit_length())

# a=int(input("Enter any decimal number: "))
# x=int(input("Enter any number that we want to shift Right: "))
# b=a>>x
# print(a,bin(a),a.bit_length())
# print(b,bin(b),b.bit_length())

# a=int(input("Enter any number: "))
# b=int(input("Enter any number: "))
# print("Both are having the same memory space:",a is b,id(a),id(b))
# print("Both are not having the same memory space:",a is not b,id(a),id(b))

# count=0
# while count<10:
#     print(count,"Hello")
#     count=count+1

# n=int(input("Enter any number: "))
# while n>0:
#     r=n%10
#     n=n//10
#     print(r)

# Display Multiplication Table of a given number
# n=int(input("Enter any number: "))
# count=1
# while count<=10:
#     x=n*count
#     print(n,"x",count,"=",x)
#     count=count+1

# 1 counting the number of a digits in a number
# 2 Find sum of digits in a number
# 3 Reversing a number
# 4 Check if a number is Palindrome

# 1 counting the number of a digits in a number
# n=int(input("Enter any number: "))
# count=0
# while n>0:
#     n=n//10
#     count=count+1
# print("Number of digits are:",count)

# 2 Find sum of digits in a number
# n=int(input("Enter any number: "))
# count=0
# sum=0
# while n>0:
#     r=n%10
#     n=n//10
#     sum=sum+r
#     count=count+1
# print("Sum of digits are",sum)

# 3 Reversing a number
# n=int(input("Enter any number: "))
# rev=0
# while n>0:
#     r=n%10  
#     n=n//10
#     rev=rev*10+r
# print("Reverse Number is:",rev)

# # 4 Check if a number is Palindrome
# n=int(input("Enter any number: "))
# m=n
# rev=0
# while n>0:
#     r=n%10  
#     n=n//10
#     rev=rev*10+r
# print("Reverse Number is:",rev)
# if m == rev:
#     print("Number is palindrome")
# else:
#     print("Number is not palindrome")

# # 1 Find Sum of given numbers as Input
# num_of_nos=int(input("Enter the times numbers to be added: "))
# sum=0
# count=0
# while count<num_of_nos:
#     n=int(input("Enter the numbers as times to be added: "))
#     sum=sum+n
#     count=count+1
# print("The sum of all entered numbers are:",sum)

# # Sum of all Positive and Negative Numbers Separately
# num_of_nos=int(input("Enter the times numbers to be added: "))
# psum=0
# nsum=0
# count=0
# while count<num_of_nos:
#     n=int(input("Enter the numbers as times to be added: "))
#     if n>0:
#         psum=psum+n
#     else:
#         nsum=nsum+n
#     count=count+1
# print("Sum of Positive numbers are:",psum)
# print("Sum of Negative numbers are:",nsum)

# # 3 Maximum number from the given input numbers
# num_of_nos=int(input("Enter the times numbers to be print: "))
# max=int(input("Enter the number: "))
# count=0
# while count<num_of_nos-1:
#     n=int(input("Enter the numbers as times to be compare: "))
#     if n>max:
#         max=n
#     count=count+1
# print("The Maximum number:",max)

# # Guess a number b/w a 1-100
# import random
# n=random.randint(1,1000)
# guess=0
# while guess!=n:
#     guess=int(input("Guess a number from 1 to 1000: "))
#     if guess<n:
#         print("The number is lesser")
#     elif guess>n:
#         print("The number is larger")
#     else:
#         print("Yes you get the number")

# # Infinite Loop - Continue - Break - Pass 
# while True:
#     n=int(input("Enter any number: "))
#     if n>0:
#         print("Positive")
#     else:
#         print("Negative")

# while True:
#     n=int(input("Enter any number: "))
#     if n>0:
#         print("Positive")
#     elif n<0:
#         print("Negative")
#     else:
#         break

# count=0
# while count<10:
#     print(count)
#     count=count+1
#     if count>5:
#         break

# # Continue
# count=0
# while count<10:
#     n=int(input("Enter any number: "))
#     if n%3==0:    
#         continue
#     print(n)
#     count=count+1

# # Pass
count=0
while count<10:
    n=int(input("Enter any number: "))
    if n%3==0:    
        pass
    else:
        print(n)
    count=count+1
