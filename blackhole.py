# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import controller 
import model


class Black_Hole(Simulton):  
    
    radius = 10
    
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, 20, 20)
        self._color = "Black"
        
        
    def contains(self, xy):
        if type(xy) == tuple:
            if super().contains(xy):
                return True 
            return False
        else:
            dist = Simulton.distance(self, xy.get_location())
            if dist < self.radius:
                return True
            return False



    def update(self):
        s = set()
        those_eaten = model.find(lambda y: isinstance(y, Prey))
        for p in those_eaten:
            if self.contains(p):
                s.add(p)
                model.remove(p)
        return s
    
    
    
    def display(self, canvas):
        canvas.create_oval(self._x-super().get_dimension()[0]/2, self._y-super().get_dimension()[1]/2, self._x+super().get_dimension()[0]/2, self._y+super().get_dimension()[1]/2, fill=self._color)