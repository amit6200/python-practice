#1 How to print spaces in Python

# space=' '
# x = 10
# y = 20
# print("Hello" ,space*5,"world")
# print("x:",space*10,x)
# print("y:",space*10,y)

#2 Python program to print text/string using user-defined method
# def putMe(text):
#     print(text)
# putMe('Hello')    

#3 print their values, types and Ids
# a=10
# print(type(a),id(a))
# b=10.0
# print(type(b),id(b))

#4 Python Scope of Variables with Example
# a=10
# def fun():
#     b=20
#     print("a: ", a, "b: ", b)
# fun()

#5 Python program to determine the type of objects
# a=[10,20,30,40]
# print(type(a))

#6 python program complex no
# c=10+2j
# print(type(c)) 

# recursion
#7 find the sum of n natural no
# def sum(n):
#     if n==1:
#         return 1
#     return n + sum(n-1)
# print(sum(10)) 

# 8 input two integer find sum 
# a=int(input("Enter a: "))
# b=int(input("Enter b: "))
# c=a+b
# print("The sum of a and b is: ",c)

# 9 find maximum of two number
# a=10
# b=12
# print(max(a,b))

# 10 area of circle & perimeter of circle
# PI=3.14
# r=float(input("Enter redius of circle: "))
# area=PI*r*r
# perimeter=2*PI*r
# print("area is: ",area)
# print("perimeter is: ",perimeter)

# 11 ASCII value
# char='A'
# print(ord(char)) 

# 12 simple interest
# p=int(input("Enter amount: "))
# r=int(input("Enter rate: "))
# t=int(input("Enter time: "))
# simple_interest=(p*r*t)/100
# print(simple_interest)

# 13 josephus problem
# def jos(n,k):
#     if(n==1):
#         return 0
#     return (jos(n-1,k)+k)%n
# print(jos(5,3))

#14 reverse string

# a=input("Enter string: ")
# print(a[-1::-1])

# a=input("Enter string: ")
# for i in range((len(a)-1),-1,-1):
#     print(a[i],end="")


# 15 reverse number
# i=int(input("Enter Number: "))
# rev=0
# while(i>0):
#     rev=(rev*10)+i%10
#     i=i//10
# print(rev)    

# #16 palindrome string and number
# x=int(input("Enter number "))
# rev=0
# a=x
# while(x>0):
#     rev=(rev*10)+x%10
#     x=x//10
# if a==rev:
#     print("palindrome")
# else:
#     print("Not palindrome")

#17 palindrome string
# s=input("Enter a string: ")
# a=s[-1::-1]
# if s==a:
#     print("Palindrome")
# else:
#     print("Not palindrome")    

# print natural number
# a=1
# while(a<=10):
#     print(a)
#     a=a+1 
# i=1
# for i in range(1,11):
#     print(i)

# print n natural number
# n=int(input("Enter number: "))
# i=1
# while(i<=n):
#     print(i)
#     i=i+1

# n=int(input("Enter number: "))
# for i in range(1,n+1):
#     print(i)

# print reverse n number
# i=10
# while(i>=1):
#     print(i)
#     i=i-1

# print  sum of n number
# n=int(input("Enter Number: "))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+i
#     i=i+1
# print(sum) 

# n=int(input("Enter number: "))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
#     i=i+1
# print(sum)    

# Sum of square 
# n=int(input("Enter Number: "))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+(i*i)
#     i=i+1   
# print(sum) 

# n=int(input("Enter your number "))
# sum=0
# for i in range(1,n+1):
#     sum=sum+(i*i)
#     i=i+1
# print(sum)   

# n=int(input("Enter your number "))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+(i*i*i)
#     i=i+1 
# print(sum)   

# print even number 1 to n
# n=int(input("Enter number: "))
# i=2
# while(i<=n):
#     print(i)
#     i=i+2
# print(i)    

# print odd number in 1 to 10
# n=int(input("Enter number: "))
# i=1
# while(i<=n):
#     print(i)
#     i=i+2
# print(i) 

# sum of even number 1 to n
# n=int(input("Enter number: "))
# i=2
# sum=0
# while(i<=n):
#     sum=sum+i
#     i=i+2
# print(sum)  

# sum of odd number 1 to n
# n=int(input("Enter number: "))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+i
#     i=i+2
# print(sum)  
     
# sum of given digit
# i=int(input("Enter number: "))
# sum=0
# while(i>0):
#     sum=sum+i%10
#     i=i//10
# print(sum)    
   
# product of given digit
# i=int(input("Enter your number: "))
# pro=1
# while(i>0):
#     pro=pro*(i%10)
#     i=i//10
# print(pro) 

# sum of square of digits of a given number
# n=int(input("Enter your number: "))
# sum=0
# while(n>0):
#     sum=sum+(n%10)*(n%10)
#     n=n//10
# print(sum) 

# sum of cube of digits
# n=int(input("Enter your number "))
# sum=0
# while(n>0):
#     sum=sum+(n%10)*(n%10)*(n%10)
#     n=n//10
# print(sum)       

# Armstrong number
# n=int(input("Enter your number: "))
# x=n
# sum=0
# while(n>0):
#     sum=sum+(n%10)*(n%10)*(n%10)
#     n=n//10
# if(x==sum):
#     print("Armstrong")
# else:
#     print("not Armstrong")     
 
