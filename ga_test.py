# The follow TSP routines was get from the above site, I'm too lazy to reinvent a new pretty wheel:
# http://www.psychicorigami.com/2007/04/17/tackling-the-travelling-salesman-problem-part-one/
# Routines:
# - cartesian_matrix
# - read_coords
# - tour_length
# - write_tour_to_img

from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import GAllele
from pyevolve import Mutators
from pyevolve import Initializators
from pyevolve import DBAdapters
from pyevolve import Crossovers
from pyevolve import Consts
import sys, random
import tsp_functions as tsp
from math import sqrt

PIL_SUPPORT = None

try:
   from PIL import Image, ImageDraw, ImageFont
   PIL_SUPPORT = True
except:
   PIL_SUPPORT = False

def cartesian_matrix(coords):
   """ A distance matrix """
   matrix={}
   for i,(x1,y1) in enumerate(coords):
      for j,(x2,y2) in enumerate(coords):
         dx,dy=x1-x2,y1-y2
         dist=sqrt(dx*dx + dy*dy)
         matrix[i,j]=dist
   return matrix

def read_coords(coord_file):
   """ Read the coords from file """
   coords=[]
   for line in coord_file:
      x,y=line.strip().split(",")
      coords.append((float(x),float(y)))
   return coords

def tour_length(matrix, tour):
   """ Returns the total length of the tour """
   total=0
   num_cities=len(tour)
   for i in range(num_cities):
      j=(i+1)%num_cities
      city_i=tour[i]
      city_j=tour[j]
      total+=matrix[city_i,city_j]
   return total

def write_tour_to_img(coords, matrix, tour, img_file):
   """ The function to plot the graph """
   padding=500
   coords=[(x+padding,y+padding) for (x,y) in coords]
   maxx = max([point[0] for point in coords])
   maxy = max([point[1] for point in coords])
   img=Image.new("RGB",(int(maxx*1.2),int(maxy*1.2)),color=(255,255,255))
   font = ImageFont.truetype("verdana.ttf",14)
   d=ImageDraw.Draw(img);
   num_cities=len(tour)
   for i in range(num_cities):
      j=(i+1)%num_cities
      city_i=tour[i]
      city_j=tour[j]
      x1,y1=coords[city_i]
      x2,y2=coords[city_j]
      d.line((int(x1),int(y1),int(x2),int(y2)),fill=(0,0,0))
      d.text((int(x1)+7,int(y1)-5),str(i),font=font,fill=(32,32,32))
   
   for x,y in coords:
      x,y=int(x),int(y)
      d.ellipse((x-5,y-5,x+5,y+5),outline=(0,0,0),fill=(196,196,196))
   dist = tour_length(cm,tour)
   d.text((maxx/2,maxy*1.1),str(dist),(0,0,0),font=font)

   del d
   img.save(img_file, "PNG")

   print "The plot was saved into the %s file." % (img_file,)

def G1DListTSPInitializator(genome, **args):
   """ The initializator for the TSP """
   genome.clearList()
   lst = [i for i in xrange(genome.getListSize())]

   for i in xrange(genome.getListSize()):
      choice = random.choice(lst)
      lst.remove(choice)
      genome.append(choice)

cm = []
coords = []

def eval_func(chromosome):
   """ The evaluation function """
   global cm
   return tour_length(cm, chromosome)

def write_random(filename, cities, xmax=800, ymax=600):
   """ Write random cities/positions to a text file """
   filehandle = open(filename, "w")
   for i in xrange(cities):
      x = random.randint(0, xmax)
      y = random.randint(0, ymax)
      filehandle.write("%d,%d\n" % (x,y))
   filehandle.close()   

# This is to make a video of best individuals along the evolution
# Use mencoder to create a video with the file list list.txt
# mencoder mf://@list.txt -mf w=400:h=200:fps=3:type=png -ovc lavc
#          -lavcopts vcodec=mpeg4:mbd=2:trell -oac copy -o output.avi
#
fitness_list = []
def evolve_callback(ga_engine):
   if ga_engine.currentGeneration % 50 == 0:
      best = ga_engine.bestIndividual()
      fitness_list.append(best.getRawScore())
      write_tour_to_img( coords,cm, best, "tsp_result_%d.png" % (ga_engine.currentGeneration,))
   return False

def main_run(path):
   global cm, coords

   # write_random(filename, number of the cities, max width, max height)
   #write_random("tsp_coords.txt", 50, 400, 400)

   # load the tsp data file
   filehandle = open("tsp_coords.txt", "r")
   coords = path
   cm = cartesian_matrix(coords)

   # set the alleles to the cities numbers
   setOfAlleles = GAllele.GAlleles(homogeneous=True)
   lst = [ i for i in xrange(len(coords)) ]
   a = GAllele.GAlleleList(lst)
   setOfAlleles.add(a)
      
   genome = G1DList.G1DList(len(coords))
   genome.setParams(allele=setOfAlleles)

   genome.evaluator.set(eval_func)
   genome.mutator.set(Mutators.G1DListMutatorSwap)
   genome.crossover.set(Crossovers.G1DListCrossoverOX)
   genome.initializator.set(G1DListTSPInitializator)

   ga = GSimpleGA.GSimpleGA(genome)
   ga.setGenerations(300)
   ga.setMinimax(Consts.minimaxType["minimize"])
   ga.setCrossoverRate(1.0)
   ga.setMutationRate(0.03)
   ga.setPopulationSize(80)

   #sqlite_adapter = DBAdapters.DBSQLite(identify="tsp", commit_freq=1000, frequency=500)
   #ga.setDBAdapter(sqlite_adapter)

   # This is to make a video
   # ga.stepCallback.set(evolve_callback)

   ga.evolve(freq_stats=100)
   best = ga.bestIndividual()
   best.fitness_list = fitness_list
   if PIL_SUPPORT:
      write_tour_to_img(coords,cm, best, "tsp_result_%d.png")
   else:
      print "No PIL detected, cannot plot the graph !"
   return [best.getRawScore(), fitness_list]
import tsp_functions as tsp
coords = tsp.generate_points(50,400)
print main_run(coords)

