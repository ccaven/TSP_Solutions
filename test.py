import sort_by_x
import sort_by_y
import next_nearest
import brute_force
import tsp_functions
import Genetic_Algorithm
from simAnneal import anneal
from simAnneal import visualize_tsp
end_distances = {"sort by x":0,"sort by y":0,"next nearest":0,"brute force":0,"ga":0,"sa":0}
num_trials = 10
for i in range(num_trials):
    #Test comment
    distances = {"sort by x":0,"sort by y":0,"next nearest":0,"brute force":0,"ga":0,"sa":0}
    coords = tsp_functionsself.generate_points(200,400)
    distances["sort by y"] = sort_by_y.sort_by_y(coords)
    distances["sort by x"] = sort_by_x.sort_by_x(coords)
    distances["next nearest"] = next_nearest.greedy_algo(coords)
    distances["ga"] = Genetic_Algorithm.GA(coords)
    distances["sa"] = anneal.SimAnneal(coords).Anneal()
