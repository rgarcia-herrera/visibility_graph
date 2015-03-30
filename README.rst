Visibility Graph Algorithm
==========================

This python package is an implementation of the algorithm described in
the article: `From time series to complex networks: The visibility graph`__.

.. __: http://www.pnas.org/content/105/13/4972.full


Installation
------------

Install library, perhaps within a virtualenv::

    $ pip install visibility_graph



Application Programming Interface
---------------------------------

Pass series as a list, visibility_graph will return a `networkX`__
undirected graph. Nodes contain the magnitudes on their timepoints.::

 >>> from visibility_graph import visibility_graph
 >>> series = [0.87, 0.49, 0.36, 0.83, 0.87]
 >>> g = visibility_graph( series )
 >>> 
 >>> g.nodes()
 [0, 1, 2, 3, 4]
 >>> g.edges()
 [(0, 1), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
 >>> 
 >>> g.node[1]
 {'mag': 0.49}

.. __: http://networkx.github.io/



Series to edgelist
------------------

A command line script is provided::
    
 $ series2edgelist.py series.csv

where **series.csv** is a file containing one time point per line. One
can specify more than one series file::

 $ series2edgelist.py series1.csv series2.csv seriesN.csv

The script will also read a series from the standard input::

 $ cat series.csv | series2edgelist.py

Edgelist will be printed to the standard output. So it might be wise
to::
  
 $ cat series.csv | series2edgelist.py > series.edgelist

  
The gist
--------

"In this graph, every node corresponds, in the same order, to series data, and two nodes are connected if visibility exists between the corresponding data, that is to say, if there is a straight line that connects the series data, provided that this “visibility line” does not intersect any intermediate data height."

.. image:: http://www.pnas.org/content/105/13/4972/F1.medium.gif

"More formally, we can establish the following visibility criteria: two arbitrary data values (t a, y a) and (t b, y b) will have visibility, and consequently will become two connected nodes of the associated graph, if any other data (t c, y c) placed between them fulfills:"

.. image:: http://www.pnas.org/content/105/13/4972/embed/graphic-2.gif
