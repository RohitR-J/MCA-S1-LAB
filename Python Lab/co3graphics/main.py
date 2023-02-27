from rectangle import *

print("Area of the rectangle is", area(5, 3))
print("Perimeter of the rectangle is", perimeter(5, 3))

from circle import *

print("Area of the circle is", area(5))
print("Perimeter of the circle is", perimeter(5))

from graphics3d import cuboid as cub, sphere as sph
print("Area of the cuboid is", cub.area(6, 5, 8))
print("Perimeter of the cuboid is", cub.perimeter(6, 5, 8))

print("Area of the sphere is", sph.area(6))
print("Perimeter of the sphere is", sph.perimeter(6))