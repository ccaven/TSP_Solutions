from random import randrange, randint
from pprint import pprint
import copy
################
## IMPORTANT ###
################
def setup():
    # if you want the program to run, set this to True
    global run
    run = True

    # if this is true, then the turtle module will draw out the points on a canvas
    global UI
    UI = True

    # if you want the distances to be printed, set this to true
    global print_distances
    print_distances = True

    # if you want there to be trials, set this >1
    global num_trials
    num_trials = 10

    # point-related variables
    global num_points,range_of_coords
    num_points = 50
    range_of_coords = 400 # This is the range of the coordinates.

    # Genetic algorithm variables
    global generations,crossover_rate,mutation_rate,population,frequency_stats
    generations = 300
    crossover_rate = 1.0
    mutation_rate = 0.02
    population = 80
    frequency_stats = None
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
        r = (((point1[0]-point2[0])**2)
            +((point1[1]-point2[1])**2))**0.5
    except:
        print((point1,point2))
        raise ValueError
    return r
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
    draw_points(orig_copy)
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
# Genetic Algorithm
def GA(path):
 path_copy = list(path)
 from pyevolve import G1DList,GAllele,GSimpleGA,Mutators,Crossovers,Consts
 import sys, random
 random.seed(1024)

 # PIL is for making images. These next lines of code sense if the computer has the PIL download
 PIL_SUPPORT = None
 try:
   from PIL import Image, ImageDraw, ImageFont
   PIL_SUPPORT = True
 except:
   PIL_SUPPORT = False

 # These are all the variables the GA uses
 global LAST_SCORE
 cm     = []
 coords = []
 num_of_points = len(path)
 WIDTH   = 1024
 HEIGHT  = 768
 LAST_SCORE = -1

 # Pythag distance matrix
 def cartesian_matrix(coords):
   """ A distance matrix """
   matrix={}
   for i,(x1,y1) in enumerate(coords):
      for j,(x2,y2) in enumerate(coords):
         dx, dy= x1-x2, y1-y2
         dist=(dx*dx + dy*dy)** 0.5
         matrix[i,j] = dist
   return matrix

 # This is the pyevolve version of path_distance
 def tour_length(matrix, tour):
   """ Returns the total length of the tour """
   total = 0
   t = tour.getInternalList()
   for i in range(num_of_points):
      j      = (i+1)%num_of_points
      total += matrix[t[i], t[j]]
   return total

 # This is for making images for the path that the GA took
 def write_tour_to_img(coords, tour, img_file):
   """ The function to plot the graph """
   padding=20
   coords=[(x+padding,y+padding) for (x,y) in coords]
   maxx,maxy=0,0
   for x,y in coords:
      maxx, maxy = max(x,maxx), max(y,maxy)
   maxx+=padding
   maxy+=padding
   img=Image.new("RGB",(int(maxx),int(maxy)),color=(255,255,255))
   font=ImageFont.load_default()
   d=ImageDraw.Draw(img);
   num_num_of_points=len(tour)
   for i in range(num_of_points):
      j=(i+1)%num_num_of_points
      city_i=tour[i]
      city_j=tour[j]
      x1,y1=coords[city_i]
      x2,y2=coords[city_j]
      d.line((int(x1),int(y1),int(x2),int(y2)),fill=(0,0,0))
      d.text((int(x1)+7,int(y1)-5),str(i),font=font,fill=(32,32,32))

   for x,y in coords:
      x,y=int(x),int(y)
      d.ellipse((x-5,y-5,x+5,y+5),outline=(0,0,0),fill=(196,196,196))
   del d
   img.save(img_file, "PNG")

 # The initializator for the TSP
 def G1DListTSPInitializator(genome, **args):
   lst = [i for i in xrange(genome.getListSize())]
   random.shuffle(lst)
   genome.setInternalList(lst)
 # This updates the score
 def evolve_callback(ga_engine):
   global LAST_SCORE
   if ga_engine.getCurrentGeneration() % 100 == 0:
      best = ga_engine.bestIndividual()
      if LAST_SCORE != best.getRawScore():
         write_tour_to_img( coords, best, "tspimg/tsp_result_%d.png" % ga_engine.getCurrentGeneration())
         LAST_SCORE = best.getRawScore()
   return False
 def get_coords(points):
  global coords
  coords = []
  for point in points:
   coords.append((point[0],point[1]))
 def ga_run():
   global cm, coords, WIDTH, HEIGHT,best
   get_coords(path_copy)
   cm     = cartesian_matrix(coords)
   genome = G1DList.G1DList(len(coords))

   genome.evaluator.set(lambda chromosome: tour_length(cm, chromosome))
   genome.crossover.set(Crossovers.G1DListCrossoverEdge)
   genome.initializator.set(G1DListTSPInitializator)

   ## This sets all the GA parameters
   ga = GSimpleGA.GSimpleGA(genome)
   ga.setGenerations(generations)
   ga.setMinimax(Consts.minimaxType["minimize"])
   ga.setCrossoverRate(crossover_rate)
   ga.setMutationRate(mutation_rate)
   ga.setPopulationSize(population)
   ga.evolve(freq_stats=frequency_stats) # Runs the GA
   best = ga.bestIndividual() # Finds the best scoring individual
   return best.getRawScore() # Return that individual's score
 # This returns the value of the score that is returned in ga_run()
 return ga_run()
# Runs all the algorithms
def run_algorithms(num_trials):
        setup()
        end_distances = {'sort by x':0,'sort by y':0,'next nearest':0,'GA':0,'least closest':0,'two way switch':0, 'three way switch':0}
        functions = {'sort by x':sort_by_x,'sort by y':sort_by_y,'next nearest':next_nearest,'GA':GA,'least closest':least_closest,'two way switch':twoOptSwap, 'three way switch':threeOptSwap}
        for i in range(num_trials):
                _points_ = [(0,0)]
                _points_ += generate_points(num_points,range_of_coords)
                _points_.append((0,0))
                print('\nWe are on trial ' + str(i+1) + '\n')
                distances = {'sort by x':0,'sort by y':0,'next nearest':0,'GA':0,'least closest':0,'two way switch':0,'three way switch':0}
                path_list = copy.copy(_points_)
                for i in distances:
                    distances[i] = functions[i](path_list)
                    end_distances[i] += distances[i]
                if print_distances:
                        print('The distances are:\n')
                        pprint(distances)
        for i in end_distances:
               end_distances[i] /= num_trials
        if print_distances:
                print('The end distances are:\n')
                pprint(end_distances)
run_algorithms(1)
# Runs the UI

