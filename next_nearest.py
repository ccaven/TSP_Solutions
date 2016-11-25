import copy
import tsp_functions as fun
def greedy_algo(coords):
    cur_node = random.choice(coords)
    solution = [cur_node]

    free_list = copy.copy(coords)
    free_list.remove(cur_node)

    dist_matrix = fun.dist_matrix(coords)
    while free_list:
        closest_dist = min([dist_matrix[cur_node][j] for j in free_list])
        cur_node = dist_matrix[cur_node].index(closest_dist)
        free_list.remove(cur_node)
        solution.append(cur_node)
    return fun.path_distance(solution)
