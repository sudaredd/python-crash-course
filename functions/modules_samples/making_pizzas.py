"""We can import 3 ways as below
1. import module
2. import specific functions from module
3. alias
4. import all functions from module
"""
import pizza
from pizza import make_pizza
from pizza import make_pizza as mp
from pizza import *

pizza.make_pizza(16, 'pepperoni')
make_pizza(12, 'Green pepper', 'Mushroom', 'Spinach')
mp(12, 'Chicken', 'Onion')