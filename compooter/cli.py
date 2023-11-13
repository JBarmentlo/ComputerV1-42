import math
from fire import Fire

from .Parser   import PolynomeParser
from .Polynome import Polynome
from .Monome   import Monome

def _solve(polystr):
    print(polystr)
    parser = PolynomeParser()
    poly = parser.parse(polystr)
    print(f"{poly} = 0")
    print(f"Polynomial Equation of degree {poly.degree}")
    if poly.degree > 2:
        print("I only solve polynomials up to degree 2.")
        return
    # try:
    solutions = poly.solve_print()
    # except Exception as e:
    #     print("Invalid input. Please format as in this example:\n5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0 + 0 * X^1")                
    #     return
    
def do_the_thing():
    Fire(_solve)