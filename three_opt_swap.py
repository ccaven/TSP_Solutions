import tsp_functions as fun,copy
from random import randint
from random import choice
import next_nearest
def threeOptSwap(path):
    initial_solution = next_nearest.greedy_algo(path)[1]
    orig_copy = copy.copy(initial_solution)
    test_copy = copy.copy(initial_solution)
    for coord in orig_copy:
        #Other points, not including the current point
        otherpoints = [j for j in orig_copy]
        otherpoints.remove(coord)

        #Closest 5 points
        closest = [[fun.pythag_distance(coord,j),j] for j in otherpoints]
        closest.sort(key= lambda s:s[0])
        closest5_duel = closest[0:5]
        closest5 = [k[1] for k in closest5_duel]

        for j in closest5:
            # Set nodes
            swap_p = coord
            bswap_p = coord
            new_p = j
            bnew_p = j
            new2_p = choice(closest5)
            bnew2_p = choice(closest5)

            # Swapping procedure
            solutions = ["132","213","231","312","321"]
            for i in solutions:
                nodes = list(i)
                real_nodes = {"1":swap_p,"2":new_p,"3":new2_p}
                path_i = {"1":test_copy.index(swap_p),"2":test_copy.index(new_p),"3":test_copy.index(new2_p)}
                for i in nodes:
                    test_copy[path_i[i]] = real_nodes[i]
                if fun.path_distance(test_copy) < fun.path_distance(orig_copy):
                        orig_copy = copy.copy(test_copy)
                else:
                        test_copy = copy.copy(orig_copy)
    return fun.path_distance(orig_copy)
