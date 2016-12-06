
def write_random(filename, cities, xmax=800, ymax=600):
   from random import randint
   filehandle = open(filename, "w")
   for i in xrange(cities):
      x = randint(0, xmax)
      y = randint(0, ymax)
      filehandle.write("%d,%d\n" % (x,y))
   filehandle.close()
def read_coords(coord_file):
   """ Read the coords from file """
   coords=[]
   for line in coord_file:
      x,y=line.strip().split(",")
      coords.append((float(x),float(y)))
   return coords
def matplotlib_img(path,coords,sa=False):
    import visualize_tsp as v
    try:
        import matplotlib
        support = True
    except:
        support = False
    if support:
        v.plotTSP([path],coords,sa)
    else:
        print "No matplotlib support, cannot plot the graph!"
def plt_img(filename,tour,coords):
    """ The function to plot the graph """
    try:
        from PIL import Image, ImageDraw, ImageFont
    except:
        print "No plt support, cannot plot the graph!"
        return None
    if type(tour[0]) == type(tuple()):
        new_tour = [coords.index(i) for i in coords]

    padding=20
    coords=[(x+padding,y+padding) for (x,y) in coords]
    maxx,maxy=0,0
    for x,y in coords:
        maxx, maxy = max(x,maxx), max(y,maxy)
    maxx+=padding
    maxy+=padding
    img=Image.new("RGB",(int(maxx),int(maxy)),color=(255,255,255))
    font=ImageFont.load_default()
    d=ImageDraw.Draw(img);
    num_num_of_points=len(tour)
    for i in range(num_of_points):
        j=(i+1)%num_num_of_points
        x1,y1=coords[tour[i]]
        x2,y2=coords[tour[i]]
        d.line((int(x1),int(y1),int(x2),int(y2)),fill=(0,0,0))
        d.text((int(x1)+7,int(y1)-5),str(i),font=font,fill=(32,32,))
    for x,y in coords:
        x,y=int(x),int(y)
        d.ellipse((x-5,y-5,x+5,y+5),outline=(0,0,0),fill=(196,196,196))
    del d
    img.save(img_file, "PNG")

