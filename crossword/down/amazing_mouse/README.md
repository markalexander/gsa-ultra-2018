
# 9d. "Truly a-mazing mouse"

You have made a maze for your beloved pet mouse. The maze is divided into N×N
squares of unit size, arranged into N rows and N columns. One of the squares
contains your mouse's goal: a piece of cheese. Each of the squares is of one of
the following types:

  - `S` - start: The initial position of the mouse. This square can be freely
    visited even after the mouse leaves it. There is exactly one square of this
    type.
  - `.` - pathway: The mouse can freely visit this square.
  - `W` - wall: The mouse cannot visit this square.
  - `R` - red key: The mouse can freely visit the square. When it does so, it
    picks up a red key.
  - `G` - green key: The mouse can freely visit the square. When it does so, it
    picks up a green key.
  - `B` - blue key: The mouse can freely visit the square. When it does so, it
    picks up a blue key.
  - `C` - cheese: The position of the cheese. The mouse can freely visit this
    square at any time, but it can collect the cheese only if it has a red key,
    a green key and a blue key. There is exactly one square of this type.

The mouse starts without any keys. Let the tuple (i, j) denote the square at row
i and column j. The mouse can move from one square to another only if those two
squares share a side, and if all the conditions specific to the destination
square (as listed above) are satisfied. The mouse completes the maze when it
picks up the cheese.

More formally, if the mouse is at square (i, j), it can move to some of the
following squares under the conditions provided above and for the squares which
are within the maze: (i-1,j), (i+1,j), (i,j-1), (i,j+1). The maze is surrounded
by a high wall so that if the mouse is at a corner of the maze, it cannot leave
it. Furthermore, the mouse needs exactly one second to move from square to
square. The mouse starts from the start square S at time 0. The mouse moves
optimally through the maze.

Write a function that takes two parameters as input: an integer N (3 ≤ N ≤ 100),
which specifies number of rows and of column in the maze, and a tuple M.

M is a tuple containing N strings, where the i-th string in M represents the
i-th row of the maze. Each string consists of N characters, with the j-th
character of the string representing the square in the j-th column of the
corresponding row. Each character of each string will be from the set
`{'S', '.', 'W', 'R', 'G', 'B', 'C'}`, denoting a square type as described
above. It will always be possible for the mouse to complete the maze
successfully.

Given this representation of the maze, your function should return the minimum
time in milliseconds the mouse needs to complete the maze.

The answer into the crossword will be the output of your function for the
downloadable input file included with this question (in case you're curious).

----

Additional materials

  - [downloadable_input.txt (1 KB)](downloadable_input.txt)