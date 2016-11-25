import copy
import tsp_functions as fun
def greedy_algo(coords):
    path = copy.copy(coords)
    end_path = []
    current_point = path[0]
    points_left = path[1:]
    for i in range(len(path)-1):
        end_path.append(current_point)
        closest = [[fun.pythag_distance(current_point,points_left[i]),points_left[i]] for i in range(len(points_left))]
        closest.sort()
        next_point = closest[0][1]
        del closest[0]
        points_left = [i[1] for i in closest]
        current_point = copy.copy(current_point)
    end_path.append(current_point)
    return end_path
