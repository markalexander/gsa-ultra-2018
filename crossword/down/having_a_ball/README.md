
# 1d. "Having a ball"

You are given N labeled boxes and N (1 ≤ N ≤ 10^4) balls labeled 1 to N where
each box contains exactly one ball. The i-th box contains ball i.

You want to generate as many different configurations as possible by swapping
the balls present in the boxes. A swap consists of choosing two boxes, say x and
y, and putting the ball present in box x in box y and vice versa. One
configuration is considered different from another if at least one ball is in a
different box.

The list of possible swaps you can perform is represented by M pairs of integers
(x_i, y_i) where 1 ≤ M ≤ 10^5 and 1 ≤ x_i, y_i ≤ N denoting that you can make a
swap between boxes x and y if (x, y) or (y, x) is present in these M pairs. You
can apply a permitted swap as many times as you like.

Write a function that takes the following inputs:

  - An integer N, denoting the number of boxes and balls
  - A tuple of length M, consisting of tuples of length 2, listing the allowed
    swaps

and outputs the number of different configurations achievable. Since the answer
could be huge, output the answer modulo 10^9 + 7.

For example, the output of `solution(3, ((1, 2),))` would be 2, since the two
possible configurations are [1, 2, 3] and [2, 1, 3] (which can be formed by
swapping the balls in first two boxes in the initial configuration).

The answer into the crossword will be the output of your function for the
downloadable input file included with this question (in case you're curious).

----

Additional materials

  - [downloadable_input.txt (1 KB)](downloadable_input.txt)