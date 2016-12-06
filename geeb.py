import copy
import tsp_functions as fun
import visualize_tsp as pic
def single_path(path):
    pcopy = copy.copy(path)
    def mean(iterable):
        print iterable
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
    num_sect = 10
    maxx = max([i[0] for i in path])
    maxy = max([i[1] for i in path])
    xsize = maxx/num_sect
    ysize = maxy/num_sect
    sections = [[[] for j in range(num_sect)] for i in range(num_sect)]
    point_descriptions = {}
    # NOTE:  Gives each point a description
    for i in pcopy:
        print "i:**************************************************************************** :)"
        print i
        count = 0
        for x in range(num_sect):
            for y in range(num_sect):
                print (x,y)
                leftx = (x*xsize)
                bottomy = (y*ysize)
                print (leftx,bottomy)
                print (leftx+xsize,bottomy+ysize)
                if point_in_box(i,leftx,bottomy,xsize,ysize):
                    point_descriptions[i] = [(leftx,bottomy),(leftx+xsize,bottomy+ysize)]
                else:
                    count+=1
        if count==num_sect**2:
            print i
            print point_descriptions
            raise Exception
    # NOTE:  Sorts each point into a section
    for point in point_descriptions:
        index = pcopy.index(point)
        secti = point_descriptions[point]
        pointx = secti[0][0]
        pointy = secti[0][1]
        sectx = pointx//xsize
        secty = pointy//ysize
        print "                                           ))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))"
        print point
        print (pointx,pointy)
        print (sectx,secty)
        sections[sectx][secty].append(point)
    for i in path:
        if not i in point_descriptions:
            print i
            #raise Exception
    # NOTE:  Sort each section based on the MAD of the x and y
    for x in sections:
        print sections
        for y in x:
            xi = sections.index(x)
            yi = x.index(y)
            print y
            if MAD([point[0] for point in y]) > MAD([point[1] for point in y]):
                sections[xi][yi].sort(key=lambda p:p[1])
            else:
                sections[xi][yi].sort(key=lambda p:p[0])

    # NOTE: Make end path a combination of each section
    end_path = []
    for x in range(len(sections)):
        for y in range(x):
            sectx = x
            if sectx%2 == 1:
                reverse = True
            else:
                reverse = False
            if reverse:
                sections[x][y] = list(reversed(sections[x][y]))
                sections[x] = list(reversed(sections[x]))
            for point in sections[x][y]:
                end_path.append(point)
    for point in pcopy:
        if not point in end_path:
            print point
            #raise IndexError
    return (fun.path_distance(end_path),end_path)
p = fun.generate_points(2000,100)
t = single_path(p)
print t
pic.plotTSP([t[1]],p,"other")
