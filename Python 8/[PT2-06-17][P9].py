class Store(object):
    """Class which allows creation of the New common store"""

    def __init__(self, warehouse=[], over_sum_no_discount=0, over_sum_yes_discount=0):
        """Constructor of new common store"""
        self.warehouse = warehouse
        self.over_sum_no_discount = over_sum_no_discount
        self.over_sum_yes_discount = over_sum_yes_discount

    def add_item(self, item):
        """Method which allows to add new item into store"""
        self.warehouse.append(item)
        self.overall_price_yes_discount(item)
        self.overall_price_no_discount(item)

    def remove_item(self, item):
        """Method which allows to delete item from the store"""
        if item in self.warehouse:
            self.warehouse.remove(item)
            self.change_overall(item)
        else:
            print "This element isn't in this store, please check input"

    def overall_price_yes_discount(self, item):
        """Method which returns overall price with discount"""
        if item.discount > 0:
            self.over_sum_yes_discount += item._price

    def overall_price_no_discount(self, item):
        """Method which returns overall price without discount"""
        if item.discount == 0:
            self.over_sum_no_discount += item._price

    def change_overall(self, item):
        if self.over_sum_yes_discount > 0 and item.discount > 0:
            self.over_sum_yes_discount -= item._price
        if self.over_sum_no_discount > 0 and item.discount == 0:
            self.over_sum_no_discount -= item._price


class GroceryStore(Store):
    """Class GroceryStore inheritor of Store Class, inherits all methods from Store"""

    def __init__(self, warehouse=[]):
        """Method constructor of the GroceryStore"""
        super(GroceryStore, self).__init__(warehouse)

    def add_item(self, *item):
        """Method which allows to add item into Grocery store, inherited from Store"""
        for element in item:
            if element.type == 'Grocery':
                super(GroceryStore, self).add_item(element)
            else:
                raise TypeError("Incorrect product assignment!")

    def remove_item(self, *item):
        """Method which allows to delete item from Grocery store, inherited from Store"""
        for element in item:
            super(GroceryStore, self).remove_item(element)


class HardwareStore(Store):
    def __init__(self, warehouse=[]):
        """Method which allows to create new Hardware Store"""
        super(HardwareStore, self).__init__(warehouse)

    def add_item(self, *item):
        """Method which allows to add item into Hardware Store, inherited from Store"""
        for element in item:
            if element.type == 'Tool':
                super(HardwareStore, self).add_item(element)
            else:
                raise TypeError("Incorrect product assignment!")

    def remove_item(self, *item):
        """Method which allows to delete item from Hardware Store, inherited from Store"""
        for element in item:
            super(HardwareStore, self).remove_item(element)


class Goods(object):
    """Class ancestor for all goods"""

    def __init__(self, price=0, discount=0, freezing=True, type=None):
        """Constructor of goods"""
        self._price = price
        self.discount = discount
        self.freezing = freezing
        self.type = type

    @property
    def protected_price(self):
        return self._price

    @protected_price.setter
    def freeze_value(self, value):
        """Method which allows enabling/disabling freezing of price"""
        if self.freezing == False:
            self._price = value
        else:
            raise ValueError("Changing of price is denied")

    def set_discount(self, discount):
        """Method which sets discount of the good"""
        self.discount = discount
        decrement = 1 - self.discount / 100.0
        self._price *= decrement

    def reset_discount(self):
        """Method which allows disable discount for good"""
        increment = 1 - self.discount / 100.0
        self._price *= 1 / increment
        self.discount = 0


class Food(Goods):
    """Class which creates new food item, inheritor of Goods class"""

    def __init__(self, price, type=None):
        """Method which creates new food item, inherited from Goods"""
        super(Food, self).__init__(price, type='Grocery')

    def set_discount(self, discount):
        """Method which allows to set discount of food item, inheritor of Goods class"""
        super(Food, self).set_discount(discount)

    def reset_discount(self):
        """Method which allows to reset discount of food item, inheritor of Goods class"""
        super(Food, self).reset_discount()


class Tools(Goods):
    """Class which creates new tool item, inheritor of Goods class"""

    def __init__(self, price, type=None):
        """Method which creates new food item, inherited from Goods"""
        super(Tools, self).__init__(price, type='Tool')

    def set_discount(self, discount):
        """Method which sets discount of good item, inherited from Goods"""
        super(Tools, self).set_discount(discount)

    def reset_discount(self):
        """Method which disables discount of tool item, inherited from Goods"""
        super(Tools, self).reset_discount()


class Banana(Food):
    """Class which creates bananas"""

    def __init__(self, price=0):
        """Method which creates new food item, inherited from Food"""
        super(Banana, self).__init__(price)


class Apple(Food):
    """Class which creates apples"""

    def __init__(self, price=0):
        """Method which creates new food item, inherited from Food"""
        super(Apple, self).__init__(price)


class Ham(Food):
    """Class which creates bananas"""

    def __init__(self, price=0):
        """Method which creates new food item, inherited from Tools"""
        super(Ham, self).__init__(price)


class Nail(Tools):
    """Class which creates nail"""

    def __init__(self, price=0):
        """Method which creates new food item, inherited from Tools"""
        super(Nail, self).__init__(price)


class Axe(Tools):
    """Class which creates axes"""

    def __init__(self, price=0):
        """Method which creates new food item, inherited from Tools"""
        super(Axe, self).__init__(price)


class Saw(Tools):
    """Class which creates saws"""

    def __init__(self, price=0):
        """Method which creates new food item, inherited from Tools"""
        super(Saw, self).__init__(price)


if __name__ == '__main__':
    """Creation of stores"""
    food_shop = GroceryStore()
    hardware_shop = HardwareStore()
    hardware_shop2 = HardwareStore()

    """Creation of items"""
    banana = Banana(8)
    ham = Ham(22)
    nail = Nail(2)
    saw = Saw(6)

    """Checking main functionality of
    grocery shop"""
    ham.set_discount(50)
    food_shop.add_item(ham, banana)
    print food_shop.over_sum_no_discount
    print food_shop.over_sum_yes_discount
    food_shop.remove_item(ham)
    print food_shop.over_sum_no_discount
    print food_shop.over_sum_yes_discount
    ham.reset_discount()
    food_shop.add_item(ham)
    print food_shop.over_sum_no_discount
    print food_shop.over_sum_yes_discount
    try:
        food_shop.add_item(nail)
    except TypeError:
        print "This good isn't suitable for this store \n"

    """Checking main functionality of
    hardware shop"""
    saw.set_discount(50)
    hardware_shop.add_item(saw, nail)
    print hardware_shop.over_sum_no_discount
    print hardware_shop.over_sum_yes_discount
    hardware_shop.remove_item(saw)
    print hardware_shop.over_sum_no_discount
    print hardware_shop.over_sum_yes_discount
    saw.reset_discount()
    hardware_shop.add_item(saw)
    print hardware_shop.over_sum_no_discount
    print hardware_shop.over_sum_yes_discount
    try:
        hardware_shop.add_item(banana)
    except TypeError:
        print "This good isn't suitable for this store \n"

    """Checking of price freezing"""
    try:
        nail.freeze_value = 6
        print 'Price was changed on {}'.format(nail._price)
    except ValueError:
        print 'Changing of price is denied'
    nail.freezing = False
    try:
        nail.freeze_value = 8
        print 'Price was changed on {}'.format(nail._price)
    except ValueError:
        print 'Changing of price is denied'
