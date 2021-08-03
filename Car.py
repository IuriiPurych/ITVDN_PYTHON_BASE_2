from LandVehicle import LandVehicle


class Car(LandVehicle):
    model = str
    price = int
    color = str
    count_of_wheel = 4
    cont_of_crew = 1
    max_count_of_passenger = 4
    volume_tank = 50

    def __init__(self, model, price, color='black'):
        self.model = model
        self.color = color
        self.price = price

    def ride(self):
        print(f'The {self.model} is going.')

    def get_fuel(self, volume=0):
        if self.volume_tank < volume:
            print('It\'s a lot fuel.')
            return
        print('I have a fuel.')