class Vehicle:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._state = 'off'
        self._motor = Motor(4)

    def accelerate(self,type="slow"):
        if type == "fast":
            self._motor.inject_gas(10)
        else:
            self._motor.inject_gas(3)

        self._state = 'on'

class Motor:
    def __init__(self, cylinder, type='gas'):
        self.cylinder = cylinder
        self.type = type
        self._temperature = 0

    def inject_gas(self,quantity):
        pass