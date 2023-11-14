from typing import Optional, List, Tuple
from copy import deepcopy
import math

from .Monome import Monome

class Polynome:
    # TODO: Negative coefficients will fuck shit up (first one espech)
    def __init__(self):
        self.monomes = {0: Monome(0, 0)}
    
    @staticmethod
    def from_coeffs(a, b, c):
        coeffs = [c, b, a]
        out = Polynome()
        out.monomes = {d: Monome(coeffs[d], d) for d in range(3)}
        return out

    
    def evaluate(self, x):
        return sum([m.evaluate(x) for m in self.monomes.values()])
    
    def get_monome(self, d):
        if d in self.monomes:
            return self.monomes[d]
        return Monome(0, d)
    
    def get_a_b_c(self):
        a = self.get_monome(2).c
        b = self.get_monome(1).c
        c = self.get_monome(0).c
        return a, b, c
        
    def discriminant(self) -> float:
        a, b, c = self.get_a_b_c()
        
        return (b**2 - 4*a*c)
    
    def solve_print(self):
        if self.degree == 2:
            self._print_discriminant()
            solutions = self._second_degree_solution()
            if len(solutions) == 1:
                print(f"There is 1 solution: {solutions[0]:.2f}")
            if len(solutions) == 2:
                print(f"There are 2 solution: {solutions[0]:.2f}, {solutions[1]:.2f}")
        
        if self.degree == 1:
            print(f"There is one solution {self._first_degree_solution():.2f}")
        
        if self.degree == 0:
            self._zero_degree_solution()
    
    def solve(self):
        if self.degree == 2:
            return self._second_degree_solution()
        
        if self.degree == 1:
            return self._first_degree_solution()
        
        if self.degree == 0:
            return self._zero_degree_solution()     
    
    def _print_discriminant(self):
        discriminant = self.discriminant()
        if discriminant > 0:
            print("Strictly positive discriminant.")

        if discriminant == 0:
            print("Nul discriminant.")
        
        if discriminant < 0:
            print("Negative discriminant.")
    
    def _second_degree_solution(self):
        a, b, c = self.get_a_b_c()
        
        discriminant = self.discriminant()
        if discriminant >= 0:
            return ((-b - math.sqrt(discriminant)) / (2*a)),
        
        if discriminant < 0:
            thingy = math.sqrt(-discriminant) / (2*a)
            return complex(real = -b / (2*a), imag = thingy), complex(real = -b / (2*a), imag = -thingy)
            
        raise ValueError("This should never print", self)
    
    
    def _first_degree_solution(self):
        assert self.degree == 1

        a, b, c = self.get_a_b_c()
        return -c / b
    

    def _zero_degree_solution(self):
        assert self.degree == 0

        a, b, c = self.get_a_b_c()
        
        if c == 0:
            print("All numbers are solutions")
            return (12, 0, -123456789)
        
        else:
            print("No solution")
            return None
    
    def reduced(self):
        out = self.clone()
        out._self_reduce()
        return out
        
    def _self_reduce(self):
        leading_coeff = self.monomes[self.degree].c
        self.monomes = {m.d: m / leading_coeff for m in self.monomes.values()}
    
    def clone(self):
        return deepcopy(self)
    
    @property
    def degree(self):
        fil = filter(lambda x: x.c != 0 or x.d == 0, self.monomes.values())
        mappe = map(lambda x: x.d, fil)
        return max(mappe)

    @property
    def min_degree(self):
        fil = filter(lambda x: x.c != 0 or x.d == 0, self.monomes.values())
        mappe = map(lambda x: x.d, fil)
        return min(mappe)

    def __add__(self, other):
        if isinstance(other, Monome):
            out = self.clone()
            out.monomes[other.d] = out.get_monome(other.d) + other
            return out
        
        if isinstance(other, Polynome):
            out = self.clone()
            for monome in other.monomes.values():
                out += monome
            return out
        
        raise ValueError("Can only add Monome or Polynome")

    def __sub__(self, other):
        return self + other * -1

    def __mul__(self, other):
        out = self.clone()
        out.monomes = {m.d: m * other for m in out.monomes.values()}
        return out


        
    def __str__(self):
        out = ""
        first = True
        for m in reversed(self.monomes.values()):
            if m.c == 0:
                continue
            if not first:
                out += ' + '
            else:
                first = False
            out += str(m)
        if out == "":
            out = "0"
        return out
    
    def __repr__(self):
        return str(self)        