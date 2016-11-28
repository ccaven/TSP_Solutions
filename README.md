# TSP Solutions
6th grade science fair project - test multiple solutions for TSP
Algorithms so far:
* Sort by X
* Sort by Y
* Greedy Algorithm
* Two Opt Swap
* Three Opt Swap
* Simulated Annealing
* Genetic Algorithm

Uses pythagorean distance
```python
p1 = (10,21)
p2 = (-12,10)
dist = pow(pow(p1[0]-p2[0],2) + pow(p1[1] - p2[1],2),0.5)
```

Some algorithms use distance matrixes to find the distance of a path
```python
distMatrix = [[distance(i,j) for i in coords] for j in coords]
```

The solution for each algorithm can be plotted on a map using matplotlib. Here is an example of Simulated Annealng:

![Simulated Annealing Image](https://github.com/ccaven/TSP_Solutions/blob/master/pics/Simulated_Anneal_pic.png)

Here is an example of the Greedy Algorithm:

![Greedy Algorithm Image](https://github.com/ccaven/TSP_Solutions/blob/master/pics/next_nearest.png)

Sort By X:

![Sort by X Image](https://github.com/ccaven/TSP_Solutions/blob/master/pics/sort_by_x.png)

Sort By Y:

![Sort by Y Image](https://github.com/ccaven/TSP_Solutions/blob/master/pics/sort_by_y.png)

Two Opt Swap:

![Two Opt Swap Image](https://github.com/ccaven/TSP_Solutions/blob/master/pics/two_opt_swap.png)

Three Opt Swap:

![Three Opt Image](https://github.com/ccaven/TSP_Solutions/blob/master/pics/three_opt_swap.png)

Genetic Algorithm:

