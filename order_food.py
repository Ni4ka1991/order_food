#!/usr/bin/env Python3


#data

food_1_name     = "Pizza"
food_1_price    = 45          #MDL
food_1_aviable  = 5           #piece

food_2_name     = "Bifsteak"
food_2_price    = 122         #MDL
food_2_aviable  = 2           #piece

drink_1_name    = "Orange juice fresh"
drink_1_price   = 25          #MDL
drink_1_aviable = 1           #drink




#logic

   #Calculate the cost of food_1 order
      
      #Input and transform data from the user

food_1_quantity = int(input("How many " + food_1_name + " do you want?\n"))

      #Verification and calculation of data

if (food_1_quantity <= food_1_aviable):
  food_1_cost = food_1_quantity * food_1_price
  print("We have enough " + food_1_name + ".")
  print("The price of " + str(food_1_quantity) + " pieces  will be " + str(food_1_cost) + " MDL\n")
else:
  print("Sorry. We haven't enougt pieces of " + food_1_name + ".")
  print("The maximal quantity of " + food_1_name + " you can order is " + str(food_1_aviable) + ".")
  print("Please, change your order.\n")
  food_1_quantity = int(input("Be careful, how many " + food_1_name + " do you want?\n"))
  food_1_cost = food_1_quantity * food_1_price
  print("The price of " + str(food_1_quantity) + " pieces  will be " + str(food_1_cost) + " MDL\n")
   


     #Calculate the cost of food_2 order

      #Input and transform data from the user

food_2_quantity = int(input("How many " + food_2_name + " do you want?\n"))

      #Verification and calculation of data

if (food_2_quantity <= food_2_aviable):
  food_2_cost = food_2_quantity * food_2_price
  print("We have enough " + food_2_name + ".")
  print("The price of " + str(food_2_quantity) + " pieces  will be " + str(food_2_cost) + " MDL\n")
else:
  print("Sorry. We haven't enougt pieces of " + food_2_name + ".")
  print("The maximal quantity of " + food_2_name + " you can order is " + str(food_2_aviable) + ".")
  print("Please, change your order.\n")
  food_2_quantity = int(input("Be careful, how many " + food_2_name + " do you want?\n"))
  food_2_cost = food_2_quantity * food_2_price
  print("The price of " + str(food_2_quantity) + " pieces  will be " + str(food_2_cost) + " MDL\n")


     #Calculate the cost of drink_1 order
	
      #Input and transform data from the user

drink_1_quantity = int(input("How many " + drink_1_name + " do you want?\n"))
     
      #Verification and calculation of data

if (drink_1_quantity <= drink_1_aviable):
  drink_1_cost = drink_1_quantity * drink_1_price
  print("We have enough " + drink_1_name + ".")
  print("The price of " + str(drink_1_quantity) + " pieces  will be " + str(drink_1_cost) + " MDL\n")
else:
  print("Sorry. We haven't enougt pieces of " + drink_1_name + ".")
  print("The maximal quantity of " + drink_1_name + " you can order is " + str(drink_1_aviable) + ".")
  print("Please, change your order.\n")
  drink_1_quantity = int(input("Be careful, how many " + drink_1_name + " do you want?\n"))
  drink_1_cost = drink_1_quantity * drink_1_price
  print("The price of " + str(drink_1_quantity) + " pieces  will be " + str(drink_1_cost) + " MDL\n")

    #Calculate a bill

bill = food_1_cost + food_2_cost + drink_1_cost
print("Your bill is " + str(bill) + " MDL\n")
    

    #Delivery info

food_delivery = int(input("Would you like delivery&.\nPlease, type 1 or 0\n"))

if (food_delivery == True):
 if (bill > 1000):
  print("Free shipping")
 else:
  bill = bill + 150
  print("Order price is " + str(bill) + " MDL")
else:
 print("Have a good day!")
