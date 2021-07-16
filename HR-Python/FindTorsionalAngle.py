# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem

# first to get the program working in the compiler, we need to add, "pass"
# to the various funcitons to ensure that the program works.


import math

class Points(object):
    # we first need to initialize the variables in an __init__ function.
    # we reference self
    # The first argument of every class method, including init,
    # is always a reference to the current instance of the class.
    # by convention, it is always named, "self"
    # we set up x, y, z
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def __sub__(self, no):
        pass

    def dot(self, no):
        pass

    # cross product
    def cross(self, no):
        # inputs self, no
        # example function call: ().cross(c - b)
        # so what is "no" ?
        c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

         return c

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
