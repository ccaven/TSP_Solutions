import copy
def greedy_algo(coords):
    path = copy.copy(coords)
    end_path = []
    current_point = path[0]
    points_left = path[1:]
    for point in path:
        end_path.append(current_point)
        closest = sorted([[pythag_distance(current_point,otherpoint),otherpoint] for otherpoint in points_left])
        next_point = closest[0][1]
        del closest[0]
        points_left = list(closest)
        current_point = copy.copy(current_point)
    end_path.append(current_point)
    return end_path
