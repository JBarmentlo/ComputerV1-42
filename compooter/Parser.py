import logging
import re
import sys

from .Monome import Monome
from .Polynome import Polynome

logging.basicConfig()
logger = logging.getLogger("Parser")
logger.setLevel(logging.INFO)

class PolynomeParser:
    def __init__(self):
        self.current_string = ""
    
    def parse(self, polystr: str):
        if len(polystr.split("=")) == 2:
            one, two = polystr.split("=")
            poly = self._parse(one) - self._parse(two)

        if len(polystr.split("=")) == 1:
            poly = self._parse(polystr)

        return poly
    
    def parse_and_print(self, polystr: str):
        poly = self.parse(polystr)
        print(f"{poly} = 0")
    
    
    def _parse(self, polystr: str):
        self.current_string = polystr
        polynome = Polynome()
        self.initial_cleaning()
        while len(self.current_string) > 0:
            polynome += self.get_monome()
        
        return polynome
    
    def initial_cleaning(self):
        logger.debug(f"Cleaning string: {self.current_string}")
        self.current_string = self.current_string.replace(" ", "")
        self.current_string = "+" + self.current_string
        logger.debug(f"Done: {self.current_string}")
    
    
    def _starts_with_sign(self):
        return self.current_string.startswith(("+", "-"))
    
    
    def _get_sign(self) -> int:
        if len(self.current_string) == 0:
            raise ValueError("Getting sign on empty string")
        
        if self.current_string[0] == "+":
            return 1
        
        if self.current_string[0] == "-":
            return -1
        
        raise ValueError(f"String doesn't start with sign: {self.current_string}")
    
    
    def get_sign(self):
        if not self._starts_with_sign():
            print("Invalid input, Missing operator")
            sys.exit(0)
        logger.debug(f"Getting sign")
        
        sign = 1
        while self._starts_with_sign():
            sign = sign * self._get_sign()
            self.current_string = self.current_string[1:]
        
        logger.debug(f"{sign = }. str = {self.current_string}")
        return sign
    
    
    def get_coeff(self):
        logger.debug(f"Getting coef")
        
        coef_str, *_ = self.current_string.split("*")
        try:
            coef = float(coef_str)
        except ValueError:
            print(f"Invalid input")
            sys.exit(0)
        self.current_string = self.current_string[len(coef_str):]
        
        logger.debug(f"{coef = }. str = {self.current_string}")
        return coef


    def remove_multiply(self):
        logger.debug("Removing *")
        if not self.current_string.startswith("*"):
            print("Invalid input, Missing multiply")
            sys.exit(0)
        self.current_string = self.current_string.removeprefix("*")
        logger.debug(f"Done. str = {self.current_string}")
          

    
    def get_degree(self):
        logger.debug(f"Getting degree")
        if not self.current_string.startswith("X^"):
            print("Invalid input, Missing 'X'")
            sys.exit(0)
            
        self.current_string = self.current_string.removeprefix("X^")
        degree_str, *_ = re.split("[-|\+]", self.current_string)
        self.current_string = self.current_string.removeprefix(degree_str)
        try:
            degree = int(degree_str)
        except ValueError:
            print(f"Invalid input (degree)")
            sys.exit(0)
            
        logger.debug(f"{degree = }. str = {self.current_string}")
        return degree
    
    def get_monome(self):
        sign = self.get_sign()
        coef = self.get_coeff() * sign
        self.remove_multiply()
        deg  = self.get_degree()
        
        return Monome(coef, deg)
        
        