# even or odd
# 1.args with return type
# def evenodd(a):
#     if a%2==0:
#         return "even"
#     else:
#         return "odd"

# print(evenodd(5))
# print(evenodd(8))

#2.args without return type
# def evenodd(a):
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")

# evenodd(5)
# evenodd(8)

#3.no args with return type
# def evenodd():
#     a=8
#     if a%2==0:
#         return "even"
#     else:
#         return "odd"

# print(evenodd())

#4.no args without return type
# def evenodd():
#     a=5
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")

# evenodd()


#POsitive,negative or zero
# 1.args with return type
# def pos_neg_zero(a):
#     if a==0:
#         return "zero"
#     elif a<0:
#         return "negative"
#     else:
#         return "Positive"

# print(pos_neg_zero(5))
# print(pos_neg_zero(-9))
# print(pos_neg_zero(0))

#2.args without return type
# def pos_neg_zero(a):
#     if a==0:
#         print("zero")
#     elif a<0:
#         print ("negative")
#     else:
#         print ("Positive")

# (pos_neg_zero(5))
# (pos_neg_zero(-9))
# (pos_neg_zero(0))

#3.no args with return type
# def pos_neg_zero():
#     a=3
#     if a==0:
#         return "zero"
#     elif a<0:
#         return "negative"
#     else:
#         return "Positive"

# print(pos_neg_zero())


#4.no args without return type
# def pos_neg_zero():
#     a=-7
#     if a==0:
#         print("zero")
#     elif a<0:
#         print ("negative")
#     else:
#         print ("Positive")

# (pos_neg_zero())

#palindrome

# 1.args with return type
# def palindrome(a):
#  num=a
#  rev=0
#  while(a>0):
#   digit=a%10
#   rev=rev*10+digit
#   a=a//10
#  if num==rev:
#   return "palindrome"
#  else:
#   return "not palindrome"
# print(palindrome(12321))

# 2.args without return type
# def palindrome(a):
#  num=a
#  rev=0
#  while(a>0):
#   digit=a%10
#   rev=rev*10+digit
#   a=a//10
#  if num==rev:
#   print("palindrome")
#  else:
#   print("not palindrome")
  
# (palindrome(12321))

# 3.no args with return type
# def palindrome():
#  a=8765
#  num=a
#  rev=0
#  while(a>0):
#   digit=a%10
#   rev=rev*10+digit
#   a=a//10
#  if num==rev:
#   return "palindrome"
#  else:
#   return "not palindrome"
# print(palindrome())

# 4.no args without return type
# def palindrome():
#  a=8765
#  num=a
#  rev=0
#  while(a>0):
#   digit=a%10
#   rev=rev*10+digit
#   a=a//10
#  if num==rev:
#   print("palindrome")
#  else:
#   print("not palindrome")
  
# (palindrome())


#reverse a number
# 1.args with return type
# def reverse_num(a):
#  rev=0
#  while(a>0):
#   digit=a%10
#   rev=rev*10+digit
#   a=a//10
#  return rev

# print(reverse_num(1234))

# 2.args without return type
# def reverse_num(a):
#  rev=0
#  while(a>0):
#   digit=a%10
#   rev=rev*10+digit
#   a=a//10
#  print(rev)

# (reverse_num(1234))

# 3.no args with return type
# def reverse_num():
#  a=1234
#  rev=0
#  while(a>0):
#   digit=a%10
#   rev=rev*10+digit
#   a=a//10
#  return rev

# print(reverse_num())

# 4.no args without return type
# def reverse_num():
#  a=1234
#  rev=0
#  while(a>0):
#   digit=a%10
#   rev=rev*10+digit
#   a=a//10
#  print(rev)

# (reverse_num())

#prime number
#1.args with return type
# def prime_num(num):

#  count=0
#  for i in range(1,num+1):
#     if num%i==0:
#         count+=1
#  if count==2:
#     return("prime")
#  else:
#     return("not prime")

# print(prime_num(7))

#2.Args without return type
# def prime_num(num):

#  count=0
#  for i in range(1,num+1):
#     if num%i==0:
#         count+=1
#  if count==2:
#     print("prime")
#  else:
#     print("not prime")

# (prime_num(7))

#3.no args with return type
# def prime_num():
#  num=6
#  count=0
#  for i in range(1,num+1):
#     if num%i==0:
#         count+=1
#  if count==2:
#     return("prime")
#  else:
#     return("not prime")

# print(prime_num())

#no args without return type
# def prime_num():
#  num=6
#  count=0
#  for i in range(1,num+1):
#     if num%i==0:
#         count+=1
#  if count==2:
#     print("prime")
#  else:
#     print("not prime")

# (prime_num())



#range prime number
#args with return type
# def prime_num(r):
#    prime=[]
#    for i in range(1,r+1):
   
#     count=0
#     for j in range(1,i+1):
#      if i%j==0:
#         count+=1
#     if(count==2):
#      prime.append(i)

#    return(prime)

# print(prime_num(100))


#args without return type
# def prime_num(r):
#    prime=[]
#    for i in range(1,r+1):
    
#     count=0
#     for j in range(1,i+1):
#      if i%j==0:
#         count+=1
#     if(count==2):
#      prime.append(i)

#    print(prime)

# (prime_num(100))
    
#no args with return type
# def prime_num():
#    r=200
#    prime=[]
#    for i in range(1,r+1):
   
#     count=0
#     for j in range(1,i+1):
#      if i%j==0:
#         count+=1
#     if(count==2):
#      prime.append(i)

#    return(prime)

# print(prime_num())

#no args without return type
# def prime_num():
#    r=100
#    prime=[]
#    for i in range(1,r+1):
    
#     count=0
#     for j in range(1,i+1):
#      if i%j==0:
#         count+=1
#     if(count==2):
#      prime.append(i)

#    print(prime)

# (prime_num())


#factorial 
#args with return type
# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#      fact=fact*i
#     return (fact)
# print(factorial(4))

#args without return type
# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#      fact=fact*i
#     print(fact)
# factorial(5)

#no args with return type
# def factorial():
#     num=6
#     fact=1
#     for i in range(1,num+1):
#      fact=fact*i
#     return (fact)
# print(factorial())

#no args without return type
# def factorial():
#     num=7
#     fact=1
#     for i in range(1,num+1):
#      fact=fact*i
#     print(fact)
# factorial()


# square and cube
#args with return type
# def sq_cube(num):
    
#   return(num**2),(num**3)
# print(sq_cube(3))

#args without return type
# def sq_cube(num):
#  print(num**2)
#  print(num**3)
# sq_cube(4)

#no args with return type
# def sq_cube():
#   num=5
    
#   return(num**2),(num**3)
# print(sq_cube())

# no args without return type
# def sq_cube():
#  num=6
#  print(num**2)
#  print(num**3)
# sq_cube()
