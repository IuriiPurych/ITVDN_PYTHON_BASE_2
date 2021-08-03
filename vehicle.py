class Vehicle:
    type_vehicle = ('ground', 'water', 'air')
    type_fuel = ('eat', )
    driving_force_type = ('muscular', 'animal', 'mechanical')
    max_speed = int
    cruising_speed = int
    carrying = int
    cont_of_crew = int
    count_of_passenger = int

    def ride(self):
        print('Here\'s go.')

    def get_fuel(self):
        print('Yami-Yami.')