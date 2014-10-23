from classes import Dimension
from conversions import *

acceleration = Dimension(acceleration_dimcon, 'm/s^2')
angle = Dimension(angle_dimcon, 'radian')
area = Dimension(area_dimcon, 'm^2')
energy = Dimension(energy_dimcon, 'J')
force = Dimension(force_dimcon, 'N')
length = Dimension(length_dimcon, 'm')
mass = Dimension(mass_dimcon, 'kg')
pressure = Dimension(pressure_dimcon, 'N/m^2')
time = Dimension(time_dimcon, 's')
velocity = Dimension(velocity_dimcon, 'm/s')
volume= Dimension(volume_dimcon, 'm^3')

dimconlib = (acceleration, angle, area, energy, force, length, mass, pressure,
 time, velocity, volume)

for i in dimconlib:
    i.get_base()
