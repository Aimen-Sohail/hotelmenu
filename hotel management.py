#Define the menu of the resturant.
menu = {
    'Pizza':500,
    'Pasta': 350,
    'Zinger Burger':450,
    'Shawarma':180,
    'Kabab roll':250
}

#Greet the Customers.
print("WELCOME TO BNQ RESTURASNT")
print("Pizza:  Rs:500\nPasta: Rs:350\nZinger Burger: Rs450\nShawarma: Rs180\nKabab roll: Rs250")

Order_Total = 0
#for Example= (*Pizza=500+Pasta+350)=850

item_1 = input("Enter the Name of item you want to order = ")
if item_1 in menu:
    Order_Total += menu[item_1] #500+350
    print(f"your item {item_1} has been added to your order")

else:
    print(f"your item {item_1} is not available at our resturant yet!")

Another_order = input("Do you want to add another item?  (Yes/No)")
if Another_order == "Yes":
       item_2 = input("Enter the name of Second Dish= ")
       if item_2 in menu:
           Order_Total += menu[item_2]
           print(f"your item {item_2} has been added to your order")
       else:
        print(f"Ordered item{item_2}your item is not available at our resturant yet!")

print(f"The total amount of your order is {Order_Total}")


           