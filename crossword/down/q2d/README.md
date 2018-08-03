
# 2d. "Flower power"

Anna is visiting a botanical garden and notices a row of N beautiful flowers
(*3 ≤ N ≤ 2000*). The colour of each of the flowers is `yellow`, `red` or
`blue`. Anna says that a subsequence of contiguous flowers is "super-colourful"
if both of the following conditions are satisfied:

  1. Each of the possible colours appears at least once in the subsequence
  2. No two colours appear the same number of times in the subsequence

For instance, the subsequence (red, red, blue) is not super-colourful as
`yellow` does not appear. Nor is (red, red, blue, yellow, yellow) as `red` and
`yellow` appear the same number of times. However,
(red, blue, red, red, yellow, yellow, red) is super-colourful.

Even if two flowers have the same colour, a careful observer will know that they
are still two different flowers. Two subsequences of contiguous flowers are said
to be "different" if they start or end at different flowers.

Write a function that takes as input a string S of length N. Each character of S
is `Y`, `R` or `B`. The i-th character of S describes the colour of the i-th
flower in the row: the characters `Y`, `R` and `B` denote yellow, red or blue
respectively. Your function should compute the number, C, of different
super-colourful subsequences of contiguous flowers there are in the entire row
of flowers, and return 10000 + C.

The answer into the crossword will be the output of your function for the
downloadable input file included with this question (in case you're curious).

----

Additional materials

  - [downloadable_input.txt (1 KB)](downloadable_input.txt)