import unittest

#all
class Flights(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

#marcus
# Passengers should have a Name, Passport no, title, DoB, age and nationality
class Passengers(unittest.TestCase):
    def test_initialise(self):
        self.passengers_x = Passengers('Marcus', '12345678A', 'Mr', '01/01/2000', '20', 'British')

    def test_get_name(self):
        self.assertEqual(True, False)

    def test_get_name_passport(self):
        self.assertEqual(True, False)

    def test_title(self):
        self.assertEqual(True, False)

    def test_DoB(self):
        self.assertEqual(True, False)

    def test_age(self):
        self.assertEqual(True, False)

    def test_Nationality(self):
        self.assertEqual(True, False)

#fahad
class Staff(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
#marcus
# ticket type, price,
class Sales(unittest.TestCase):
    def test_ticket_type(self):
        self.assertEqual(True, False)

    def test_set_ticket_price(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
