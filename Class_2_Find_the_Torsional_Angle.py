import math
class Points(object):
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def __sub__(self, no):
        vector = [d1 - d2 for d1,d2 in zip([self.x,self.y,self.z],[no.x,no.y,no.z])]
        return Points(*vector)
    def dot(self, no):
        sprod = sum([sp1*sp2 for sp1,sp2 in zip([self.x,self.y,self.z],[no.x,no.y,no.z])])
        return(sprod)
    def cross(self, no):
        vprod = [(self.y*no.z)-(self.z*no.y),(self.z*no.x)-(self.x*no.z),(self.x*no.y)-(self.y*no.x)]
        return Points(*vprod)
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
