#. Create a class (2-D vector) and use it to create another class representing a 3-Dvector.
class TwoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    
    def show(self):
        print(f'The vector is: {self.i}i + {self.j}j')

class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
        
    def show(self):
        print(f'The vector is: {self.i}i + {self.j}j + {self.k}k')

m=TwoDVector(1,2)
m.show()
n=ThreeDVector(1,2,3)
n.show()