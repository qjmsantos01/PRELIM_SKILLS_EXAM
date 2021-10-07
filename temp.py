import unittest

class Temperature:
    def __init__(self, kelvin=None, celsius=None, fahrenheit=None):
        values = [x for x in [kelvin, celsius, fahrenheit] if x]

        if len(values) < 1:
            raise ValueError('Need argument')

        if len(values) > 1:
            raise ValueError('Only one argument')

        if celsius is not None:
            self.kelvin = celsius + 273.15
        elif fahrenheit is not None:
            self.kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
        else:
            self.kelvin = kelvin

        if self.kelvin < 0:
            raise ValueError('Temperature in Kelvin cannot be negative')

    def __str__(self):
        return f'Temperature = {self.kelvin} Kelvins'

    
class father(unittest.TestCase):

    def test_uno(self):
        testing1 = Temperature(celsius = 50)
        self.assert_(testing1)
        print('1.) test = ' + str(testing1.kelvin))

    def test_dos(self):
        testing2 = Temperature(fahrenheit = 200)
        self.assert_(testing2)
        print('2.) test = ' + str(testing2.kelvin))
    
    def test_tres(self):
        testing3 = Temperature(celsius = 100)
        self.assert_(testing3)
        print('3.) test = ' + str(testing3.kelvin))
    
    def test_quat(self):
        testing4 = Temperature(fahrenheit = 150)
        self.assert_(testing4)
        print('4.) test = ' + str(testing4.kelvin))

if __name__ == "__main__":
    unittest.main()
