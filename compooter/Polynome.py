from typing import Optional, List, Tuple
from copy import deepcopy
import math

from .Monome import Monome
from .Complex import Complex

class Polynome:
    # TODO: Negative coefficients will fuck shit up (first one espech)
    def __init__(self):
        self.monomes = [Monome(0, d) for d in range(3)]

    
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
    
    
    def _second_degree_solution(self) -> Tuple[Complex, Complex]:
        a, b, c = self.get_a_b_c()
        
        discriminant = self.discriminant()
        # if discriminant == 0:
            # return Complex(real = -b / (2*a), im=0), Complex(real = -b / (2*a), im=0)
        
        if discriminant >= 0:
            return Complex(real = (-b - math.sqrt(discriminant)) / (2*a), im = 0), Complex(real = (-b + math.sqrt(discriminant)) / (2*a), im=0)
        
        if discriminant < 0:
            thingy = math.sqrt(-discriminant) / (2*a)
            return Complex(real = -b / (2*a), im = thingy), Complex(real = -b / (2*a), im = -thingy)
            
            
            
        
        
    
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