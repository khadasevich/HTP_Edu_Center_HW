Below is home assignment for Class 9, Python

By 5PM Tuesday, 11/14/17:

 

Using your knowledge about class attributes operators:

 

1)     Make a class “Store”.

2)     Inherit two classes from it – “GroceryStore” and “HardwareStore”.

3)     Create a class “Goods”, inherit classes “Food” and “Tools” from it.

4)     Subclass 4 random food and tools naming from each (Banana, Apple, Ham - from Food, Nail, Axe, Saw – from Tools…).

5)     Each of the goods’ object must have a read-write “price” attribute, which is set upon creation (make the price up, just should be a positive int or float), set_discount() method that takes discount percentage as an argument, reset_discount() that typically sets it to 0.

6)     Goods objects must also posess freeze_price() method that takes Boolean value as an argument and allows changing price or discount if it was called with True only. By default price is not frozen. You can allow changing the values for example, after banana.freeze_price(False) called. If banana.freeze_price(True) is called, the price should not change.

7)     Instantiate one grocery store and two hardware stores, they all must have methods:

a.     add_item(item) and add_items(*items)

b.     remove_item(item) and remove_items(*items). Allow optional count argument to define how many items are going to be added.

c.      calculate overall goods price currently available (without discount)

d.     calculate overall goods price currently available (with discount)

8)     Shops must allow adding goods of their supported types only – Grocery stores accept goods of Food type only, Hardware stores can add Tools only.

 

Example:

 

belmarket = GroceryStore()
bananas = Banana(6)  # create a banana with 5$ price
strawberry = Strawberry(22)  # create a strawberry with 18$ price
belmarket.add_item(bananas)
belmarket.add_item(strawberry)
print(belmarket.overall_price_no_discount())  # -> outputs 6+22 -> 28

belmarket.remove_item(strawberry)
strawberry.set_discount(50)
strawberry.freeze_price(True)
belmarket.add_item(strawberry)
print(belmarket.overall_price_no_discount())  # -> outputs 6+(22/100*50) -> 17

hammer = Hammer(50)
belmarket.add_item(hammer)  # -> TypeError("Incorrect product assignment!") is raised

 

 

 

Send the attached script(s) by the time and date above.

Please use Python2, or even better, write Py3 code fully compatible with Py2. Use PyCharm debugger when needed.
