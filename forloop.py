# 1. Find the sum of the digits of a number.

# digit=343
# sum=0
# for i in (str(digit)):
#     sum+=int(i)
# print(sum)

#2. Find the sum of all even numbers from 1 to 100

# sum=0
# for i in range(0,101,2):
#     sum+=i
# print(sum)

#3. Find the sum of all odd numbers from 1 to 100
# for i in range(1,101,2):
#     sum+=i
# print(sum)

#4.Find the average of N numbers entered by the user.
# total=0
# t_num=6
# for i in range(t_num+1):
#     num=int(input("Enter number"))
#     total+=num

# print("Average is ",total/t_num)

#5.Count how many numbers between 1 and 100 are divisible by 7
# count=0
# for i in range(1,101,7):
#     count+=1
# print(count-1)

# 6.Count the vowels in a string
# s="Anushka"
# count=0
# for i in s.lower():
#    if i in 'aeiou':
#       count+=1
# print(count)

# 7.Count the consonants in a string.
# s="Anushka"
# count=0
# for i in s.lower():
#    if i not in 'aeiou':
#     count+=1
# print(count)

#8. Count the uppercase and lowercase letters in a string.
# s="Anushka"
# count1=0
# for i in s:
#     if i.isupper():
#         count1+=1
# print(f"number of uppercase letter {count1}")
# print(f"number of lowercase letter {len(s)-count1}")

#9.Find the sum of the squares of the first N natural numbers.
# sum=0
# for i in range(1,10):
#     sum+=i**2
# print(sum)

#10.Prime number
# num=93
# if num <= 1:
#     is_prime = False
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break  
# if is_prime:
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")


#11. Print all numbers from 1 to 100 that end with the digit 3.
# for i in range(3,101,10):
#     print(i)

#12. Print all two-digit numbers whose digits are the same (11, 22, ...)
# for i in range(11,100):
#     if i%11==0:
#         print(i)

#13.Print the first 15 terms of the series 3, 6, 9, 12, ..
# for i in range(1,16):
#     print(i*3)

#14.Print the first 10 terms of the series 2, 5, 8, 11, ..
# n=2
# for i in range(11):
#     print(n)
#     n+=3
    
#15.Print numbers from 1 to 20, replacing multiples of 3 with “Fizz” and multiples of 5 with “Buzz”
# for i in range(1, 21):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

#16.Find the sum of numbers from 1 to 50 that are not divisible by 5
# sum=0
# for i in range(1, 51):
#     if i % 5 != 0:
#         sum+=i
# print(sum)

#17.Print the reciprocal (1/n) of numbers from 1 to 5, rounded to 2 decimals
# for i in range(1, 6):
#      print(round(1/i, 2))

#18.Print a table converting 0 to 100 °C (in steps of 20) to Fahrenheit.
# temp=0
# for i in range(0,100,20):
#     temp=(i*1.5)+32
#     print(temp)

# 19.Print the simple interest on 1000 at 5% for years 1 to 5.
# p=100
# r=5/100
# for i in range(1,6):
#     S_I=p*r*i/100
#     print(S_I)

#20.Find the sum of all numbers from 50 to 100
# sum=0
# for i in range(50,101):
#     sum+=i
# print(sum)

# 21.Print each word of a sentence on a new line
# s = "Python is easy language"
# for i in s.split():
#     print(i)

#22. Print the first letter of each word in a sentence.
# s="Python is easy language"
# for i in s.split():
#     print(i[0])

#23. Count the digits in an alphanumeric string.
# count=0
# s="Anushka1234"
# for i in s:
#     if i.isdigit():
#         count+=1
# print(count)

#24. Count the special characters in a string.
# count=0
# s="Anushka@1!#4%^"
# for i in s:
#     if not i.isalnum():
#         count+=1
# print(count)

#25. Toggle the case of each character in a string (a to A, B to b).
# s="AnUsHkA"
# for i in s:
#     if i.islower():
#         print(i.upper())
#     if i.isupper():
#         print(i.lower())

#26. Print the characters of a string at odd indexes.
# s="Anushka"
# for i in range(1,len(s),2):
#     print(s[i])

