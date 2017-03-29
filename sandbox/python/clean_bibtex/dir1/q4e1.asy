// This is written by Zhiyang Ong
// For "Discrete Optimization" Homework #4, Question 3)

// Size of the figure
size(8cm,0,false);

// Importing packages from the Aysymptote Library
import graph;
import geometry;



// Set the limits of the x- and y- axis
xlimits(-1, 11);
ylimits(-1, 11);

// Radius of small circles indicating nodes along an edge, or in a graph
real R=0.2;

// Draw graph on slide 37 of Lecture 5
point a=(0,5);
circle ac=circle(a, R);
draw(ac, blue);
label("a",(0,4.5));

point b=(3,8);
circle bc=circle(b, R);
draw(bc, blue);
label("b",(3,7.5));

point c=(3,2);
circle cc=circle(c, R);
draw(cc, blue);
label("c",(3,1.5));

point d=(8,8);
circle dc=circle(d, R);
draw(dc, blue);
label("d",(8,7.5));

point e=(8,2);
circle ec=circle(e, R);
draw(ec, blue);
label("e",(8,1.5));

// Draw the graph
draw(a--b,red);


// Label the edges
label("2",(1.5,6.5));
























