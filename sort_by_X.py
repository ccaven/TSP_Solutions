import tsp_functions
def sort_by_x(path):
    points = list(path)
    points.sort(key= lambda x:x[0]) # lambda sorting, so no need for operator.itemgetter
<<<<<<< HEAD
    return tsp_functions.path_distance(points)
=======
    return (tsp_functions.path_distance(points),points)
>>>>>>> 4c038d8264d5a1a9deabfa97d5d1c875760078c1
