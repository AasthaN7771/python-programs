class complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self,other):
        return complex(self.real+other.real,self.imaginary+other.imaginary)

    def __sub__(self,other):
        return complex(self.real-other.real,self.imaginary-other.imaginary)

    def __mul__(self,other):
        real_part = ( self.real*other.real)-(self.imaginary*other.imaginary)
        imaginary_part= (self.real*other.imaginary)+(self.imaginary*other.real)
        return complex(real_part,imaginary_part)

    def __truediv__(self,other):
        denominator=(other.real**2+other.imaginary**2)
        if denominator == 0:
            raise valueerror("cannot divide by zero.")
        real_part=(self.real*other.real+self.imaginary*other.imaginary)/ denominator
        imaginary_part = (self.imaginary* other.real -self.real*other.imaginary)/denominator
        return complex(real_part,imaginary_part)
    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} +{self.imaginary}i"

        else :
            return f"{self.real} - {-self.imaginary}i"

        
if __name__=="__main__":
            c1=complex(3,2)
            c2=complex(1,7)

            print("c1",c1)
            print("c2",c2)

            c3=c1+c2
            print("c1+c2",c3)

            c4=c1-c2
            print("c1-c2",c4)

            c5=c1*c2
            print("c1*c2",c5)

            c6=c1/c2
            print("c1/c2",c6)

            

        



        

    

    
