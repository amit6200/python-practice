# try:
#     x=10
#     y=0
#     z=x/y
#     print(z)
# except:
#     print("an exception occ") 
# else:
#     print("no error in previous ")
# finally:
#     print("This is the finally block")     

# l=[20,2,3,5,4,1]
# ev_list=[x for x in l if x%2==0]
# print(ev_list) 

# def fibo(n):
#     x=0
#     y=1
#     z=0
#     while z<=n:
#         print(z)
#         x=y
#         y=z
#         z=x+y
# fibo(7)  

# name="Amit"
# age=20
# str="my name is {} and age is {}"
# print(str.format(name,age))  

# f=open("file name","r")
# print(f)

# # income tax calculator

# tax_rate=.20
# standard_deduction=10000.0
# dependent_deduction=3000.0
# grossIncome=float(input("Enter the gross income "))
# numDependent=int(input("Enter the number of dependents: "))
# taxableIncome=grossIncome-standard_deduction-(dependent_deduction*numDependent) 
# incomeTax=taxableIncome*tax_rate
# print(incomeTax) 

# compute the area of tringle
# base=float(input("Enter tringle base "))
# height=float(input("Enter tringle height "))
# area=.5*base*height
# print("area of tringle is ",area)  

# compute the area of circle
# radius=float(input("Enter radius of circle "))
# area=3.14*(radius**2)
# print(area)

# x="dog"
# y="cat"
# print(x +" "+ y)
# print("the "+x+" chase the "+y)
# print(x * 4)

# for i in range(10,0,-1):
#     print(i,end=" ")
# for count in range(5):
#    print(count + 1)
# for count in range(1, 4):
#    print(count)
# for count in range(1, 6, 2):
#    print(count)
# for count in range(6, 1, -1):
#     print(count)  

# for value in range(128):
#     print(f"ASCII Value: {value},Character: {chr(value)}")

# sum=0.0
# data=input("Enter a number or just enter quit: ")
# while data !="":
#     number=int(data)
#     sum += number
#     data=input("Enter number or just quit: ")
# print(sum)    

# theSum = 0
# for i in range(1, 11):
#  theSum += i
# print(theSum)

# sum=0
# count=1
# while count<11:
#     sum+=count
#     count +=1
# print(sum)    

# for i in range(10,0,-1):
#     print(i ,end=" ")
# print()    
    
# i=10
# while i>=1:
#     print(i,end=" ")
#     i -= 1

# import random
# for roll in range(10):
#     print(random.randint(1,6),end=" ")

# import random
# smaller=int(input("Enter the smaller number: "))
# larger=int(input("Enter larger number: "))
# mynumber=random.randint(smaller,larger)
# count=0
# while True:
#     count+=1
#     userNumber=int(input("Enter your guess: "))
#     if userNumber<mynumber:
#         print("Too small")
#     elif userNumber>mynumber:
#         print("Too large")    
#     else:
#         print("Congratulations ! You have got",count,"tries")
#         break

# x = 5
# y = 4
# if x > y:
#  print( y )
# else:
#  print( x )

# data="Hi there"
# for index in range(len(data)):
#     print(index,data[index])

# binary to decimal convert

# n=input("Enter a binary number: ")
# l=list(n)
# sum=0
# l.reverse()
# # print(l)
# for i in range(len(l)):
#     sum=sum+int(l[i])*2**i
# print(sum) 

# n="amit"
# print(n.split())

# s="Hi there"
# # print(len(s))
# # print(s.center(11))
# # print(s.count('e'))
# # print(s.endswith("there"))
# # print(s.startswith("Hi"))
# # print(s.find("the"))
# # print(s.isalpha())
# a=s.split()
# print(" ".join(a))

# data="Python rules!"
# print(data.split())
# print(data.upper())
# print(data.find("rules"))
# a=data.replace("!","?")
# print(a)
# print(data.endswith("i"))  
# print(" totally ".join(data.split()))

# f=open("myfile.txt", 'w')
# f.write("First line. \nSecond line.\n")
# f.close()

# import random
# f=open("Integer.txt",'w')
# for i in range(1,51):
#     f.write(str(i)+'\n')
# f.close()   

# f=open("Integer.txt", 'r') 
# text=f.read()
# print(text)

# f=open("Integer.txt","r")
# sum=0
# for i in f:
#     i=i.strip()
#     n=int(i)
#     sum += n
# print(sum)  

# print(list("HI there")) 

a=[1,2,3,4]
# print(a+[7,8]) 
# b=[1,2,3,4]
# print(a==b)
# a[3]=0
# print(a)

# Square of list
# for i in range(len(a)):
#     a[i]=a[i]**2
# print(a) 

# aList = [34, 45, 67]
# target = 34
# if target in aList:
#  print(aList.index(target))
# else:
#  print(-1)   

# f=[10,20,30,40]
# s=f
# print(f)
# print(s)
# f[1]=99
# print(f)
# print(s)

data=[5,3,7]
# print(data[2])
# print(len(data))
# print(data[0:2])
# print(0 in data)
# print(data+[2,10,5])
# print(tuple(data))
# data[0]=1
# print(data)
# data.append(10)
# print(data)
# data[2]=22
# print(data)
# print(data.pop(1))
# print(data)

# newdata=[1,2,3]
# print(data+newdata)
# print(data.index(7)
# data.sort()
# print(data)

# def square(x):
#     return x*x
# print(square(4))

# def avg(l):
#     sum=0
#     for i in l:
#         sum +=i
#     return sum/len(l)
# print(avg([10,12]))

# def avg(l):
#     sum=0
#     for i in l:
#         sum +=i
#     return sum/len(l)
# print(avg([10,22])) 

# def main():
#     n=float(input("Enter N: "))
#     result=square(n)
#     print(result) 
# def square(n):
#     return n*n
# if __name__=="__main__":
#     main() 

# def even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# print(even(4))   

# def summation(low,high):
#     return low+high
# print(summation(1,2))     
 
   
# generate sentence 
# import random
# articles = ("A", "THE")
# nouns = ("BOY", "GIRL", "BAT", "BALL")
# verbs = ("HIT", "SAW", "LIKED")
# prepositions = ("WITH", "BY")  

# def sentence():
#  """Builds and returns a sentence."""
#  return nounPhrase() + " " + verbPhrase()
# def nounPhrase():
#  """Builds and returns a noun phrase."""
#  return random.choice(articles) + " " + random.choice(nouns)
# def verbPhrase():
#  """Builds and returns a verb phrase."""
#  return random.choice(verbs) + " " + nounPhrase() + " " + \
#  prepositionalPhrase()
# def prepositionalPhrase():
#  """Builds and returns a prepositional phrase."""
#  return random.choice(prepositions) + " " + nounPhrase()
# def main():
#     number = int(input("Enter the number of sentences: "))
#     for count in range(number):
#         print(sentence())
# if __name__ == "__main__":
#    main()        

# info={}
# info["name"]="amit"
# info["age"]=20
# print(info)
# info["age"]=21
# print(info)
# print(info["age"])
# if "age" in info:
#     print(info.get("age"))
# print(info.pop("age"))
# print(info)
# for key in info:
#     print(key,info[key])

# grades = {90:'A', 80:'B', 70:'C'}
# print(list(grades.items()))
# for (key,value) in grades.items():
#     print(key,value)

# def sum(lower,upper):
#     result=0
#     while lower<=upper:
#         result += lower
#         lower += 1
#     return result
# print(sum(1,4))    

