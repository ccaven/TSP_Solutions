import tsp_functions
def sort_by_x(path):
    points = list(path)
    points.sort(key= lambda x:x[0]) # lambda sorting, so no need for operator.itemgetter
    return (tsp_functions.path_distance(points),points)
<<<<<<< HEAD

=======
>>>>>>> 607273b85d32ee900701a0e5de2ea6d6022c6749
