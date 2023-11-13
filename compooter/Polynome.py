from typing import Optional, List, Tuple
from copy import deepcopy
import math

from .Monome import Monome

class Polynome:
    # TODO: Negative coefficients will fuck shit up (first one espech)
    def __init__(self):
        self.monomes = [Monome(0, d) for d in range(3)]
    
    @staticmethod
    def from_coeffs(a, b, c):
        coeffs = [c, b, a]
        out = Polynome()
        out.monomes = [Monome(coeffs[d], d) for d in range(3)]
        return out
         

    
    def evaluate(self, x):
        return sum([m.evaluate(x) for m in self.monomes])
    
    def get_a_b_c(self):
        a = self.monomes[2].c
        b = self.monomes[1].c
        c = self.monomes[0].c
        return a, b, c
        
    def discriminant(self) -> float:
        a, b, c = self.get_a_b_c()
        
        return (b**2 - 4*a*c)
    
    def solve(self):
        if self.degree == 2:
            return self._second_degree_solution()
    
    
    def _second_degree_solution(self) -> Tuple[complex, complex]:
        a, b, c = self.get_a_b_c()
        
        discriminant = self.discriminant()
        # if discriminant == 0:
            # return complex(real = -b / (2*a), im=0), complex(real = -b / (2*a), im=0)
        
        if discriminant >= 0:
            return complex(real = (-b - math.sqrt(discriminant)) / (2*a), imag = 0), complex(real = (-b + math.sqrt(discriminant)) / (2*a), imag=0)
        
        if discriminant < 0:
            thingy = math.sqrt(-discriminant) / (2*a)
            return complex(real = -b / (2*a), imag = thingy), complex(real = -b / (2*a), imag = -thingy)
            
        raise ValueError("This should never print", self)
    
    
    def _first_degree_solution(self):
        assert self.degree == 1

        a, b, c = self.get_a_b_c()
        return c / b
    

    def _zero_degree_solution(self):
        assert self.degree == 0

        a, b, c = self.get_a_b_c()
        
        if c == 0:
            print("All numbers are solutions")
            return (1, 16)
        
        if c != 0:
            print("No solution")
            return (),
        
        
    def reduce(self):
        leading_coeff = self.monomes[self.degree].c
        self.monomes = [m / leading_coeff for m in self.monomes]
    
    def clone(self):
        return deepcopy(self)
    
    @property
    def degree(self):
        fil = filter(lambda x: x.c != 0 or x.d == 0, self.monomes)
        mappe = map(lambda x: x.d, fil)
        return max(mappe)

    def __add__(self, other):
        if isinstance(other, Monome):
            out = self.clone()
            out.monomes[other.d] += other
            return out
        
        if isinstance(other, Polynome):
            out = self.clone()
            for monome in other.monomes:
                out += monome
            return out
        
        raise ValueError("Can only add Monome or Polynome")

    def __sub__(self, other):
        return self + other * -1

    def __mul__(self, other):
        out = self.clone()
        out.monomes = [m * other for m in out.monomes]
        return out


        
    def __str__(self):
        out = "Polynome: "
        first = True
        for m in reversed(self.monomes):
            if not first:
                out += ' + '
            else:
                first = False
            out += str(m)

        return out
    
    def __repr__(self):
        return str(self)        