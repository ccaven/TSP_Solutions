# Genetic Algorithm
generations = 300
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
    def init_solution(coords):
        import next_nearest as nn
        return nn.greedy_algo(coords)[1]
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
        padding=400
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
    def G1DListTSPInitializator(genome,**args):
        lst = []
        size = genome.getListSize()
        coords = get_coords(path_copy)
        print coords
        new_coords = init_solution(coords)[1]
        print new_coords
        for i in range(size):
            lst.append(coords.index(new_coords[i]))
        genome.setInternalList(lst)
    # This updates the score
    def evolve_callback(ga_engine,points):
        global LAST_SCORE
        if ga_engine.getCurrentGeneration() % 100 == 0:
            best = ga_engine.bestIndividual()
            if LAST_SCORE != best.getRawScore():
                print points
                write_tour_to_img( points, best, "tspimg_tsp_result_%d.png" % ga_engine.getCurrentGeneration())
                LAST_SCORE = best.getRawScore()
        return False
    def get_coords(points):
        coords = []
        for point in points:
            coords.append(point)
        return coords
    def ga_run():
        global cm, coords, WIDTH, HEIGHT,best
        coords = get_coords(path_copy)
        cm     = cartesian_matrix(coords)
        genome = G1DList.G1DList(len(coords))

        genome.evaluator.set(lambda chromosome: tour_length(cm, chromosome))
        genome.crossover.set(Crossovers.G1DListCrossoverEdge)
        genome.initializator.set(G1DListTSPInitializator)

        ## This sets all the GA parameters
        ga = GSimpleGA.GSimpleGA(genome)
        ga.setGenerations(1000)
        ga.setMinimax(Consts.minimaxType["minimize"])
        ga.setCrossoverRate(1.0)
        ga.setMutationRate(0.01)
        ga.setPopulationSize(80)
        ga.evolve(freq_stats=50) # Runs the GA
        best = ga.bestIndividual() # Finds the best scoring individual
        print coords
        evolve_callback(ga,coords)
        return best.getRawScore() # Return that individual's score
 # This returns the value of the score that is returned in ga_run()
    return ga_run()
import tsp_functions as fun

print GA(fun.generate_points(25,50))
