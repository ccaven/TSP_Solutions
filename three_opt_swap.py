import tsp_functions as fun,copy
def threeOptSwap(path):
    orig_copy = copy.copy(path)
    test_copy = copy.copy(path)
    for coord in range(len(path)):
        otherpoints = []
        for i in range(len(orig_copy)):
            if orig_copy[i] != coord:
                otherpoints.append([orig_copy[i],i])
        #closest = sorted([[pythag_distance(path[coord],otherpoints[j][0]),otherpoints[j][1]] for j in range(len(otherpoints))])
        closest = []
        for j in range(len(otherpoints)):
            closest.append([fun.pythag_distance(path[coord],otherpoints[j][0]),otherpoints[j][1]])
        closest.sort()
        closest5 = closest[:5]
        # Go through the closest 5 and do the swapping procedure
        for i in range(len(closest5)):
            # Name all the nodes
            node1 = copy.copy(coord)
            node1_copy = orig_copy[node1]
            node2 = copy.copy(i)
            node2_copy = orig_copy[closest5[node2][1]]
            node3 = copy.copy(randint(-i,i))
            node3_copy = orig_copy[closest5[node3][1]]
            # Swap nodes
            solutions  = ["bca","cab","bac","acb","cba"]
            for i in solutions:
                if i == "acb":
                    test_copy[closest5[node2][1]] = copy.copy(node3_copy)
                    test_copy[closest5[node3][1]] = copy.copy(node2_copy)

                if i == "bac":
                    test_copy[node1] = copy.copy(node2_copy)
                    test_copy[closest5[node2][1]] = copy.copy(node1_copy)

                if i == "cba":
                    test_copy[node1] = copy.copy(node3_copy)
                    test_copy[closest5[node3][1]] = copy.copy(node1_copy)

                if i == "bca":
                    test_copy[node1] = copy.copy(node2_copy)
                    test_copy[closest5[node2][1]] = copy.copy(node3_copy)
                    test_copy[closest5[node3][1]] = copy.copy(node1_copy)
                if i == "cab":
                    test_copy[node1] = copy.copy(node3_copy)
                    test_copy[closest5[node2][1]] = copy.copy(node1_copy)
                    test_copy[closest5[node3][1]] = copy.copy(node2_copy)
                if fun.path_distance(test_copy) < fun.path_distance(orig_copy):
                    orig_copy = copy.copy(test_copy)
                else:
                    test_copy = copy.copy(orig_copy)
    return funs.path_distance(orig_copy)
