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

food_1_quantity = int(input("How many " + food_1_name + " do you want?"))


if (food_1_quantity <= food_1_aviable):
  food_1_cost = food_1_quantity * food_1_price
  print("We have enough " + food_1_name + ".")
  print("The price of " + str(food_1_quantity) + " pieces  will be " + str(food_1_cost) + " MDL")
else:
  print("Sorry. We haven't enougt piece of " + food_1_name + ".")
  print("The maximal quantity of " + food_1_name + " you can order is " + str(food_1_aviable) + ".")
  print("Do you whant to change your order$.")
  
  response = input("Type Y or N")
  if (response == "Y"):
    food_1_quantity = int(input("Change your order. Put here maximal quantity of " + food_1_name)
  else:
   print("You can order another dish. We have a lot of different dishes.")
	


#view