# reverse number
# n=int(input("Enter n: "))
# rev=0
# while(n>0):
#     rev=rev*10+n%10
#     n=n//10
# print(rev) 

# palindrome 
# n=int(input("Enter your number: "))
# x=n
# rev=0
# while(n>0):
#     rev=rev*10+n%10
#     n=n//10
# if(x==rev):
#     print("Palindrome")
# else:
#     print("Not palindrome") 

# prime number
# n=int(input("Enter your number: "))
# if(n%2==0):
#     print("prime")
# else:
#     print("Not prime")

# factorial
# i=int(input("Enter N: "))
# fact=1
# while(i>0):
#     fact=fact*i
#     i=i-1
# print(fact)    
 
# fibnacci serise   
# n=int(input("Enter N: "))
# x=0
# y=1
# z=0
# while(z<=n):
#     print(z)
#     x=y
#     y=z
#     z=x+y 

# star pattern 
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1   
 
# reverse star 
# i=1
# while(i<=5):
#     b=1
#     while(b<=5-i):
#         print(" ",end="")
#         b=b+1
#     r=1
#     while(r<=i):
#         print("*",end="")
#         r=r+1
#     print()
#     i=i+1    

# print pyramid
# a=1          
# i=1
# while(i<=9):
#     j=1
#     while(j<=9-i):
#         print(" ",end="")
#         j=j+1
#     k=1    
#     while(k<=a):
#         print("*",end="")
#         k=k+1
#     a=a+2    
#     print()
#     i=i+1  
            
# reverse number
# n=int(input("Enter N: "))
# rev=0 
# while n>0:
#     rem=n%10
#     rev=rev*10+rem
#     n=n//10
# print(rev)               

# factorial
# n=int(input("Enter N: "))        
# fact=1
# while n>0:
#     fact=n*fact
#     n=n-1
# print(fact) 

# lambda expression
# f=lambda a,b:a+b
# print(f(1,4)) 

# f=lambda n: 1 if n==0 else n*f(n-1)
# print(f(5)) 

# how to create multivariable argument
# def avg(*t):
#     avg=sum(t)/len(t)
#     print(avg)
# avg(10,2030)    

# reverse
# s="Amit"
# print(s[::-1])  

# Palindrome 
# s="aba"
# x=s
# a=s[::-1]
# if x==a:
#     print("palindrome")  
# else:
#     print("Not palindrome")   

# x=121
# a=x
# rev=0
# while x>0:
#     rem=x%10
#     rev=rev*10+rem 
#     x=x//10
# print(rev)
# if a==rev:
#     print("palindrome")
# else:
#     print("Not palindrome") 

# find comman letter in string
# a=input("Enter str1: ") 
# b=input("Enter str2: ")
# s1=set(a)
# s2=set(b)
# k=s1&s2
# print(k)  

# combaine two list
# a=[1,2,3,4]
# b=["one","two","three","four"]
# c=dict(zip(a,b))
# print(c)

# find missing number in python array
# a=[1,2,4,5,6]
# n=a[-1]
# sum1=0
# total=n*(n+1)//2
# sum1=sum(a)
# k=total-sum1
# print(k)

# pair of sum
# def sumTwo(arr,sum):
#     arr.sort()
#     left=0
#     right=len(arr)-1
#     while(left<=right):
        
#         if(arr[left]+arr[right]>sum):
#             right= right-1
#         elif(arr[left]+arr[right]<sum):
#             left= left+1
#         elif(arr[left]+arr[right]==sum):
#            print(arr[left],arr[right])
#            right=right-1
#            left=left+1
# arr=[1,2,4,5,6,7,15]
# sum=13
# sumTwo(arr,sum) 

# arr=[1,2,3,3,4,5,4,1,2] 
# remove_dupli=lambda arr:set (arr)
# print(remove_dupli(arr))              
     
# n=int(input("Enter number"))
# a=0
# b=1
# c=0
# while c<=n:
#     print(c) 
#     a=b
#     b=c
#     c=a+b    
     
             
# n=int(input("Enter N: "))
# x=0
# y=1
# z=0
# while z<=n:
#     print(z,end=" ")
#     x=y
#     y=z
#     z=x+y

# def two_Sum(arr,sum):
#     arr.sort()
#     l=0
#     r=len(arr)-1
#     while(l<=r):
#         if(arr[l]+arr[r]>sum):
#             r=r-1
#         elif(arr[l]+arr[r]<sum):
#             l=l+1
#         elif(arr[l]+arr[r]==sum):
#             print(arr[l],arr[r])
#             r=r-1
#             l=l+1
# arr=[12,13,1,5,7]
# sum=6            
# two_Sum(arr,sum) 

# n=int(input("Enter number: "))
# fact=1
# while n>0:
#     fact=fact*n
#     n=n-1
# print(fact)
                   
# i=2
# while i<=10:
#     print(i,end=" ")
#     i=i+2        
    
# n=int(input("Enter n: "))
# sum=0
# while n>0:
#     sum=sum+(n%10)*(n%10)*(n%10)
#     n=n//10
# print(sum)    




    
          