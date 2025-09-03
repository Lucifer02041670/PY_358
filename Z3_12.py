class BasicShape:
    def __init__(self, x):
        self.x = x
        self.n = len(self.x)

    @property
    def perimeter(self):
        total = 0.0

        for i in range(self.n):
            x1, y1 = self.x[i]
            x2, y2 = self.x[(i+1) % self.n]
            total +=  self.pram(x1,y1,x2,y2)

        return total

    @property
    def square(self):
        total = 0.0

        for i in range(self.n):
            x1, y1 = self.x[i]
            x2, y2 = self.x[(i + 1) % self.n]
            total = total + (x1 * y2) - (x2 * y1)

        return abs(total)*0.5

    def add(self, coordinate: tuple[float, float]):
        if type(self) is Quadrilateral:
            raise AttributeError("Метод add не поддерживается для Quadrilateral")
        else:
            self.x.append(coordinate)
            self.n += 1

    @staticmethod
    def pram(x1, y1, x2, y2):
        return ((x2-x1)**2+(y2-y1)**2)**0.5

    def __add__(self, other):
        return self.square + other.square

    def __sub__(self, other):
        return self.square - other.square

    def __mul__(self, other):
        return self.square * other.square

    def __truediv__(self, other):
        if other.square != 0:
            return self.square / other.square
        else:
            raise ZeroDivisionError("площадь фигуры равна 0, деление невозможно")



class Quadrilateral(BasicShape):

    @property
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

    @property
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

class Shapes:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        if type(shape) is BasicShape:
            self.shapes.append(shape)
        else:
            raise TypeError("Можно добавлять только объекты типа BasicShape")

    def remove_shape(self, shape):
        if shape in self.shapes:
            self.shapes.remove(shape)
        else:
            raise ValueError("Фигура не найдена")

    def square(self):
        total_area = 0.0
        for shape in self.shapes:
            total_area += shape.square
        return total_area

    def perimeter(self):
        total_perimeter = 0.0
        for shape in self.shapes:
            total_perimeter += shape.perimeter
        return total_perimeter

    def add(self, shape, coordinate):
        if shape in self.shapes:
            shape.x.append(coordinate)
            shape.n += 1
        else:
            raise ValueError("Фигура не найдена")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Суммарная площадь всех фигур:", self.square())
        return False

if __name__ == "__main__":

    shape1 = BasicShape([(0,0), (0,3), (2,3), (2,0)])
    shape2 = BasicShape([(1,1), (1,4), (1,1), (1,4)])
    quad = Quadrilateral([(0,0), (0,3), (3,3), (3,0)])

    print(shape1.perimeter)
    print(shape1.square)

    shape1.add((6, 3))
    print(shape1.x)
    print(shape1 - shape2)
    shape_col = Shapes()
    shape_col.add_shape(shape1)
    shape_col.add_shape(shape2)
    print(shape_col.square())

    with shape_col as shapes:
        shapes.add(shape1, (0.5, 0.5))  # Добавляем новую точку к shape1
        shapes.add(shape2, (1, 1))