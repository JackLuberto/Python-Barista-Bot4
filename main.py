### JHL Development Robot Coffee Barista
### Learning In Python Part 4

## Name of business here =
business = "Jacks Coffee House"  

## Items on menu here =
menu = "Black Coffee, Espresso, Light and Sweet,\n" + "Ice Coffee, Cappucino, Sweet Tea"

## Introduction message
print("Hello Welcome To " + business + "!!!")

## Thank You Message
print("Thank you so much for coming in today!!!")

## Asks Customer For Name
name = input("What is your name?\n")

## Banned Customer ("Mike")
if name == "Mike":  ## Banned Customer Name Here
  badcustomerstatus = input(  ## Question To Find Out If The User Has Been Banned Before Or Not
    "You look quite familiar... Have You ever been banned from " + business +
    "\n")
  if badcustomerstatus == "Yes":  ## If The User Answers Yes Then
    print("You are still banned from " +
          business)  # Response To Customer Statement ("Yes")
    exit()  ## Program Exit If Customer Answers "Yes"
    
## Banned Customer ("mike")
if name == "mike":  ## Banned Customer Name Here
  badcustomerstatus = input(  ## Question To Find Out If The User Has Been Banned Before Or Not
    "You look quite familiar... Have You ever been banned from " + business +
    "\n")
  if badcustomerstatus == "Yes":  ## If The User Answers Yes Then
    print("You are still banned from " +
          business)  # Response To Customer Statement ("Yes")
    exit()  ## Program Exit If Customer Answers "Yes"

## Banned Customer ("Ben")
if name == "Ben":  ## Banned Customer Name Here
  badcustomerstatus = input(  ## Question To Find Out If The User Has Been Banned Before Or Not
    "You look quite familiar... Have You ever been banned from " + business +
    "\n")
  if badcustomerstatus == "Yes":  ## If The User Answers Yes Then
    print("You are still banned from " +
          business)  # Response To Customer Statement ("Yes")
    exit()  ## Program Exit If Customer Answers "Yes"

## Banned Customer ("ben")
if name == "ben":  ## Banned Customer Name Here
  badcustomerstatus = input(  ## Question To Find Out If The User Has Been Banned Before Or Not
    "You look quite familiar... Have You ever been banned from " + business +
    "\n")
  if badcustomerstatus == "Yes":  ## If The User Answers Yes Then
    print("You are still banned from " +
          business)  # Response To Customer Statement ("Yes")
    exit()  ## Program Exit If Customer Answers "Yes"
    
  else:  ## If Customer Answers "Yes" Then
    print("Ok, my apologies. Come on in to " +
          business)  #Response To Customer Statement
else:  ## If Customer Answers Anything But "Yes" Ie: Customer Answers No Then
  print("Hello " + name + " Welcome to " +
        business)  # Response To Customer Statement

## Displays Menu And Asks Customer What They Want To Order
order = input("What Would You Like To Order?\n" + 
              "This Is What We Have On Our Menu For Today:\n" + menu + "\n") 

## Set Price of Items here =
if order == "Black Coffee":
  price = 2 
elif order == "Espresso":
  price = 3
elif order == "Light and Sweet":
  price = 5
elif order == "Ice Coffee":
  price = 4
elif order == "Sweet Tea":
  price = 1

quantity = input("How much " + order + " Would you like?\n") ## Asks customer how many they want of specific order

## Customer Order Extras
if order == "Ice Coffee": 
  ic_creme_sugar = input("Would you like extra creme and sugar?\n") ## Asks customer if they want an Addon
  if ic_creme_sugar == "Yes":
    price = 5 ## Sets New Price If They Want The Addon
    new_coffee_price = input(
      "Great!! That will be $1 extra per coffee. Is this okay? \n") ## Upcharges customer on the addon and asks for permission
    if new_coffee_price == "Yes": ## if answer is yes then price remains the same
      price = 5 
    else: ## If answer is no then price remains the same as original set price without the addon
      new_coffee_price == "No"
      price = 4

if order == "Light and Sweet": ## Asks customer if they want an Addon
  ls_drinksize = input("Would you like a Large?\n")
  if ls_drinksize == "Yes":
    price = 6 ## Sets New Price If They Want The Addon
    new_coffee_price = input(
      "Great!! That will be $1 extra per coffee. Is this okay? \n") ## Upcharges customer on the addon and asks for permission
    if new_coffee_price == "Yes":
      price = 6
    else: ## If answer is no then price remains the same as original set price without the addon
      new_coffee_price == "No"
      price = 5

if order == "Espresso": 
  es_drinksize = input("Would you like a Large?\n") ## Asks customer if they want an Addon
  if es_drinksize == "Yes":
    price = 4 ## Sets New Price If They Want The Addon
    new_coffee_price = input(
      "Great!! That will be $1 extra per coffee. Is this okay? \n") ## Upcharges customer on the addon and asks for permission
    if new_coffee_price == "Yes":
      price = 4
    else: ## If answer is no then price remains the same as original set price without the addon
      new_coffee_price == "No"
      price = 3

if order == "Black Coffee": 
  bc_drinksize = input("Would you like A Large?\n") ## Asks customer if they want an Addon
  if bc_drinksize == "Yes":
    price = 4 ## Sets New Price If They Want The Addon
    new_coffee_price = input(
      "Great!! That will be $1 extra per coffee. Is this okay? \n")
    if new_coffee_price == "Yes":
      price = 4
    else: ## If answer is no then price remains the same as original set price without the addon
      new_coffee_price == "No"
      price = 3

if order == "Sweet Tea":
  tea_drinksize = input("Would you like a Large?\n") ## Asks customer if they want an Addon
  if tea_drinksize == "Yes":
    price = 2 ## Sets New Price If They Want The Addon
    new_coffee_price = input(
      "Great!! That will be $1 extra per tea. Is this okay? \n")
    if new_coffee_price == "Yes":
      price = 2
    else: ## If answer is no then price remains the same as original set price without the addon
      new_coffee_price == "No"
      price = 1

total = price * int(quantity) ## Equation to tally up the total amount of money owed to the business and changes quantity into an interger

## Statement that they will call the person when the order is ready # while converting the total into a string
## And displaying the quantity, total, and order in the correct format
print("Sounds great " + name + " Your total is going to be " + "$" +
      str(total) + "\n" + "we will get your " + quantity + " " + order + 
      " right up for you!!!" +
      " We will call you to the register when your \n" + quantity + " " +
      order + " is ready!!!") 

## Statement letting the customer know the order is ready, and telling the customer to come recieve the order at the counter
print("Hey " + name + " Your " + quantity + " " + order +
      " is ready at the counter!!!\n" + "Thank you for choosing " + business +
      "!!!\n" + "Have a good day, and we hope to see you soon!!!")
