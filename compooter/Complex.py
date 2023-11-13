from dataclasses import dataclass

@dataclass
class Complex:
    real: float
    im  : float

    def __str__(self):
        if self.im == 0:
            return str(self.real)
        elif self.real == 0:
            return f"{self.im}i"
        return f"{self.real} + {self.im}i"
    
    def __repr__(self):
        return str(self)        