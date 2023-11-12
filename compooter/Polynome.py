from typing import Optional, List
from copy import deepcopy
from .Monome import Monome

class Polynome:
    def __init__(self):
        self.monomes = [Monome(0, d) for d in range(3)]


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

    
    def clone(self):
        return deepcopy(self)
    
    @property
    def degree(self):
        fil = filter(lambda x: x.c != 0 or x.d == 0, self.monomes)
        mappe = map(lambda x: x.d, fil)
        return max(mappe)
        
    def __str__(self):
        out = "Polynome: "
        first = True
        for m in self.monomes:
            if not first:
                out += ' + '
            else:
                first = False
            out += str(m)

        return out
    
    def __repr__(self):
        return str(self)        