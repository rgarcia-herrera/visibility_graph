# The Visibility Graph

This article: [From time series to complex networks: The visibility graph](http://www.pnas.org/content/105/13/4972.full)

We shall write an implementation of that algorithm.

## The gist

"In this graph, every node corresponds, in the same order, to series data, and two nodes are connected if visibility exists between the corresponding data, that is to say, if there is a straight line that connects the series data, provided that this “visibility line” does not intersect any intermediate data height."

<img src="http://www.pnas.org/content/105/13/4972/F1.medium.gif">

"More formally, we can establish the following visibility criteria: two arbitrary data values (t a, y a) and (t b, y b) will have visibility, and consequently will become two connected nodes of the associated graph, if any other data (t c, y c) placed between them fulfills:

<img src="http://www.pnas.org/content/105/13/4972/embed/graphic-2.gif">"
