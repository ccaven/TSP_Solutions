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

![Simulated Annealing Image](https://github.com/ccaven/TSP_Solutions/blob/master/Simulated_Anneal_pic.png)

Here is an example of the Greedy Algorithm:

![Simulated Annealing Image](https://github.com/ccaven/TSP_Solutions/blob/master/next_nearest.png)

Sort By X:

![Simulated Annealing Image](https://github.com/ccaven/TSP_Solutions/blob/master/sort_by_x.png)

Sort By Y:

![Simulated Annealing Image](https://github.com/ccaven/TSP_Solutions/blob/master/sort_by_y.png)

Two Opt Swap:

![Simulated Annealing Image](https://github.com/ccaven/TSP_Solutions/blob/master/two_opt_swap.png)

Three Opt Swap:

![Simulated Annealing Image](https://github.com/ccaven/TSP_Solutions/blob/master/three_opt_swap.png)

Genetic Algorithm:

