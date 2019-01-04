import math

class Sphere(object):

    def __init__(self, R, x = 0.0, y = 0.0, z = 0.0):
        self.R = R
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        self.volume = 4*math.pi*self.R**3/3
        return self.volume

    def get_square(self):
        self.square = 4*math.pi*self.R**2
        return self.square

    def get_radius(self):
        return self.R

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, R):
        self.R = R

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x,y,z):
        return self.R*self.R >= (x-self.x)*(x-self.x) + (y-self.y)*(y-self.y) + (z-self.z)*(z-self.z)


sph = Sphere(0.5) # test sphere creation with radius and default center
print (sph.get_center()) # (0.0, 0.0, 0.0)
print (sph.get_volume()) # 0.523598775598
print (sph.is_point_inside(0, -1.5, 0)) # False
sph.set_radius(1.6) 
print (sph.is_point_inside(0, -1.5, 0)) # True
print (sph.get_radius()) # 1.6