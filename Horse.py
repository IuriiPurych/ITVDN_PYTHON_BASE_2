from LandVehicle import LandVehicle


class Horse(LandVehicle):
    name = str
    horse_suit = str
    cont_of_crew = 1
    cruising_speed = 15
    max_speed = 60
    count_of_passenger = 1
    type_fuel = 'eat'
    type_vehicle = 'muscular'

    def __init__(self, name, color):
        self.name = name
        self.horse_suit = color

    def neighing(self):
        print(f'The {self.name} is neighing.')

    def bite(self):
        print(f'The {self.name} is biting.')

    def gallop(self):
        print(f'The {self.name} is running. Yahoo!!!!')

    def get_fuel(self):
        print(f'The {self.name} is eating.')
