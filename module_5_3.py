class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


Building1 = Building(10, 'Жилой дом')
Building2 = Building(10, 'Офисное здание')

print(Building1 == Building2)
