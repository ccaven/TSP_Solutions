import tsp_functions
def sort_by_y(path):
        points = list(path)
        points.sort(key= lambda y:y[1])
        return path_distance(points)
