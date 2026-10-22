#Grade
# marks=56
# match marks :
#     case r if marks<35 and marks>0 :
#            print("c grade")
#     case r if marks<70 and marks>35:
#             print('b grade')
#     case r if marks<100 and marks>70:
#             print("A grade")
   
#     case _ :
#               print("Fail")


#Quarter
# Quarter ='december'
# match Quarter.lower():
#    case 'jan'|'feb'|'march'|'april':
#      print("First quarter")
#    case 'may'|'june'|'july'|'august':    
#      print("Second Quarter")
#    case 'september'|'october'|'november'|'december':
#      print("Third Quarter")
#    case _:
#       print("Invalid input")

#Signal meaning
# clr=input("Enter colour ")
# match clr.casefold():
#     case 'red':
#         print("stop")
#     case 'yellow':
#         print("Slow down")
#     case 'Green':
#         print("Go")
#     case _:
#         print("Invalid input")



# An ATM menu accepts either a number or a word: 1/balance, 2/withdraw, 3/deposit, 4/exit/quit.
# Input may contain extra spaces or capital letters, so clean it first.
# Invalid input should return "Invalid option".

# Amount=14393
# pin=1412
# acc_no=12345678
# user_acc_no=int(input("Enter account number"))
# user_pin=int(input("Enter pin"))
# if(user_pin==pin and user_acc_no==acc_no):
#     option=int(input("Enter option 1:checking balance,2:Withdraw amount,3:Deposit amount,4:exit" ))
#     match option:
#      case 1:
#           print(f"Balance amount is {Amount}")
#      case 2:
#           withdraw_amt=int(input("Enter amount to be withdrawed"))
#           Amount-=withdraw_amt
#           print(f"Balance amount is {Amount}")
#      case 3:
#             Depo_amt=int(input("Enter amount to be deposit"))
#             Amount+=Depo_amt
#             print(f"Balance amount is {Amount}")
#      case 4:
#             print("Exit")
#      case _:
#               print("Invalid Input")
# else:
#      print("Enter valid credentials")


# A game accepts typed commands. Split the command into words and handle:
# go <direction>
# pick up <item>
# drop <item>
# quit
# Anything else is an unknown command.
# Sample input: "pickup sword" → Expected output: Picked up: sword


# cmd=input("Enter command ")
# match cmd.split():
#     case ["go",direction]:
#         print(f"moving to direction {direction}")
#     case ["pickup",item]:
#         print(f"picked up {item}")
#     case ["drop",item]:
#         print(f"dropped {item}")
#     case ["quit"]:
#         print("game over")
#     case _:
#         print("Invalid command")




#Find area of square,rectangle,circle
# 
#  
# option=int(input("Enter option, 1:Square, 2:Rectangle, 3:Circle "))
# match option:
#     case 1:
#         side=int(input("Enter side"))
#         area=side**2
#         print(f"area of square is {area}")
#     case 2:
#         length=int(input("Enter length"))
#         width=int(input("Enter width"))
#         area=length*width
#         print(f"area of rectangle is {area}")
#     case 3:
#         radius=int(input("Enter radius"))
#         area=3.14*radius**2
#         print(f"area of circle is {area}")
#     case _:
#         print("Invalid choice")




# Calculate a ticket price from (age, day) using these rules:
# Age below 5: free
# Age below 18 on Tuesday: ₹80
# Age below 18 on other days: ₹120
# Age 60 or above: ₹100
# Adults on Saturday or Sunday: ₹250
# All other adults: ₹200

# age=25
# day="monday"
# match (age,day):
#     case(a,b) if a<5:
#         print("price is 0")
#     case(a,'Tuesday') if a<18:
#         print("price is 80")
#     case(a,b) if a<18:
#         print("price is 120")
#     case(a,b) if a>60 and a<120:
#         print("price is 100")
#     case(a,'saturday'|'sunday') if a>=18:
#         print("price is 250")
#     case(a,b) if a>=18:
#         print("price is 200")
#     case _:
#         print("Invalid input")




# Electricity Bill Slabs

# Accept the units consumed.
# Calculate the bill with these slabs:
# Up to 100 units: ₹3 per unit
# 101 to 200 units: ₹5 per unit
# Above 200 units: ₹8 per unit
# The rate applies to all units, not slab by slab.
# Add a fixed charge of ₹50 and print the total.
# Negative units should print Invalid reading.
# Sample input: 150 → Output: Total bill: ₹800



# unit=150

# match unit:
#     case u if u<=100:
#         bill=unit*3+50
#         print(f"Bill will be {bill}")
#     case u if u>100 and u<=200:
#          bill=unit*5+50
#          print(f"Bill will be {bill}")
#     case u if u>200:
#          bill=unit*8+50
#          print(f"Bill will be {bill}")
#     case _:
#           print('Invalid input')




# A machine sells: 1 Water (₹20), 2 Juice (₹40), 3 Chips (₹30).
# Accept the item number and the amount inserted.
# Print Collect your item if the amount is enough, and also show the change to return.
# Print Insufficient amount if it is less than the price.
# Print Invalid item for any other item number.
# Sample input: 2, 50 → Output: Collect your Juice. Change: ₹10

# option=int(input('Enter option 1:water(20),2:juice(40),3:chips(30)'))
# amount=50
# match option:
#         case 1 if amount>20:
#             change=amount-20
#             print(f"Collect item and change:{change}")
#         case 2 if amount>40:
#              change=amount-40
#              print(f"Collect item and change:{change}")
#         case 3 if amount>30:
#              change=amount-30
#              print(f"Collect item and change:{change}")
#         case _:
#             print("Invalid input")



#Simple calculator

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /, %): ")

# match op:
#     case "/" | "%" if b == 0:
#         print("Cannot divide by zero")
#     case "+":
#         print(a + b)
#     case "-":
#         print(a - b)
#     case "*":
#         print(a * b)
#     case "/":
#         print(a / b)
#     case "%":
#         print(a % b)
#     case _:
#         print("Invalid operator")


