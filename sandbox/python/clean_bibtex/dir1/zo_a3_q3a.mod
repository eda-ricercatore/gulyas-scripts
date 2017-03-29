# This is written by Zhiyang Ong, for Homework #3 of
# Discrete Optimization at National Taiwan University, Fall 2013.

# Question 3a)

/*	Decision variables */
var x1 >= 0;
var x2 >= 0;


/*	Objective function	*/
maximize z: -x1 + x2;

/*	Constraints	*/
s.t. c1 : x1 - x2 <= 2;
s.t. c2 : x1 + x2 <= 6;
/*
s.t. x1 >= 0;
s.t. x2 >= 3;
*/

end;