import copy
import tsp_functions as fun
import visualize_tsp as pic
def single_path(path):
    pcopy = copy.copy(path)
    def mean(iterable):
        if len(iterable) != 0:
            return sum(iterable)/len(iterable)
        else:
            return 0
    def MAD(iterable):
        m = mean(iterable)
        return mean([m-i for i in iterable])
    '''
    This function calculates if a point is in a section
    (boxx,boxy) == corner towards orgin
    '''
    def point_in_box(point,boxx,boxy,boxw,boxh):
        if point[0] > boxx and point[0] < boxx+boxw and point[1] > boxy and point[1] < boxy + boxh:
            return True
        else:
            return False
    num_points = len(pcopy)
    num_sect = 4
    maxx = max([i[0] for i in path])
    maxy = max([i[1] for i in path])
    xsize = maxx/num_sect
    ysize = maxy/num_sect
    sections = [[] for j in range(num_sect)]

    # NOTE:  Gives each point a section
    for i in pcopy:
        print i
        if i[0]<maxx/2 and i[1]<maxy/2:
            sections[0].append(i)
        elif i[0]>=maxx/2 and i[1]<maxy/2:
            sections[1].append(i)
        elif i[0]<maxx/2 and i[0]>=maxy/2:
            sections[2].append(i)
        else:
            sections[3].append(i)
        print sections
    # NOTE:  Sort each section based on the MAD of the x and y
    for x in range(len(sections)):
        if MAD([point[0] for point in sections[x]]) > MAD([point[1] for point in sections[x]]):
            sections[x].sort(key=lambda p:p[1])
        else:
            sections[x].sort(key=lambda p:p[0])

    # NOTE: Make end path a combination of each section
    end_path = []
    for i in sections:
        for p in i:
            end_path.append(i)
    print end_path
    print point_in_box((0,0),-10,-10,20,20)
    return (fun.path_distance(end_path),end_path)

p = fun.generate_points(2000,100)
t = single_path(p)
pic.plotTSP([t[1]],p,"other")
