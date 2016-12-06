import sort_by_X as sx
import sort_by_Y as sy
import next_nearest as nn
import brute_force as bf
import three_opt_swap as opt3
import two_opt_swap as opt2
import pprint
<<<<<<< HEAD
import tsp_functions as fun

try:
    import ga_test as ga
    pye_support = True
except:
    pye_support = False
    
try:
    import anneal as sa
    from visualize_tsp import plotTSP as pic
    sa_support = True
except:
    sa_support = False


import file_handler as op
=======
import tsp_functions
#import Genetic_Algorithm
import anneal
import visualize_tsp
>>>>>>> 607273b85d32ee900701a0e5de2ea6d6022c6749
end_distances = {"sort by x":0,"sort by y":0,"two opt swap":0,"three opt swap":0,"next nearest":0,"brute force":0,"ga":0,"sa":0}
num_trials = 10

# Runs each algorithm
for i in range(num_trials):

    #Test comment

    distances = {"sort by x":0,"sort by y":0,"next nearest":0,"two opt swap":0,"three opt swap":0,"brute force":0,"ga":0,"sa":0}

<<<<<<< HEAD
    coords = op.read_coords(open("trial%d" % i))

    distances["sort by y"] = sy.sort_by_y(coords)[0]

    distances["sort by x"] = sx.sort_by_x(coords)[0]

    distances["two opt swap"] = opt2.twoOptSwap(coords)[0]

    distances["three opt swap"] = opt3.threeOptSwap(coords)[0]

    distances["next nearest"] = nn.greedy_algo(coords)[0]

    if sa_support:
        
        distances["sa"] = sa.SimAnneal(coords).Anneal()[0]
        
    else:
        
        print "no sa support, cannot run simulated annealing"
    
    if pye_support:
        
        distances["ga"] = ga.GA(coords)
        
    else:
        
        print "no pyevolve support, cannot run ga"
        
    print("Trial " + str(i) + ":")
    pprint.pprint(distances)

    end_distances["sort by y"] += distances["sort by y"]
    end_distances["sort by x"] += distances["sort by x"]
    end_distances["two opt swap"] += distances["two opt swap"]
    end_distances["three opt swap"] += distances["three opt swap"]
    end_distances["next nearest"] += distances["next nearest"]
    if sa_support:end_distances["sa"] += distances["sa"]
    if pye_support:end_distances["ga"] += distances["ga"]
=======
    coords = tsp_functions.generate_points(50,400)

    distances["sort by y"] = sort_by_Y.sort_by_y(coords)

    #visualize_tsp.plotTSP([distances["sort by y"][1]],coords,"y")

    distances["sort by x"] = sort_by_X.sort_by_x(coords)

    #visualize_tsp.plotTSP([distances["sort by x"][1]],coords,"x")

    distances["two opt swap"] = two_opt_swap.twoOptSwap(coords)

    #visualize_tsp.plotTSP([distances["two opt swap"][1]],coords,"2opt")

    distances["three opt swap"] = three_opt_swap.threeOptSwap(coords)

    #visualize_tsp.plotTSP([distances["three opt swap"][1]],coords,"2opt")

    distances["next nearest"] = next_nearest.greedy_algo(coords)

    #visualize_tsp.plotTSP([distances["next_nearest"][1]],coords,"2opt")

    distances["sa"] = anneal.SimAnneal(coords).Anneal()

    #distances["ga"] = Genetic_Algorithm.GA(coords)
    print("Trial " + str(i) + ":")
    pprint.pprint(distances)

    end_distances["sort by y"] += distances["sort by y"][0]
    end_distances["sort by x"] += distances["sort by x"][0]
    end_distances["two opt swap"] += distances["two opt swap"][0]
    end_distances["three opt swap"] += distances["three opt swap"][0]
    end_distances["next nearest"] += distances["next nearest"][0]
    end_distances["sa"] += distances["sa"][0]
    #end_distances["ga"] += distances["ga"][0]
>>>>>>> 607273b85d32ee900701a0e5de2ea6d6022c6749
for i in end_distances:
    end_distances[i] /= num_trials
print("The end averages are:")
pprint.pprint(end_distances)
