import random


class GasolineCar(object):
    # Class ancestor of Car class creates gasoline cars
    def __init__(self, engine_kind='Gasoline', gas_consump=8, gas_cost=2.4, amort=9.5, km_till_rep=100000, repair=500):
        self.engine_kind = engine_kind
        self.gas_consump = gas_consump
        self.gas_cost = gas_cost
        self.amort = amort
        self.km_till_rep = km_till_rep
        self.repair = repair


class DieselCar(object):
    # Class ancestor of Car class creates diesel cars
    def __init__(self, engine_kind='Diesel', gas_consump=6, gas_cost=1.8, amort=10.5, km_till_rep=150000, repair=700):
        self.engine_kind = engine_kind
        self.gas_consump = gas_consump
        self.gas_cost = gas_cost
        self.amort = amort
        self.km_till_rep = km_till_rep
        self.repair = repair


class Car(GasolineCar, DieselCar):
    # Car - main class inferitor for all machines, car_quantity allows to know how many cars were created
    car_quantity = 1

    def __init__(self, gas_tank=60, cost=10000, cunsump_incr=0.01,
                 engine_kind='Gasoline', gas_consump=8, gas_cost=2.4, amort=9.5, km_till_rep=100000, repair=500):
        # Constuctor of Car
        super(Car, self).__init__(engine_kind, gas_consump, gas_cost, amort, km_till_rep, repair)
        self.gas_tank = gas_tank
        self.cost = cost
        self.cunsump_incr = cunsump_incr
        self.tank_custom()
        self.diesel_car()
        Car.car_quantity += 1

    def tank_custom(self):
        # Method for change volume of gasoline tank for every 5 car
        if Car.car_quantity % 5 == 0:
            self.gas_tank = 75

    def diesel_car(self):
        # Method which initialize creation of the diesel car
        if Car.car_quantity % 3 == 0:
            DieselCar.__init__(self)


class Race(object):
    # Class Race makes all actions which happens with car during race.
    def __init__(self, length=0, gas_cost_total=0, quantity_of_gas_res=0, total_rep_cost=0):
        self.length = length
        self.gas_cost_total = gas_cost_total
        self.quantity_of_gas_res = quantity_of_gas_res
        self.total_rep_cost = total_rep_cost

    def random_route(self):
        # Creates random route for car
        self.length = random.randint(55000, 286000)
        return self.length

    @staticmethod
    def amortisation(length, car):
        # Returns cost of car after race
        for step in range(0, length, 1000):
            car.cost -= car.amort
            if car.cost < 0:
                raise NameError('Your car was broken during race')
        return car.cost

    def gas_restore(self, length, car):
        # Returns how many time car was fueled and quantity of fuelings
        for step in range(0, length, 100):
            if step != 0 and step % 1000 == 0:
                car.gas_consump = self.consumption_increment(car)
            car.gas_tank -= car.gas_consump
            if car.gas_tank <= 0:
                self.quantity_of_gas_res += 1
                self.gas_cost_total += car.gas_cost
        return self.quantity_of_gas_res, int(self.gas_cost_total)

    @staticmethod
    def consumption_increment(car):
        # Returns new consumption of gasoline after race
        car.gas_consump += car.gas_consump * car.cunsump_incr
        return car.gas_consump

    @staticmethod
    def km_till_destroy(car, newcost):
        # Returns how many km car can make till utilisation
        kms_destro = (newcost / car.amort) * 1000
        return int(kms_destro)

    def repair_car(self, length, car):
        # Returns cost of repair
        for step in range(0, length, car.km_till_rep):
            if step != 0 and step % 1000 == 0:
                self.total_rep_cost += car.repair
        return self.total_rep_cost


class TaxoPark(object):
    # Class Taxopark
    def __init__(self, create_cars=0, places=500, list_of_cars=None,
                 total_cost=0, diesel_cars=None, gasoline_cars=None, sorted_gasoline=None, sorted_diesel=None):
        self.places = places
        self.create_cars = create_cars
        self.list_of_cars = list_of_cars
        self.total_cost = total_cost
        self.diesel_cars = diesel_cars
        self.gasoline_cars = gasoline_cars
        self.sorted_gasoline = sorted_gasoline
        self.sorted_diesel = sorted_diesel

    def fill_taxopark(self):
        # Fills taxopark by cars
        self.list_of_cars = []
        for _ in range(self.create_cars):
            self.list_of_cars.append(Car())
        self.places -= len(self.list_of_cars)

    def car_statistic(self):
        # Returns stats of cars in Taxopark
        for car in self.list_of_cars:
            route = Race()
            length_of_route = route.random_route()
            new_gas_cons = route.gas_restore(length_of_route, car)
            rep_tot_cost = route.repair_car(length_of_route, car)
            car.cost = car.cost - new_gas_cons[1] - rep_tot_cost
            try:
                newcost = route.amortisation(length_of_route, car)
                destro_kms = route.km_till_destroy(car, newcost)
            except NameError:
                newcost = 'Your car was broken during race'
                destro_kms = 'Your car was broken during race'
                car.cost = 0
            print "Since creation car has made {} km.\n" \
                  "Now cost of car is {}.\n" \
                  "Since creation quantity of fuellings and total cost of gas/diesel {}.\n" \
                  "Full utilisation of car happens in {} km.\n" \
                  "Total cost of repairs {}.\n" \
                .format(length_of_route, newcost, new_gas_cons, destro_kms, rep_tot_cost)

    def list_creation_gas(self):
        # Creates dicts of results for gasoline cars
        self.gasoline_cars = [Race().km_till_destroy(car, car.cost) for car in self.list_of_cars
                              if car.engine_kind == 'Gasoline']

    def list_creation_dies(self):
        # Creates dicts of results for diesel cars
        self.diesel_cars = [car.cost for car in self.list_of_cars if car.engine_kind == 'Diesel']

    def sorting_of_list_gas(self):
        # Sorts results for gasoline cars
        self.list_creation_gas()
        self.sorted_gasoline = sorted(self.gasoline_cars, reverse=True)

    def sorting_of_list_dies(self):
        # Sorts results for diesel cars
        self.list_creation_dies()
        self.sorted_diesel = sorted(self.diesel_cars, reverse=True)

    def printing_sorted_res_gas_cars(self):
        # Returns results of sorting of gasoline cars
        self.sorting_of_list_gas()
        for element in self.sorted_gasoline:
            print "KMs left till utilisation: {}\n".format(element)

    def printing_sorted_res_dies_cars(self):
        # Returns results of sorting of diesel cars
        self.sorting_of_list_dies()
        for element in self.sorted_diesel:
            print "Cost of car: {}\n".format(element)

    def total_car_cos(self):
        # Returns total cost of cars in the park
        for car in self.list_of_cars:
            self.total_cost += car.cost
        print "At the moment total cost of cars is {}\n".format(self.total_cost)

    def taxo_stat(self):
        # Returns quantity of empty places in the Taxopark and how many cars are already in park
        print "At the moment taxopark contains {} cars.\nEmpty places {}\n".format(self.create_cars, self.places)


if __name__ == '__main__':
    Skoda = TaxoPark(100)
    Skoda.fill_taxopark()
    Skoda.car_statistic()
    Skoda.printing_sorted_res_gas_cars()
    Skoda.printing_sorted_res_dies_cars()
    Skoda.total_car_cos()
    Skoda.taxo_stat()
