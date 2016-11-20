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
    return [Point(randrange(-_range_,_range_), # x
                  randrange(-_range_,_range_))# y
                  for i in range(quantity)] # number of points
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
# Sort by X
def sort_by_x(path):
        points = list(path)
        points.sort(key= lambda x:x[0]) # lambda sorting, so no need for operator.itemgetter
        return path_distance(points)
# Sort by Y
def sort_by_y(path):
        points = list(path)
        points.sort(key= lambda y:y[1]) # same as sort_by_x and sort_by_z except for 1 letter
        return path_distance(points)
# Next Nearest
def next_nearest(path):
    end_path = []
    orig_copy = copy.copy(path)
    points_left = []
    for i in range(len(orig_copy)):
        points_left.append([orig_copy[i],i])
    current_point = 0
    end_path.append(orig_copy[current_point])
    for i in range(len(orig_copy)):
        next_closest = sorted([[pythag_distance(orig_copy[current_point],points_left[i][0]),points_left[i][1]] for i in range(len(points_left))])
        end_path.append(orig_copy[next_closest[0][1]])
        current_point = copy.copy(next_closest[0][1])
        points_left = []
        del next_closest[0]
        for i in next_closest:
            points_left.append([orig_copy[i[1]],i[1]])
    #draw_points(end_path)
    return path_distance(end_path)
# Least Closest
def least_closest(path):
        points = list(path)
        points_copy = points
        long_path = []
        current_point = Point()
        for i in range(len(points)):
                # This goes through all the points and calculates the distance to them
                permutations = [[pythag_distance(current_point,point),point] for point in points_copy]
                permutations.sort(reverse=True)# Sorts points farthest to closest
                long_path.append(permutations[0][1])# Adds the point farthest away to the path
                points_copy.remove(permutations[0][1])# Remove the point so it cannot be used again
                current_point = permutations[0][1] # Set the current point to the point selected
        return path_distance(long_path)
# Two Way Switch
def twoOptSwap(path):
    orig_copy = copy.copy(path)
    test_copy = copy.copy(path)
    for coord in range(len(path)):
        otherpoints = []
        for i in range(len(orig_copy)):
            if orig_copy[i] != coord:
                otherpoints.append([orig_copy[i],i])
        closest = sorted([[pythag_distance(path[coord],otherpoints[j][0]),otherpoints[j][1]] for j in range(len(otherpoints))])
        closest5 = closest[:5]
        for i in range(len(closest5)):
            node1 = copy.copy(coord)
            node1_copy = orig_copy[node1]
            node2 = copy.copy(i)
            node2_copy = orig_copy[closest5[node2][1]]
            # Swap the nodes and see if it is shorter than the original one
            test_copy[node1] = copy.copy(node2_copy)
            test_copy[closest5[node2][1]] = copy.copy(node1_copy)
            # if it is shorter, set that one as the copy
            if path_distance(test_copy) < path_distance(orig_copy):
                orig_copy = copy.copy(test_copy)
            else:
                test_copy = copy.copy(orig_copy)
            # return end_path
    return path_distance(orig_copy)
# Three way switch
def threeOptSwap(path):
    orig_copy = copy.copy(path)
    test_copy = copy.copy(path)
    for coord in range(len(path)):
        otherpoints = []
        for i in range(len(orig_copy)):
            if orig_copy[i] != coord:
                otherpoints.append([orig_copy[i],i])
        #closest = sorted([[pythag_distance(path[coord],otherpoints[j][0]),otherpoints[j][1]] for j in range(len(otherpoints))])
        closest = []
        for j in range(len(otherpoints)):
            closest.append([pythag_distance(path[coord],otherpoints[j][0]),otherpoints[j][1]])
        closest.sort()
        closest5 = closest[:5]
        # Go through the closest 5 and do the swapping procedure
        for i in range(len(closest5)):
            # Name all the nodes
            node1 = copy.copy(coord)
            node1_copy = orig_copy[node1]
            node2 = copy.copy(i)
            node2_copy = orig_copy[closest5[node2][1]]
            node3 = copy.copy(randint(-i,i))
            node3_copy = orig_copy[closest5[node3][1]]
            # Swap nodes
            solutions  = ["bca","cab","bac","acb","cba"]
            for i in solutions:
                if i == "acb":
                    test_copy[closest5[node2][1]] = copy.copy(node3_copy)
                    test_copy[closest5[node3][1]] = copy.copy(node2_copy)

                if i == "bac":
                    test_copy[node1] = copy.copy(node2_copy)
                    test_copy[closest5[node2][1]] = copy.copy(node1_copy)

                if i == "cba":
                    test_copy[node1] = copy.copy(node3_copy)
                    test_copy[closest5[node3][1]] = copy.copy(node1_copy)

                if i == "bca":
                    test_copy[node1] = copy.copy(node2_copy)
                    test_copy[closest5[node2][1]] = copy.copy(node3_copy)
                    test_copy[closest5[node3][1]] = copy.copy(node1_copy)
                if i == "cab":
                    test_copy[node1] = copy.copy(node3_copy)
                    test_copy[closest5[node2][1]] = copy.copy(node1_copy)
                    test_copy[closest5[node3][1]] = copy.copy(node2_copy)
                if path_distance(test_copy) < path_distance(orig_copy):
                    orig_copy = copy.copy(test_copy)
                else:
                    test_copy = copy.copy(orig_copy)
    return path_distance(orig_copy)
# Brute Force
def brute_force(path):
    points = list(path)
    import itertools

    def distance(p1, p2):
        return (((((p1[0]-p2[0])**2)
                +((p1[1]-p2[1])**2))**0.5)
                +(((p1[2]-p2[2])**2)))**0.5

    def calCosts(routes, nodes):
        travelCosts = []

        for route in routes:
            travelCost = 0

            #Sums up the travel cost
            for i in range(1,len(route)):
                #takes an element of route, uses it to find the corresponding coords and calculates the distance
                travelCost += distance(nodes[str(route[i-1])], nodes[str(route[i])])

            travelCosts.append(travelCost)

        #pulls out the smallest travel cost
        smallestCost = min(travelCosts)
        shortest = (routes[travelCosts.index(smallestCost)], smallestCost)

        #returns tuple of the route and its cost
        return shortest

    def genRoutes(routeLength):
        #lang hold all the 'alphabet' of nodes
        lang = [ x for x in range(2,routeLength+1) ]

        #uses built-in itertools to generate permutations
        routes = list(map(list, itertools.permutations(lang)))
        #inserts the home city, must be the first city in every route
        for x in routes:
            x.insert(0,1)
        return routes

    def main(nodes=None, instanceSize=5):
        #nodes and instanceSize are passed into main() using another program
        #I just gave them default values for this example

        #The Node lookup table.
        Nodes = {}
        for i in range(len(points)):
            x = points[i].x
            y = points[i].y
            z = points[i].z
            Nodes[str(i)] = (x,y,z)

        routes = genRoutes(instanceSize)
        shortest = calCosts(routes, Nodes)

        print("Shortest Route: ", shortest[0])
        print("Travel Cost: ", shortest[1])

    if __name__ == '__main__':
        main()

