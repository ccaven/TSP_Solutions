from random import randrange, randint
from pprint import pprint
import copy
################
## IMPORTANT ###
################
# This function is used to make a lambda function with a x and y value
# If you don't put a x, y, or z value when you are making points, it will automatically be 0
def Point(x=0,y=0):
        #point1=lambda point1:point1
        #point1.x = x
        #point1.y = y
        #point1.z = z
        return (x,y)
# function for generating points, may put control group in it
def generate_points(quantity,_range_):
    return [Point(randrange(0,_range_), # x
                  randrange(0,_range_))# y
                  for i in range(quantity)] # number of points
def get_points(filename):
    coords = []
    with open('coord.txt','r') as f:
        i = 0
        for line in f.readlines():
            line = [float(i.replace('\n','')) for i in line.split(' ')]
            coords.append([])
            for j in range(1,3):
                coords[i].append(line[j])
            i += 1
    return coords

# 3D pythag distance
def pythag_distance(point1,point2):
    try:
        dist = (((point1[0]-point2[0])**2)
            +((point1[1]-point2[1])**2))**0.5
    except:
        print((point1,point2))
        raise ValueError
    return dist
# This is used to calculate the length of a path
def path_distance(path):
        start = Point()
        current_point = start
        dist = 0
        for point in path:
                dist += pythag_distance(current_point,point)
                current_point = point
        dist += pythag_distance(current_point,start)
        return dist
# Draws the points on a 2D canvas. ONLY WORKS WITH 2D POINTS!!!
def draw_points(coords,color='green'):
        import turtle
        turtle.home()
        turtle.color(color)
        for point in coords:
                turtle.pendown()
                turtle.circle(5)
                turtle.goto(point[0],point[1])
        turtle.circle(5)
        turtle.home()
def dist_matrix(coords):
    return [[pythag_distance(i,j) for i in coords] for j in coords]
