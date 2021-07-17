import math

class Points(object):
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def __sub__(self, no):
        return(Points(no.x-self.x, no.y-self.y, no.z-self.z))

    def dot(self, no):
        return self.x*no.x+self.y*no.y+self.z*no.z

    def cross(self, no):
        return Points(self.y*no.z-self.z*no.y,
             self.z*no.x-self.x*no.z,
             self.x*no.y-self.y*no.x)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


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
