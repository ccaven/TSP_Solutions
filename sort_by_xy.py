import tsp_functions as fun
class Rule(object):
    def __init__(self, rangex, rangey):
        self.status = False
        self.maxx = rangex[1]
        self.maxy = rangey[1]
        self.minx = rangex[0]
        self.miny = rangey[0]

    def P_overlap(self,newp):
        if newp[0]<=self.maxx and newp[0]>=self.minx:
            x = True
        else:
            x = False
        if newp[1]<self.maxy and newp[1]>self.miny:
            y = True
        else:
            y = False
        if x and y:
            return True
        else:
            return False
    def get_paras(self):
        return ((self.maxx,self.maxy),(self.minx,self.miny))
def single_path(path):
    num_sect = int(len(path)/10)
    maxx = max([i[0] for i in path])
    maxy = max([i[1] for i in path])
    xsize = (maxx*2)/num_sect
    ysize = (maxy*2)/num_sect
    def mean(iterable):
        return sum(iterable)/len(iterable)
    def MAD(iterable):
        m = mean(iterable)
        return mean([m-i for i in iterable])
    sect = list()
    section_rules = dict()

    for i in range(num_sect):
        section_rules[str(i)] = {}
        for j in range(num_sect):
            print (i,j)
            print (xsize,ysize)
            section_rules[str(i)][str(j)] = Rule(((i-maxx)*xsize,(i+1)*xsize),((i-maxy)*ysize,(i+1)*ysize))
            print section_rules[str(i)][str(j)].get_paras()
    for i in section_rules:
        for j in i:
            e = section_rules[i][j]
            print (e.maxx,e.minx)
            print (e.maxy,e.miny)
    # NOTE: sorts points into groups
    for x in range(num_sect):
        for y in range(num_sect):
            sect.append([])
            for i in path:
                if section_rules[str(x)][str(y)].P_overlap(i):
                    sect[x].append(i)
    print sect
    # NOTE: This makes sure all points are included
    for p in path:
        included = []
        print sect
        for i in sect:
            print "i: "+str(i)
            for j in i:
                included.append(j)
        if not p in included:
            print p
            print included
            raise IndexError
    # NOTE: This sorts each group based on the x value of the points
    for i in range(len(sect)):
        if MAD([j[1] for j in i]) > MAD([j[0] for j in i]):
            sect[i].sort(key=lambda x:x[0])
        else:
            sect[i].sort(key=lambda x:x[1])
    end_path = []
    for i in sect:
        for j in i:
            end_path.append(j)
    return (fun.path_distance(end_path),end_path)
print single_path(fun.generate_points(25,50))
