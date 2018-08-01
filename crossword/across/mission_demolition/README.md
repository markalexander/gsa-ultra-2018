
# 12a. "Mission: Demolition"

You are tasked with demolishing a building and decide to model the distribution
of your explosives one-dimensionally as points on a line. The `N` explosives
(`1 ≤ N ≤ 200`) are described by two tuples `X` and `R`. For each explosive `i`,
integer `X_i`​ (`0 ≤ X_i ≤ 10000`) is the `x`-coordinate of the explosive and
integer `R_i` (`1 ≤ R_i ≤ 10000`) is its explosive strength.

Once an explosive is detonated it explodes. Explosive i can be detonated in one
of two ways:

  1. By using a detonator on explosive `i`
  2. By the explosion of explosive `j` such that
     `(X_j - R_j) ≤ X_i ≤ (X_j + R_j)`

You will only successfully demolish the building if you detonate all the
explosives that have been laid. For the sake of efficiency, you want to find out
the minimum number of detonators that must be used in order to detonate all of
the explosives.

For instance, if `N = 4`, `X = (2, 6, 7, 10)` and `R = (1, 3, 2, 5)` then it
suffices to detonate the first and the fourth explosive. Note that detonating
the fourth explosive would further trigger the detonation of the second and the
third.

Write a function that takes as input the integer `N`, the tuple `X` and the
tuple `R`.  Your function should calculate the minimum number, `D`, of
detonators that must be used in order to detonate all the explosives and return
`D × 10000`.

You may assume that `R` and `X` will both be of length `N` and that no two
elements of `X` will have the same value.

The answer into the crossword will be the output of your function for the
downloadable input file included with this question (in case you're curious).

----

Additional materials

  - [downloadable_input.txt (1 KB)](downloadable_input.txt)