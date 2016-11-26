import tsp_functions as fun,copy
import next_nearest
def twoOptSwap(path):
    initial_solution = next_nearest.greedy_algo(path)[1]
    orig_copy = copy.copy(initial_solution)
    test_copy = copy.copy(initial_solution)
    for i in orig_copy:
        #Other points, not including the current point
        otherpoints = [j for j in orig_copy]
        otherpoints.remove(i)

        #Closest 5 points
        closest = [[fun.pythag_distance(i,j),j] for j in otherpoints]
        closest.sort(key= lambda s:s[0])
        closest5 = closest[0:5]

        for j in closest5:
            # Set nodes
            swap_p = i
            bswap_p = i

            new_p = j
            bnew_p = j

            # Swap procedure
            test_copy[test_copy.index(swap_p)] = bnew_p
            test_copy[test_copy.index(new_p)] = bswap_p

            #If the swap is optimal, keep it
            if fun.path_distance(test_copy) < fun.path_distance(orig_copy):
                orig_copy = copy.copy(test_copy)

            #If it is not, dont keep it
            else:
                test_copy = copy.copy(orig_copy)

    return fun.path_distance(orig_copy)
