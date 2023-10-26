# NPTEL
NPTEL PROGRAMMING ASSIGNMENTS
Programming, Data Structures And Algorithms Using Python
ABOUT THE COURSE :
This course is an introduction to programming and problem solving in Python.  It does not assume any prior knowledge of programming.  Using some motivating examples, the course quickly builds up basic concepts such as conditionals, loops, functions, lists, strings and tuples.  It goes on to cover searching and sorting algorithms, dynamic programming and backtracking, as well as topics such as exception handling and using files.  As far as data structures are concerned, the course covers Python dictionaries as well as classes and objects for defining user defined datatypes such as linked lists and binary search trees.

INTENDED AUDIENCE: Students in any branch of mathematics/science/engineering, 1st year 

PREREQUISITES:          School level mathematics.

INDUSTRY SUPPORT:   This course should be of value to any company requiring programming skills.



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------



check if the questions are same:
Week2 Question
A positive integer m is a prime product if it can be written as p×q, where p and q are both primes. .

Write a Python function primeproduct(m) that takes an integer m as input and returns True if m is a prime product and False otherwise. (If m is not positive, your function should return False.)

Here are some examples of how your function should work.

>>> primeproduct(6)
True

>>> primeproduct(188)
False

>>> primeproduct(202)
True
Write a function delchar(s,c) that takes as input strings s and c, where c has length 1 (i.e., a single character), and returns the string obtained by deleting all occurrences of c in s. If c has length other than 1, the function should return s

Here are some examples to show how your function should work.

 
>>> delchar("banana","b")
'anana'

>>> delchar("banana","a")
'bnn'

>>> delchar("banana","n")
'baaa'

>>> delchar("banana","an")
'banana'
Write a function shuffle(l1,l2) that takes as input two lists, 11 and l2, and returns a list consisting of the first element in l1, then the first element in l2, then the second element in l1, then the second element in l2, and so on. If the two lists are not of equal length, the remaining elements of the longer list are appended at the end of the shuffled output.

Here are some examples to show how your function should work.

>>> shuffle([0,2,4],[1,3,5])
[0, 1, 2, 3, 4, 5]

>>> shuffle([0,2,4],[1])
[0, 1, 2, 4]

>>> shuffle([0],[1,3,5])
[0, 1, 3, 5]


