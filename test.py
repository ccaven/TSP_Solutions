import sort_by_X
import sort_by_Y
import next_nearest
import brute_force
import three_opt_swap
import two_opt_swap
import pprint
import tsp_functions
#import Genetic_Algorithm
import anneal
import visualize_tsp
end_distances = {"sort by x":0,"sort by y":0,"two opt swap":0,"three opt swap":0,"next nearest":0,"brute force":0,"ga":0,"sa":0}
num_trials = 1
for i in range(num_trials):

    #Test comment

    distances = {"sort by x":0,"sort by y":0,"next nearest":0,"two opt swap":0,"three opt swap":0,"brute force":0,"ga":0,"sa":0}

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
for i in end_distances:
    end_distances[i] /= num_trials
print("The end averages are:")
pprint.pprint(end_distances)
