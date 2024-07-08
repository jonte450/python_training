import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius ** 3
    return volume

radius = 6
volume = sphere_volume(radius)
print("Volume of the sphere with radius", radius, "is:", volume)
