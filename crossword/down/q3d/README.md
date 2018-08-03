
# 3d. "Fearful symmetry"

A string is a palindrome if it reads the same backwards as forwards. For
instance, `cabac` and `beeb` are palindromes, but `abb` is not.

Given a string T, we define the "score" of T as the length of the longest
palindrome that can be constructed by using some of the characters of T. For
instance, the score of `T = 'abc'` is 1, corresponding to the possible
palindromes `a`, `b` or `c`. The score of `T = 'aacggg'` is 5, corresponding to
the palindrome `gacag`.

Write a function that takes as input a string S consisting of N characters
(`200 ≤ N ≤ 5000`), each from the set `{'a', 'b', 'c', 'd', 'e', 'f', 'g'}`.
Your function should split S into four non-overlapping pieces such that:

  - Each piece has non-zero length
  - Each piece consists of contiguous characters
  - The sum of the scores of each piece is minimised

Your function should return the minimum total score for S.

For instance, if `S = 'abccaa'` then the total minimum score is 4. Splitting S
into the four pieces 'abc', 'c', 'a', 'a' gives the total score
1 + 1 + 1 + 1 = 4. It is easy to see that it is not possible to obtain a lower
score. Observe that if the string was instead split as 'a', 'b', 'cc', 'aa' then
the total score would be 1 + 1 + 2 + 2 = 6.

The answer into the crossword will be the output of your function for the
downloadable input file included with this question (in case you're curious).

----

Additional materials

  - [downloadable_input.txt (1 KB)](downloadable_input.txt)