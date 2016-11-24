import tsp_functions
def sort_by_x(path):
        points = list(path)
        points.sort(key= lambda x:x[0]) # lambda sorting, so no need for operator.itemgetter
        return path_distance(points)
