class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors
        return self.buildingType == other.buildingType


Building1 = Building(10, 'Жилой дом')
Building2 = Building(10, 'Офисное здание')
print(Building1.numberOfFloors == Building2.numberOfFloors)
print(Building1.buildingType == Building2.buildingType)
