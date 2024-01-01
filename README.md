# Finding the optimal route for the problem of delivering parcels of a delivery company
This project models the problem of finding an optimal delivery route for multiple trucks at a delivery company using Intelligent Search Algorithms and State Space Search representation with effective abstraction methodologies.

**The goal is to deliver all parcels and return to the starting location at the lowest possible cost.**

## The problem specifics:
1- Each parcel has a pickup location and a destination location.

2- Each truck has at least one parcel at the beginning.

3- There are locations that have buildings and where trucks can't pass by.

4- It is allowed to pass by the same location more than one time.

5- The cost of moving from one location to another is 1 + the number of parcels that are being transferred in the moment.

## The allowed processes:
1- Moving East.

2- Moving West.

3- Moving Wouth.

4- Moving North.

5- Receiving a parcel.

6- Delivering a parcel.

## The used intelligent search algorithms:
- DFS
- BFS
- UCS
- A star with 3 differnet heuristic functions

## The used tools:
**Programming language:** Python
**Libraries:** termcolor, queue, time, copy
