import tsp_functions as fun
def clo_to_center(path):
    points = list(path)
    lst = [[fun.pythag_distance((0,0),i),i] for i in points]
    lst.sort(key=lambda l:l[0])
    end_path = [i[1] for i in lst]
    return [fun.path_distance(end_path),end_path]
class single_path(object):
    def __init__(self, path):
        self.coords = list(path)
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
            for para in self.parameters:
                if i[0] > para[0][0] and i[0] < para[1][0] and i[1] > para[0][1] and i[1] < para[1][1]:
                    point_descriptions[i] = para
        sections = [[[] for j in range(range_y))] for i in range(range_x)]
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
                topy = (i*self.ysize)
                bottomy = ((i+1)*self.ysize)
                p[i].append(((leftx,bottomy),(rightx,topy)))
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
        for group in self.sections:
            # do stuff
    def solve(self):
        return (fun.path_distance(self.coords),self.coords)
