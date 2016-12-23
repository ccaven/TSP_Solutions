import copy,random
import tsp_functions as fun
def greedy_algo(coords):
    cur_node = random.choice(coords)
    solution = [cur_node]

    free_list = copy.copy(coords)
    free_list.remove(cur_node)

    dist_matrix = fun.dist_matrix(coords)
    while free_list:
        closest_dist = [[fun.pythag_distance(cur_node,j),j] for j in free_list]
        closest_dist.sort()
        try:
            cur_node = closest_dist[0][1]
        except:
            print cur_node
            raise Exception
        free_list.remove(cur_node)
        solution.append(cur_node)
    return [fun.path_distance(solution),solution]
