def brute_force(path):
    points = list(path)
    import itertools

    def distance(p1, p2):
        return (((((p1[0]-p2[0])**2)
                +((p1[1]-p2[1])**2))**0.5)
                +(((p1[2]-p2[2])**2)))**0.5

    def calCosts(routes, nodes):
        travelCosts = []

        for route in routes:
            travelCost = 0

            #Sums up the travel cost
            for i in range(1,len(route)):
                #takes an element of route, uses it to find the corresponding coords and calculates the distance
                travelCost += distance(nodes[str(route[i-1])], nodes[str(route[i])])

            travelCosts.append(travelCost)

        #pulls out the smallest travel cost
        smallestCost = min(travelCosts)
        shortest = (routes[travelCosts.index(smallestCost)], smallestCost)

        #returns tuple of the route and its cost
        return shortest

    def genRoutes(routeLength):
        #lang hold all the 'alphabet' of nodes
        lang = [ x for x in range(2,routeLength+1) ]

        #uses built-in itertools to generate permutations
        routes = list(map(list, itertools.permutations(lang)))
        #inserts the home city, must be the first city in every route
        for x in routes:
            x.insert(0,1)
        return routes

    def main(nodes=None, instanceSize=5):
        #nodes and instanceSize are passed into main() using another program
        #I just gave them default values for this example

        #The Node lookup table.
        Nodes = {}
        for i in range(len(points)):
            x = points[i].x
            y = points[i].y
            z = points[i].z
            Nodes[str(i)] = (x,y,z)

        routes = genRoutes(instanceSize)
        shortest = calCosts(routes, Nodes)

        print("Shortest Route: ", shortest[0])
        print("Travel Cost: ", shortest[1])

    if __name__ == '__main__':
        main()
