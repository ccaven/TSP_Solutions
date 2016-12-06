import tsp_functions as fun
def clo_to_center(path):
    points = list(path)
    lst = [[fun.pythag_distance((0,0),i),i] for i in points]
    lst.sort(key=lambda l:l[0])
    end_path = [i[1] for i in lst]
    return [fun.path_distance(end_path),end_path]
def mean(iterable):
    return sum(iterable)/len(iterable)
def MAD(iterable):
    m = mean(iterable)
    try:
        return mean([m-i for i in iterable])
    except Exception as e:
        print iterable
        print m
        raise e
class single_path(object):
    def __init__(self, path):
        self.coords = list(path)
        self.end_path = []
        self.maxx = max([i[0] for i in self.coords])
        self.maxy = max([i[1] for i in self.coords])
        self.minx = min([i[0] for i in self.coords])
        self.miny = min([i[1] for i in self.coords])
        self.rangex = abs(self.maxx-self.minx)
        self.rangey = abs(self.maxy-self.miny)
        self.xsize = self.rangex/5
        self.ysize = self.rangey/5
        self.parameters = self.get_paras()
        self.sections = self.split_into_quads()
        return None
    def split_into_quads(self):
        point_descriptions = {}
        for i in self.coords:
<<<<<<< HEAD
            for para in self.parameters:
                if i[0] > para[0][0] and i[0] < para[1][0] and i[1] > para[0][1] and i[1] < para[1][1]:
                    point_descriptions[i] = para
        sections = [[[] for j in range(range_y)] for i in range(range_x)]
=======
            for column in self.parameters:
                for sect in column:
                    if i[0] > sect[0][0] and i[0] < sect[1][0] and i[1] > sect[0][1] and i[1] < sect[1][1]:
                        point_descriptions[i] = para
        sections = [[[] for j in range(self.rangey)] for i in range(self.rangex)]
        print point_descriptions
>>>>>>> 607273b85d32ee900701a0e5de2ea6d6022c6749
        for point in point_descriptions:
            secti = point_descriptions[i]
            sectx = secti[0][0]/xsize
            secty = secti[0][1]/ysize
            sections[sectx][secty].append(point)
        return sections
    def get_paras(self):
        p = []
        for i in range(5):
            p.append([])
            for j in range(5):
                leftx = (i*self.xsize)
                rightx = ((i+1)*self.xsize)
                topy = (j*self.ysize)
                bottomy = ((j+1)*self.ysize)
                p[i].append(((leftx,bottomy),(rightx,topy)))
        print p
        return p
    def sort_by_x(self,path):
        p = list(path)
        p.sort(key=lambda point:point[0])
        return p
    def sort_by_y(self,path):
        p = list(path)
        p.sort(key=lambda point:point[1])
        return p
    def combined(self):
        self.get_paras()
        self.split_into_quads()
        for group in self.sections:
<<<<<<< HEAD
            # do stuff
            pass
    def solve(self):
        return (fun.path_distance(self.coords),self.coords)
=======
            i = self.sections.index(group)
            print i
            print group
            if MAD([point[0] for point in group]) > MAD([point[1] for point in group]):
                self.sections[i] = self.sort_by_y(group)
            else:
                self.sections[i] = self.sort_by_x(group)
        return None
    def vecSectToList(self):
        self.combined()
        for i in range(len(self.sections)):
            sectx = i//5
            if sectx%2 == 1:
                reverse = True
            else:
                reverse = False
            if reverse:
                self.sections[i] = list(reversed(self.sections[i]))
        for group in self.sections:
            print group
            for point in group:
                print point
                self.end_path.append(point)
    def get_best(self):
        print self.end_path
        return (fun.path_distance(self.end_path),self.end_path)
    def main(self):
        self.vecSectToList()
        self.best = get_best()
points = fun.generate_points(25,50)
print clo_to_center(points)[0]
sp = single_path(points)
sp.main()
print sp.best
>>>>>>> 607273b85d32ee900701a0e5de2ea6d6022c6749
