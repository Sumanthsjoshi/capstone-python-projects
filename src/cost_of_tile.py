"""This is a program to calculate cost of tiles to cover a W*H floor"""
# Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it
# would take to cover a floor plan of width and height, using a cost entered by
# the user.
from src.utils.get_number_input import get_number_input


class TileCostCalculator:
    """A class which calculates the cost of tiles for given floor plan of width
    and height"""
    def __init__(self, tile_cost, width=1, height=1):
        self.width = width
        self.height = height
        self.tile_cost = tile_cost

    def get_tile_cost(self, r=2):
        return round(self.width * self.height * self.tile_cost, r)


tc = get_number_input("Please provide a tile cost per sq meter: ", float)
w = get_number_input("Please provide a floor width in meters: ", float)
h = get_number_input("Please provide a floor height in meters: ", float)
tcc = TileCostCalculator(tc, w, h)
print(tcc.get_tile_cost(3))
