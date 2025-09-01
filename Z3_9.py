class BasicShape:
    def __init__(self, x):
        self.x = x
        self.n = len(self.x)


    def perimeter(self):
        total = 0.0

        for i in range(self.n):
            x1, y1 = self.x[i]
            x2, y2 = self.x[(i+1) % self.n]
            total +=  self.pram(x1,y1,x2,y2)

        return total

    def square(self):
        total = 0.0

        for i in range(self.n):
            x1, y1 = self.x[i]
            x2, y2 = self.x[(i + 1) % self.n]
            total = total + (x1 * y2) - (x2 * y1)

        return abs(total)*0.5

    @classmethod
    def add(cls, coordinate: tuple[float, float]):
        cls.x.append(coordinate)
        return cls.x


    @staticmethod
    def pram(x1, y1, x2, y2):
        return ((x2-x1)**2+(y2-y1)**2)**0.5

class Quadrilateral(BasicShape):
    def is_rectangle(self):

        t_x = 0.0
        t_y = 0.0
        d_x = 0.0
        t = False

        for i in range(self.n):
            x1, y1 = self.x[i]
            x2, y2 = self.x[(i + 1) % (len(self.x))]
            if i <= 1:
                t_x += self.pram(x1,y1,x2,y2)
            else:
                t_y += self.pram(x1,y1,x2,y2)

        for i in range(1, self.n-1):
            x1, y1 = self.x[i]
            x2, y2 = self.x[(i + 2) % (len(self.x))]
            if d_x == self.pram(x1,y1,x2,y2):
                t = True
                d_x = self.pram(x1,y1,x2,y2)
            else:
                t = False
                d_x = self.pram(x1,y1,x2,y2)

        return t_x == t_y and t == True


    def is_square(self):

        t_x = 0.0
        d_x = 0.0
        t = False
        d = False

        for i in range(self.n):
            x1, y1 = self.x[i]
            x2, y2 = self.x[(i + 1) % (len(self.x))]
            if t_x == self.pram(x1, y1, x2, y2):
                t = True
                t_x = self.pram(x1, y1, x2, y2)
            else:
                t = False
                t_x = self.pram(x1, y1, x2, y2)

        for i in range(1, self.n-1):
            x1, y1 = self.x[i]
            x2, y2 = self.x[(i + 2) % (len(self.x))]
            if d_x == self.pram(x1,y1,x2,y2):
                d = True
                d_x = self.pram(x1,y1,x2,y2)
            else:
                d = False
                d_x = self.pram(x1,y1,x2,y2)

        return t == d


shape = BasicShape([(1,0),(1,3),(4,3),(4,0)])
print(shape.perimeter())
print(shape.square())
print(BasicShape.add((1, 3)))