#27. Remove all spaces from a string using a loop.
# s="Python is easy language"
# for i in s:
#     if not i.isspace():
#         print(i)
#28. Find the longest word in a sentence.
# longest = ""
# s = "Python is easy language"
# for i in s.split():
#     if len(i) > len(longest):
#         longest = i
# print(longest)

#29. Print a string with each character repeated twice (“abc” to “aabbcc”)
# s = "abc"
# result = ""
# for i in s:
#     result += i * 2
# print(result)

#30.Find the product of the digits of a number.
# product=1
# num=str(1212)
# for i in num:
#     product*=int(i)
# print(product)

# 31. Count how many times a given digit appears in a number.

# count=0
# digit=str(4)
# num=str(124464)
# for i in num:
#     if digit in i:
#         count+=1
# print(count)


# 32. Print all leap years between 2000 and 2050.

# for i in range(2000,2051,4):
#     print(i)


# 33. Print the first 10 triangular numbers (1, 3, 6, 10, ...).

# for i in range(11):
#     t_num=(i*(i+1))/2
#     print(t_num)


# 34. Print all perfect squares between 1 and 1000.
# for i in range(1,32):
#     print(i**2)

   
# 35. Find the sum of the first and last digit of a number using for loop.
# sum=0
# num=str(1234)
# for i in range(len(num)):
#     if i==0 or i==len(num)-1:
#         sum+=int(num[i])

# print(sum)


# 36. Check whether a string contains only digits, without using isdigit().
# s = "12345"
# result = len(s) > 0
# for i in s:
#     if i < "0" or i > "9":
#         result = False
#         break
# print(result)

# 37. Print a string with a hyphen between every character (“abc” to a-b-c).
# s = "abc"
# r = ""
# for i in range(len(s)):
#     r += s[i]
#     if i < len(s) - 1:
#         r += "-"
# print(r)


# 38. Find the position of the last occurrence of a given character in a string.
# s = "anushka"
# c = "a"
# pos = -1
# for i in range(len(s)):
#     if s[i] == c:
#         pos = i
# print(pos)  



# 39. Print a string with alternating upper and lower case (“hello” to HeLlO).
# s="AnUsHkA"
# for i in s:
#     if i.islower():
#         print(i.upper())
#     if i.isupper():
#         print(i.lower())

# 40. Count the positions where characters match between two strings of equal length.
# a = "apple"
# b = "ample"
# count = 0
# for i in range(len(a)):
#     if a[i] == b[i]:
#         count += 1
# print(count)


# 41. Print a string after removing every occurrence of a given character.
# s='abcscgfc'
# for i in s:
#     if i not in 'c':
#         print(i)

# 42. Check whether a string starts and ends with the same character.

# 43. Swap the first and last characters of a string.


# 44. Shift each lowercase letter forward by 1 (“abc” to bcd).
# s='abcde'
# s1="" 
# for i in s:
#     s1+=chr(ord(i)+1)
# print(s1)

# 45. Count how many times two identical characters appear side by side (“aabbc” gives 2).
# s = "aabbc"
# count = 0
# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         count += 1
# print(count)

# 46. Find the character with the highest ASCII value in a string.
# s = "hello"
# highest = s[0]
# for ch in s:
#     if ord(ch) > ord(highest):
#         highest = ch
# print(highest, ord(highest))


# 47. Mask a card number so only the last 4 characters are visible (************1234).
# s = "1234567812341234"
# out = ""
# for i in range(len(s)):
#     if i < len(s) - 4:
#         out += "*"
#     else:
#         out += s[i]
# print(out)


# 48. Count the characters that come before the first vowel in a string.
# s = "strength"
# count = 0
# for ch in s.lower():
#     if ch in "aeiou":
#         break
#     count += 1
# print(count)

# 49. Check whether the characters of a string are in alphabetical order.
# s='abcde'
# count=0
# for i in range(len(s)):
#     if ord(s[i])>ord(s[i-1]):
#         print("Alpha order")
#     break

# 50. Count how many characters in a string match its first character
# s = "anushka arnav"
# count = 0
# for ch in s:
#     if ch == s[0]:
#         count += 1
# print(count)






