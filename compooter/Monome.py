
class Monome:
    def __init__(self, coefficient: float, degree: int):
        self.c: float = coefficient
        self.d: int   = degree
        
        if self.d > 2 or self.d < 0:
            raise ValueError("Degree must be inferior to two")
    
    
    def evaluate(self, x):
        return self.c * (x ** self.d)
    
    def __add__(self, other):
        if not isinstance(other, Monome):
            raise ValueError("Can only add two Monomes")
    
        if self.d != other.d:
            raise ValueError(f"Cannont add Monomes of different degrees. {self.d} != {other.d}")
        
        return Monome(self.c + other.c, self.d)


    def __mul__(self, other):
        # if not (isinstance(other, Monome) or isinstance(other, float) or isinstance(other, int)):
            # raise ValueError("Can only mul by Monome or scalar")

        if isinstance(other, Monome):
            return Monome(self.c * other.c, self.d + other.d)
        
        return Monome(self.c * float(other), self.d)
    
    def __truediv__(self, other):
        if isinstance(other, Monome):
            return Monome(self.c / other.c, self.d - other.d)
        
        return Monome(self.c / float(other), self.d)

    def __sub__(self, other):
        return self + (other * -1)

    def __rmul__(self, other):
        return self * other
    
    # def __radd__(self, other):
    #     return self + other
    
    # def __rsub__(self, other):
    #     return self - other

    def __str__(self):
        if self.d == 0:
            return f"{self.c}"
            
        return f"{self.c} * X^{self.d}"
    
    def __repr__(self):
        return str(self)        