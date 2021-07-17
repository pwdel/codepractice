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

    # __sub__ is supposed to be the "magic" method equivalent of - arithmetic operator
    # __whatever__ is also known as a "dunder" method
    # special methods that start and end with the double underscores
    # Magic methods are not meant to be invoked directly by you, but the
    # invocation happens internally from the class on a certain action.
    # For example, when you add two numbers using the + operator, internally,
    # the __add__() method could be called.
    # so this is the subtraction method
    def __sub__(self, no):
        # no.x - self.x
        # basically subtract number minus given x value
        # x - self.x
        # y - self.y
        # z - self.z
        # each element piecewise
        # we call this within Points() to store result in x,y,z
        return(Points(no.x-self.x, no.y-self.y, no.z-self.z))
        pass

    # the dot product method
    def dot(self, no):
        # self.x is the x variable
        # self.y is the y variable
        # self.z is the z variable
        # x * no.x + y * no.y + z * no.z
        # where the "no" is the number being evaluated
        return(self.x*no.x+self.y*no.y+self.z*no.z)

    # cross product
    def cross(self, no):
        # inputs self, no
        # this follows the definition of a cross product
        # where each "line" of a matrix gets combined with other lines
        # y->z - z->y
        # z->x - x->z
        # x->y - y->x
        # then result gets stored in Points for x,y,z
        return(Points(self.y*no.z-self.z*no.y,
             self.z*no.x-self.x*no.z,
             self.x*no.y-self.y*no.x))

    # absolute value
    # absolute value can be calculated  as sqrt(x^2 + y^2 + z^2)
    # pow() is a, "to the power of" function, as in x^n
    # with pow(x,n)
    # in this case we're doing ^0.5, which is the same as sqrt()
    def absolute(self):
        return(pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5))

if __name__ == '__main__':
    # create an empty list
    points = list()
    # for i at [0,1,2,3]
    for i in range(4):
        # split the input values from the input into a list [x,y,x]
        # map them and turn them into floats
        a = list(map(float, input().split()))
        # then put that into a list
        points.append(a)

    # a, b, c, d
    # the defined planes on points being calculated
    # Asterisks for packing arguments given to function
    # *points
    # * operator can be used to capture an unlimited number of positional arguments given to the function.
    # These arguments are captured into a tuple.
    # so it could be Points(1,2,3) or Points(1,2) or Points(1,2,3,4)
    # the *points makes the number of items going in variable, as long as it's a tuple
    # so a, b, c, d are likely going to have 3 points each, since they are points in 3d space.
    # but hypothetically they could be in 2D or 4D space
    # in the above, we extracted the inputs from 0,1,2 which show 3d space
    # we then put those 3-d tuples into a, b, c, d each
    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    # we then use subtraction and cross product on those points.
    # this gets us plane x and y
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    # next we do a dot product on the planes
    # the below function is the function for the angle
    # it takes into account the dot product and absolute value functions
    # as well as acos (arccosine)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    # simply print out the degree angle to 2 decimalpoint format
    print("%.2f" % math.degrees(angle))
