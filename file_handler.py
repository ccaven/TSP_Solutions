def read_coords(coord_file):
   """ Read the coords from file """
   coords=[]
   for line in coord_file:
      x,y=line.strip().split(",")
      coords.append((float(x),float(y)))
   return coords

def write_random(filename, cities, xmax=800, ymax=600):
   """ Write random cities/positions to a text file """
   filehandle = open(filename, "w")
   for i in xrange(cities):
      x = random.randint(0, xmax)
      y = random.randint(0, ymax)
      filehandle.write("%d,%d\n" % (x,y))
   filehandle.close() 
