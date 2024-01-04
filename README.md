# NPTEL
NPTEL PROGRAMMING ASSIGNMENT

Status: Passed(Elite+Silver Medal)
So, yes the codes are reliable and passed all test cases. Make sure the question is same before copy Pasting. Sample question for week 2 provided below.

Programming, Data Structures And Algorithms Using Python
ABOUT THE COURSE :
This course is an introduction to programming and problem solving in Python.  It does not assume any prior knowledge of programming.  Using some motivating examples, the course quickly builds up basic concepts such as conditionals, loops, functions, lists, strings and tuples.  It goes on to cover searching and sorting algorithms, dynamic programming and backtracking, as well as topics such as exception handling and using files.  As far as data structures are concerned, the course covers Python dictionaries as well as classes and objects for defining user defined datatypes such as linked lists and binary search trees.

INTENDED AUDIENCE: Students in any branch of mathematics/science/engineering, 1st year 

PREREQUISITES:          School level mathematics.

INDUSTRY SUPPORT:   This course should be of value to any company requiring programming skills.



```-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------



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
[0, 1, 3, 5]```

```Week 3 Programming Assignment
Due on 2023-08-17, 23:59 IST
Write three Python functions as specified below. Paste the text for all three functions together into the submission window. Your function will be called automatically with various inputs and should return values as specified. Do not write commands to read any input or print any output.
You may define additional auxiliary functions as needed.
In all cases you may assume that the value passed to the function is of the expected type, so your function does not have to check for malformed inputs.
For each function, there are normally some public test cases and some (hidden) private test cases.
"Compile and run" will evaluate your submission against the public test cases.
"Submit" will evaluate your submission against the hidden private test cases. There are 12 private test cases, with equal weightage. You will get feedback about which private test cases pass or fail, though you cannot see the actual test cases.
Ignore warnings about "Presentation errors".
Write a function expanding(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements strictly increases.

Here are some examples of how your function should work.

  >>> expanding([1,3,7,2,9])
  True
Explanation: Differences between adjacent elements are 3-1 = 2, 7-3 = 4, 7-2 = 5, 9-2 = 7.

  >>> expanding([1,3,7,2,-3]) 
  False
Explanation: Differences between adjacent elements are 3-1 = 2, 7-3 = 4, 7-2 = 5, 2-(-3) = 5, so not strictly increasing.

  >>> expanding([1,3,7,10])
  False
Explanation: Differences between adjacent elements are 3-1 = 2, 7-3 = 4, 10-7 = 3, so not increasing.

Write a Python function sumsquare(l) that takes a nonempty list of integers and returns a list [odd,even], where odd is the sum of squares all the odd numbers in l and even is the sum of squares of all the even numbers in l.

Here are some examples to show how your function should work.

>>> sumsquare([1,3,5])
[35, 0]

>>> sumsquare([2,4,6])
[0, 56]

>>> sumsquare([-1,-2,3,7])
[59, 4]
A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix

1  2  3  4
5  6  7  8
would be represented as [[1, 2, 3, 4], [5, 6, 7, 8]].

The transpose of a matrix converts each row into a column. The transpose of the matrix above is:

1  5
2  6
3  7
4  8
which would be represented as [[1, 5], [2, 6], [3, 7], [4, 8]].

Write a Python function transpose(m) that takes as input a two dimensional matrix m and returns the transpose of m. The argument m should remain undisturbed by the function.

Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix.

>>> transpose([[1,2,3],[4,5,6]])
[[1, 4], [2, 5], [3, 6]]

>>> transpose([[1],[2],[3]])
[[1, 2, 3]]

>>> transpose([[3]])
[[3]]

Private Test cases used for evaluation	Input	Expected Output	Actual Output	Status
Test Case 1	
expanding([11,35,77,21,98])
 True
True\n
Passed
Test Case 2	
expanding([11,38,79,25,-36])
 True
True\n
Passed
Test Case 3	
expanding([-1,2,-3,4,-5,6,-7,8,-9,10,-11,12])
 True
True\n
Passed
Test Case 4	
expanding([-1,2,-3,4,-5,6,-7,8,-9,10,-11,-32])
 False
False\n
Passed
Test Case 5	
sumsquare([1,-2,-3,4,5,6])
 [35, 56]
[35, 56]\n
Passed
Test Case 6	
sumsquare([1,3,5,7,9,11,13])
 [455, 0]
[455, 0]\n
Passed
Test Case 7	
sumsquare([0,2,4,6,8,10,12])
 [0, 364]
[0, 364]\n
Passed
Test Case 8	
sumsquare([0,1,-1,0,2,-2,3,-3])
 [20, 8]
[20, 8]\n
Passed
Test Case 9	
transpose([[1,2,3],[4,5,6],[7,8,9]])
 [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]\n
Passed
Test Case 10	
transpose([[1,2,3,4]])
 [[1], [2], [3], [4]]
[[1], [2], [3], [4]]\n
Passed
Test Case 11	
transpose([[1],[2],[3],[4]])
 [[1, 2, 3, 4]]
[[1, 2, 3, 4]]\n
Passed
Test Case 12	
transpose([[1,0,0],[0,1,0],[0,0,1]])
 [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]\n
Passed

The due date for submitting this assignment has passed.
12 out of 12 tests passed.
You scored 100.0/100.```
