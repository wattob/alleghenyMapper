# Final Project Proposal

## Date: 07 Nov 2018
## Group Names: Nicholas Tocci, Rowan Castellanos, Ben Watto, Dillon Thoma

  The Traveling Salesman Problem is an old optimization question asking: "Given
a list of cities and the distances between each pair of cities, what is the
shortest possible route that visits each city and returns to the origin city?"
(In Pursuit of the Traveling Salesman: Mathematics at the Limits of Computation
by William J. Cook) This problem has applications in theoretical math,
especially graph theory. It also has many applications in theoretical computer
science, especially when programmers are thinking about efficient algorithm
design. We will be adapting the traveling salesman problem to find shortest
paths between buildings on campus, rather than cities on a map. Using the
classic optimization problem, we will be taking campus locations – such as
academic buildings, residential halls, the Campus Center, gym, etcetera – and
will calculate the shortest possible routes between them. The output will be a
shortest path around Allegheny’s campus that visit each academic building in
which a particular student has class starting from their residential hall or
some other specified campus location.

  This project will be expanding upon our course’s section on Graph Theory
during which we learned the basics of constructing a graph, traveling around
them through walks and paths, and some other basics of the subject. We will be
constructing our graph by imaging each building on campus as a vertex on a graph
G. Then we will connect the graph by adding in each path or sidewalk that
connects the buildings. These connections will each be an edge connecting the
vertices on G and will represent all the ways in which a student can get to
class or otherwise travel around campus. We will then assign weights to each
edge. Weights will be determined depending on how long each path takes to walk.
For example, if it takes one minuet to walk the path from the Campus Center to
Alden hall, the edge connecting those pairs of vertices will be a 1 on the graph.
Using our algorithm, we can then produce an optimized rout for students to take
to class.

  We will be complicating the algorithm by considering time windows. Time
windows are used to advance the traveling salesman problem in order to take into
account time restrictions. The “minimum-cost path of visiting each of a set of
cities exactly once, where each city must be visited within a specified time
window” is explored (Solving the Traveling Salesman Problem with Time Windows
Through Dynamically Generated Time-Expanded Networks by Natashia Boland, Mike
Hewitt, Duc Minh, and VuMartin Savelsbergh). This will be useful in our project
as students have a limited amount of time to travel around campus if they want
to get to class on time. For our implementation we will use either Kruskall’s
Algorithm or Djikstra’s Algorithm for the path finding. Our program will load a
mapping that the user provides from a text file, that way they do not add
several pairings each time they wish to run the system. A REPL will be used in
order to give the user a choice to change the default mapping to a different
file or use the current one. Users will then be prompted for multiple choices –
fastest path from a certain place, all routs, etcetera.
