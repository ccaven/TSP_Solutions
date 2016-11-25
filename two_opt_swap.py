import tsp_functions
def twoOptSwap(path):
    orig_copy = copy.copy(path)
    test_copy = copy.copy(path)
    for coord in range(len(path)):
        otherpoints = []
        for i in range(len(orig_copy)):
            if orig_copy[i] != coord:
                otherpoints.append([orig_copy[i],i])
        closest = sorted([[pythag_distance(path[coord],otherpoints[j][0]),otherpoints[j][1]] for j in range(len(otherpoints))])
        closest5 = closest[:5]
        for i in range(len(closest5)):
            node1 = copy.copy(coord)
            node1_copy = orig_copy[node1]
            node2 = copy.copy(i)
            node2_copy = orig_copy[closest5[node2][1]]
            # Swap the nodes and see if it is shorter than the original one
            test_copy[node1] = copy.copy(node2_copy)
            test_copy[closest5[node2][1]] = copy.copy(node1_copy)
            # if it is shorter, set that one as the copy
            if path_distance(test_copy) < path_distance(orig_copy):
                orig_copy = copy.copy(test_copy)
            else:
                test_copy = copy.copy(orig_copy)
            # return end_path
    return tsp_functions.path_distance(orig_copy)
