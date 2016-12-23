import sort_by_X as sx
import sort_by_Y as sy
import next_nearest as nn
import brute_force as bf
import three_opt_swap as opt3
import two_opt_swap as opt2
import pprint
import tsp_functions as fun

try:
    import ga_test as ga
    import pyevolve
    pye_support = True
except:
    pye_support = False

try:
    import anneal as sa
    from visualize_tsp import plotTSP as pic
    sa_support = True
except:
    sa_support = False

import single_path as sp
import file_handler as op
import tsp_functions
end_distances = {"single path":0,"sort by x":0,"sort by y":0,"two opt swap":0,"three opt swap":0,"next nearest":0,"brute force":0,"ga":0,"sa":0}
num_trials = 10

# Runs each algorithm

for i in range(num_trials):

    #Test comment

    distances = {"three opt swap":0}

    coords = op.read_coords(open("trial%d" % i))

    distances["three opt swap"] = opt3.threeOptSwap(coords)

    end_distances["three opt swap"] += distances["three opt swap"]

    print str(i) + ":  " + str(distances["three opt swap"])

end_distances["three opt swap"] /= num_trials
print "end:  " + str(end_distances["three opt swap"])
'''
    distances["sort by y"] = sy.sort_by_y(coords)

    distances["sort by x"] = sx.sort_by_x(coords)

    distances["single path"] = sp.single_path(coords)[0]

    distances["two opt swap"] = opt2.twoOptSwap(coords)

    distances["three opt swap"] = opt3.threeOptSwap(coords)

    distances["next nearest"] = nn.greedy_algo(coords)[0]

    if sa_support:

        distances["sa"] = sa.SimAnneal(coords).Anneal()[0]

    else:

        print "no sa support, cannot run simulated annealing"

    try:

        distances["ga"] = ga.main_run(coords)

    except:

        print "no pyevolve support, cannot run ga"

    print("Trial " + str(i) + ":")
    pprint.pprint(distances)
    end_distances["single path"] += distances["single path"]
    end_distances["sort by y"] += distances["sort by y"]
    end_distances["sort by x"] += distances["sort by x"]
    end_distances["two opt swap"] += distances["two opt swap"]
    end_distances["three opt swap"] += distances["three opt swap"]
    end_distances["next nearest"] += distances["next nearest"]
    if sa_support:end_distances["sa"] += distances["sa"]
    if pye_support:end_distances["ga"] += distances["ga"]

for i in end_distances:
    end_distances[i] /= num_trials
print("The end averages are:")
pprint.pprint(end_distances)
'''
