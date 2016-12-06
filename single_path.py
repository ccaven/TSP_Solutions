import copy
import tsp_functions as fun
import visualize_tsp as pic
def single_path(path):
    pcopy = copy.copy(path)
    def mean(iterable):
        return sum(iterable)/len(iterable)
    def MAD(iterable):
        m = mean(iterable)
        return mean([m-i for i in iterable])
    num_points = len(pcopy)
    num_sections = num_points/5
    minx = min([i[0] for i in path])
    maxx = max([i[0] for i in path])
    sectionsize = abs(maxx - minx)/5
    sections = [[] for i in range(num_sections)]
    # Sorts points into columns
    for i in pcopy:
        for group in range(num_sections):
            leftx = (group*sectionsize) + minx
            rightx = (group*sectionsize) + minx + sectionsize
            if i[0] > leftx and i[0] < rightx:
                sections[group].append(i)
    for j in range(len(sections)):
        sections[j].sort(key=lambda point:point[1])
    new_sections = [[[] for i in range(num_sections)] for j in range(num_sections)]
    '''
    for group in range(len(sections)):
        for point in range(len(sections[group])):
            for new_sect in range(len(new_sections[group])):
                p = sections[group][point]
                bottomy = (group*sectionsize) + minx
                topy = (group*sectionsize) + minx + sectionsize
                if p[0] > bottomy and p[0] < topy:
                    new_sections[group][new_sect].append(p)
    '''
    '''
    for group in range(len(new_sections)):
        for subgroup in range(len(new_sections[group])):
            pd = new_sections[group][subgroup]
            try:
                if MAD([i[0] for i in new_sections[group][subgroup]]) < MAD([i[1] for i in new_sections[group][subgroup]]):
                    new_sections[group][subgroup].sort(key=lambda p:p[0])
                else:
                    new_sections[group][subgroup].sort(key=lambda p:p[1])
            except Exception as e:
                print e
                pass
    '''
    end_path = []
    for group in sections:
        for point in group:
            end_path.append(point)
    return (fun.path_distance(end_path),end_path)
p = fun.generate_points(200,400)
t = single_path(p)
print t
pic.plotTSP([t[1]],p,"other")
