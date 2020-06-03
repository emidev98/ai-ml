class WashingMachine:

    def __init__(self):
        pass

    def wash(self,temperature='warm'):
        self._fill_with_water(temperature)
        self._add_soap()
        self._wash()
        self._spin()


    def _fill_with_water(self,temperature):
        print(f"Filling with {temperature} water")

    def _add_soap(self):
        print("Add soap")

    def _wash(self):
        print("Washing clothes")

    def _spin(self):
        print("Spinning")


if __name__ == '__main__':
    washing_machine = WashingMachine()
    washing_machine.wash()
    washing_machine.wash("cold")