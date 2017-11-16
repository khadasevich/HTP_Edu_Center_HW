#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module creates Zoos, Aviaries, Animals of 2 kinds: Herbivorous and Carnivorous"""


class Aviary(object):
    """Creates new objects of aviary type"""

    def __init__(self, name, animal_quantity, aviary_list=None):
        """Constructor of new aviary"""
        self.name = name
        self._animal_quantity = animal_quantity
        self.aviary_list = aviary_list
        self.change_type()

    def change_type(self):
        """Changes parameter aviary_list"""
        if self.aviary_list is None:
            self.aviary_list = []

    def add_animal(self, animal):
        """Adds animal into aviary"""
        self.check_aviary(animal)

    def check_animal(self, animal):
        """Checks types of animals in the aviary"""
        if not isinstance(self.aviary_list[0], type(animal)):
            self.aviary_list.remove(animal)
            raise TypeError("You can't mix animals of different kinds")

    def check_aviary(self, animal):
        """Checks whether this aviary has empty places"""
        if len(self.aviary_list) == self._animal_quantity:
            raise AssertionError("This aviary is full")
        else:
            self.aviary_list.append(animal)
            self.check_animal(animal)
            print ("Animal {} was added to aviary {}".format(animal.name, self.name))

    def remove_animal(self, animal):
        """Removes animal from aviary"""
        if animal in self.aviary_list:
            self.aviary_list.remove(animal)
            print ("Animal {} was removed".format(animal.name))
        else:
            print ("Animal {} isn't in this aviary".format(animal.name))

    def move_animal(self, animal, second_aviary):
        """Moves one animal from one aviary to other"""
        second_aviary.add_animal(animal)
        self.remove_animal(animal)
        print ('{} was moved to {} aviary'.format(animal.name, second_aviary.name))

    def empty_aviary(self):
        """Empties aviary"""
        self.aviary_list[:] = []
        print ('Animals were killed')


class Zoo(object):
    """Creates new Zoo"""

    def __init__(self, aviary_quantity, created_aviaries=None):
        """Constructor of new Zoo"""
        self._aviary_quantity = aviary_quantity
        self.created_aviaries = created_aviaries
        self.change_type()

    def change_type(self):
        """Changes type of created_aviaries parameter"""
        if self.created_aviaries is None:
            self.created_aviaries = []

    def add_aviary(self, name, number_places):
        """Adds new aviary to Zoo"""
        if len(self.created_aviaries) <= self._aviary_quantity:
            aviary = Aviary(name, number_places)
            self.created_aviaries.append(aviary)
            print ("New aviary {} was created".format(aviary.name))
        else:
            print ("Zoo is full")

    def zoo_add_animal(self, animal, aviary_name):
        """Adds new animal to Zoo"""
        for element in self.created_aviaries:
            if element.name == aviary_name:
                element.add_animal(animal)

    def zoo_remove_animal(self, animal, aviary_name):
        """Removes animal from aviary"""
        for aviary in self.created_aviaries:
            if aviary.name == aviary_name:
                aviary.remove_animal(animal)

    def zoo_move_animal(self, animal, aviary_name_first, aviary_name_second):
        """Moves animal from one aviary to second"""
        for aviary in self.created_aviaries:
            if aviary.name == aviary_name_first:
                for element in self.created_aviaries:
                    if element.name == aviary_name_second:
                        aviary.move_animal(animal, element)

    def zoo_empty_aviary(self, aviary_name):
        """Empties aviary in the zoo"""
        for aviary in self.created_aviaries:
            if aviary.name == aviary_name:
                aviary.empty_aviary()

    def remove_aviary(self, name):
        """Removes aviary from zoo"""
        for aviary in self.created_aviaries:
            if aviary.name == name:
                self.created_aviaries.remove(aviary)
                print ("Aviary {} was deleted".format(aviary.name))

    def zoo_statistic(self):
        """Returns statistics on Zoo"""
        print ('Quantity of aviaries in the Zoo is: {}'.format(len(self.created_aviaries)))
        for aviary in self.created_aviaries:
            print ("At the moment aviary {} consists of: \n{}".format(aviary.name, *aviary.aviary_list))


class Animal(object):
    """Class which creates new Animal object"""

    def __init__(self, name, age):
        """Constructor of new animal"""
        self.name = name
        self.age = age


class Herbivorous(Animal):
    """Creates new Herbivorous animal, inherited from Animal"""
    pass


class Carnivorous(Animal):
    """Creates new Carnivorous animal, inherited from Animal"""
    pass


if __name__ == "__main__":
    cow = Herbivorous('Jane', 5)
    horse = Herbivorous('Mike', 6)
    elephant = Herbivorous('Dumbo', 4)
    wolf = Carnivorous('Jason', 6)
    tiger = Carnivorous('Sher-Khan', 3)
    lynx = Carnivorous('Bahira', 4)
    new_zoo = Zoo(5)
    new_zoo.add_aviary('1', 2)
    new_zoo.zoo_add_animal(wolf, '1')
    new_zoo.zoo_add_animal(lynx, '1')
    new_zoo.add_aviary('2', 2)
    new_zoo.zoo_move_animal(lynx, '1', '2')
    new_zoo.zoo_empty_aviary('2')
    new_zoo.remove_aviary('2')