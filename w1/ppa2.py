class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Is_valid(self):
        result = 'Valid'
        if (((self.a + self.b) < self.c) or ((self.a + self.c) < self.b) or ((self.b + self.c) < self.a)):
            result = 'Invalid'
        return(result)

    def Side_Classification(self):
        if self.Is_valid() != 'Valid':
            return("Invalid")

        if ((self.a == self.b) and (self.b == self.c)):
            return('Equilateral')
        if (self.a != self.b) and (self.b != self.c):
            return('Scalene')
        return('Isosceles')

    def Angle_Classification(self):
        if self.Is_valid() != 'Valid':
            return("Invalid")

        (a, b, c) = (-1, -1, -1)
        if self.a > self.b and self.a > self.c:
            c = self.a
            a = self.c
            b = self.b
        elif self.b > self.a and self.b > self.c:
            c = self.b
            a = self.c
            b = self.a
        else:
            c = self.c
            a = self.b
            b = self.a

        t = a**2 + b**2
        if t == c**2:
            return("Right")
        if t > c**2:
            return('Acute')
        return('Obtuse')

    def Area(self):
        if self.Is_valid() != 'Valid':
            return("Invalid")

        s = (self.a + self.b + self.c)/2
        area = (s*(s - self.a)*(s - self.b)*(s - self.c))**(1/2)
        return area

T = Triangle(5,5,5)
print(T.Angle_Classification())