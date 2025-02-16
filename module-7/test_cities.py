# Name: Justin Morrow
# Date: 02/15/2025
# Assignment: CSD325 Module 7.2 "Test Cases: test_cities.py"
# Purpose:  write a Python program that produces the required results and tests them with the module unittest
# Reference: Python Software Foundation. (n.d.). unittest — Unit testing framework
# https://docs.python.org/3/library/unittest.html
# Reference: Matthes, E. (2019). Python crash course: A hands-on, project-based introduction to programming (2nd ed.)
# https://library-books24x7-com.ezproxy.bellevue.edu/assetviewer.aspx?bookid=146803&chunkid=960165520

# Import statements
import unittest
from city_functions import city_country

# Class to test the city_country function as seen in the Python Crash Course (test_name_function.py) section
class TestCityCountry(unittest.TestCase):
    def test_city_functions(self):
        result = city_country('Palermo', 'Sicily')
        self.assertEqual(result,'Palermo, Sicily')

if __name__ == '__main__':
    unittest.main()