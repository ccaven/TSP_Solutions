# TSP Solutions
6th grade science fair project - test multiple solutions for TSP
Algorithms so far:
* Sort by X
* Sort by Y
* Greedy Algorithm
* Two Opt Swap
* Three Opt Swap
* Simmulated Annealing
* Genetic Algorithm

Uses pythagorean distance
```
p1 = (10,21)
p2 = (-12,10)
dist = pow(pow(p1[0]-p2[0],2) + pow(p1[1] - p2[1],2),0.5)
```

Some algorithms use distance matrixes to find the distance of a path
```
distMatrix = [[distance(i,j) for i in coords] for j in coords]
```

The solution for each algorithm can be plotted on a map using matplotlib
