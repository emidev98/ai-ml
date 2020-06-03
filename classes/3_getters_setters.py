class Vehicle:
    def __init__(self, brand, types):
        self._brand = brand
        self._types = types
        self._type = None

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self,type):
        if type in self._types:
            self._type = type;
        else:
            raise ValueError(f"{type} not available in {self._types}")

if __name__ == "__main__":
    vehicle = Vehicle("BMW",["S1","S2","S3","X"])
    vehicle.type = "S03"