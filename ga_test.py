"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Chace Caven
chacecaven@hotmail.com

Announcements:
 - Refactored tsp science fair program
 - Lambda function points are featured!
 - WAY less code!
 - Fewer variables
 - Code is simple and understandable
 - Helpful comments
Notes:
 - If you input 'point.__dict__' then you will get a dictionary like {'x':0,'y':323,'z':12}
 - There are 3 dimensions, but you can still use only 2 or even 1 by putting 0 in the dimension that you are not using.
 - This uses lambda functions for point instead of dictionaries
 - path_distance(path) is one function that is applied during algorithms
 - Added a sort_by_z algorithm
 - Uses 3D pythag distance
 - Started from scratch, not editing old code
 - example line of code: sort_by_y(generate_points(50,400))


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
from random import randrange
from pprint import pprint
################
## IMPORTANT ###
################
# if you want the program to run, set this to True
run = True

# if you want the distances to be printed, set this to true
print_distances = True

# if you want there to be trials, set this >1
num_trials = 1

# Genetic algorithm variables
generations = 1000
crossover_rate = 1.0
mutation_rate = 0.02
population = 80
frequency_stats = None

# This function is used to make a lambda function with a x, y, and z value
def Point(x=0,y=0,z=0): # If you don't put a x, y, or z value when you are making points, it will automatically be 0
        point1=lambda point1:point1
        point1.x = x
        point1.y = y
        point1.z = z
        return point1
# function for generating points, may put control group in it
def generate_points(quantity,_range_):return [Point(randrange(-_range_,_range_), # x
                                                    randrange(-_range_,_range_), # y
                                                    randrange(-_range_,_range_)) # z
                                              for i in range(quantity)] # number of points
# 3D pythag distance
def pythag_distance(point1,point2):
        return (((((point1.x-point2.x)**2)
                  +((point1.y-point2.y)**2))**0.5)
                +(((point1.z-point2.z)**2)))**0.5
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
        for point in _coords:
                turtle.pendown()
                turtle.circle(5)
                turtle.penup()
                turtle.goto(point.x,point.y)
        turtle.circle(5)
        turtle.home()
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
         dx, dy = x1-x2, y1-y2
         dist = (dx*dx + dy*dy)** 0.5
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
   if ga_engine.getCurrentGeneration() % 100 == 0:
      best = ga_engine.bestIndividual()
      if LAST_SCORE != best.getRawScore():
         write_tour_to_img( coords, best, "tspimg/tsp_result_%d.png" % ga_engine.getCurrentGeneration())
         LAST_SCORE = best.getRawScore()
   return False
 def translate_coords(lambda_func_list):
   coords = []
   for i in lambda_func_list:
           coords.append((i[0],i[1]))
   return coords
 def ga_run():
   #
   coords = translate_coords(path_copy)
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
   #write_tour_to_img(coords,best,"test_run.png")
   return best.getRawScore() # Return that individual's score
 # This returns the value of the score that is returned in ga_run()
 return ga_run()

