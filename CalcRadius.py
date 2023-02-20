from math import sqrt, pow, sin, cos, pi
import matplotlib.pyplot as plt
import numpy as np

# constants
mass = 0.156 #(kilograms)
spring_constant = 1 #(newtons/meter)
top_radius = 1 #(meters)
gravity = 9.81 #(meters/second^2)

# open the file, wipe it, and print the top of the table
output_file = open("results.txt", "w")
output_file.truncate(0)
output_file.write("|theta\t|radius\t|x\t|y\t|\n")

# setup the arrays to store the points
x_positions = []
y_positions = []

for angle in range(0,361,2):
    # convert angle to radians for being used in the sine function
    radians_angle = angle * (pi/180)

    # calculate the values for a quadratic
    a_term = -spring_constant
    b_term = ((1/2) * spring_constant * top_radius) - ((1/2) * mass * gravity * sin(radians_angle)) + (spring_constant * top_radius) - (mass * gravity * sin(radians_angle))
    c_term = ((3/2) * mass * top_radius * gravity) - ((1/2) * spring_constant * pow(top_radius, 2))

    # calculate the length of the radius with the quadratic formula
    radius = (-(b_term) - sqrt( pow(b_term, 2) - (4 * a_term * c_term ))) / (2 * a_term)

    # convert from polar coordinates to cartesian
    x_position = radius * cos(radians_angle)
    y_position = radius * sin(radians_angle)
    x_positions.append(x_position)
    y_positions.append(y_position)

    # print out the angle and radius
    output_file.write(f"|{angle:7}|{radius:4.9f}|{x_position:4.9f}|{y_position:4.9f}|\n")

# setup the plot
plt.scatter(np.array(x_positions), np.array(y_positions))
plt.minorticks_on()
plt.axis("square")
plt.xlabel("x - meters")
plt.ylabel("y - meters")
plt.savefig("results.png")