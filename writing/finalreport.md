# Final Project Report

## Date: 07 Dec 2018
## Group Names: Nicholas Tocci, Rowan Castellanos, Ben Watto, Dillon Thoma

<!-- Your final report should highlight the key contributions of your work and consist of at least six high quality paragraphs with a minimum of 200 words in each. The report should include a description of why the chosen topic is important and discuss the implementation that you undertook. -->

## Motivation for the project
Our motivation for this project was to build off the graph theory section of our course and focus on the Traveling Salesman Problem, which is a classic graph theory problem regarding optimization. This asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?" This problem has applications in theoretical math, especially graph theory. It also has many applications in theoretical computer science, especially when programmers are thinking about efficient algorithm design. For this project we adapted the traveling salesman problem to find shortest paths between buildings on campus, rather than cities on a map. We took campus locations such as academic buildings, residential halls, the Campus Center, and the gym then we implemented an algorithm to calculate the shortest possible routes between them. The output is a shortest path around Allegheny’s campus that visits each academic building in which a particular student has class starting from their residential hall or some other specified campus location.

Why is the application you chose important/useful?

## Detailed description
We began by constructing a graph of the campus. Each building on campus was a vertex v on a graph G. Then we connected the vertices on G by adding edges to connect the buildings. These connections were the paths or sidewalks connecting the buildings. These edges on G connecting the vertices represent all the ways in which a student can get to class or otherwise travel around campus. This is the first graph we developed from the campus map. We started with it being very close to the actual map, trying to mimic sidewalks closely, but this lead to a cluttered graph with excess points. We redrafted our graph to remove these excess vertices. We then assigned weights to each edge. Weights were determined depending on how long each path takes to walk. For example, if it takes thirty seconds to walk the path from the Campus Center to Alden Hall, the edge connecting those pairs of vertices was .5 on the graph. We made each path bidirectional since you can walk back and forth. This means that for each edge, we actually had two weights. If you are walking from the Campus Center to the Library there will be one weight, but a separate one for walking from the Library to the Campus Center. In this example the second weight would be higher because it is uphill from the Library to the CC so it will take longer to walk.


Next we began our shortest path algorithm. We used Djikstra’s Algorithm to calculate the shortest path. NetworkX has a nice implementation of this which we were able to use in our code. Using our algorithm, we can then produce an optimized route for students to take to class.

We use a repl to guide users through the program. Users input where they are starting off at and where they would like to end up. They can ask for all paths or the shortest path.

Detailed description of the work you completed for this project. Without giving a snapshot of the code you wrote, provide technical description of what you implemented and how you implemented it. In particular include software requirements and software design for your project.

## UML diagrams or a flowchart showing your project’s software design
How classes are interacting with each other. To see an example of including an image in the Markdown document, please see “Mastering Markdown” GitHub guide found at https://guides.github.com/features/mastering-markdown/.

<!-- TODO: draw.io -->

## Description of your results.
The main final output of our program is the most efficient way for a student to get to class (or some other specified destination).

Make graphs, tables, snapshots of your output, or anything else that can help me understand your results.

## Teamwork
If you worked in a team, you should also include a paragraph that describes the team work and the contribution of each team member

## Conclusion
Give a short overview of your project and its results. Describe what you learned, what were the biggest challenges and the biggest rewards.
