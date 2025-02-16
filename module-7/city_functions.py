# Name: Justin Morrow
# Date: 02/15/2025
# Assignment: CSD325 Module 7.2 "Test Cases: city_functions.py"
# Purpose:  write a Python program that produces the required results and tests them with the module unittest
# Reference: Python Software Foundation. (n.d.). unittest — Unit testing framework
# https://docs.python.org/3/library/unittest.html
# Reference: Matthes, E. (2019). Python crash course: A hands-on, project-based introduction to programming (2nd ed.)
# https://library-books24x7-com.ezproxy.bellevue.edu/assetviewer.aspx?bookid=146803&chunkid=960165520
# Reference: Lucidbrot (2018, September 25). Call function without optional arguments if they are None. Stack Overflow.
# https://stackoverflow.com/questions/52494128/call-function-without-optional-arguments-if-they-are-none

# Creating a function to pass a City and Country as City,Country. Using title to force capitalization of each word
# Updated version now includes the 3rd parameter for population. I formated it so it uses a comma in the results
# Updated version to allow population to be option utilizing if/else statements
# Updated version to include language. To allow this to pass without assigning =None I have to put before population
def city_country(city, country, population=None, language=None):
    if population is None and language is None:
        return (f"{city.title()}, {country.title()}")
    elif population is None:
        return (f"{city.title()}, {country.title()}, {language.capitalize()}")
    elif language is None:
        return (f"{city.title()}, {country.title()} - population {int(population):,}")
    else:
        return (f"{city.title()}, {country.title()} - population {int(population):,}, {language.capitalize()}")


# Calling the city_country function 3 times using places I have family ties to
# Changed the text case to ensure .title capitalizes the first letter and lower case each other letter per each word
# Updated to verify the results pass with a population, with no population parameter entered or population=None
# Updated to include language and entered in different casing to confirm .capitalize formatting
print(city_country(city="albuquerque", country="UNITED States of America", population="500000", language="english"))
print(city_country(city="Palermo", country="sicily", language="ITALIAN"))
print(city_country(city="oslo", country="norway", population=None))
