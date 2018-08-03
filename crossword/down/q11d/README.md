
# 11d. "Squared away"

John loves mathematics. Yesterday in school he learnt about square integers, and
now he can't stop thinking about them. As a reminder, integer n is "square" if
there exists some integer x such that `n = x × x`. At some point, John realises
that some integers could be described as "almost-square". An integer is
almost-square if it is square after one digit is removed.

For instance, `1231` is an almost-square integer, as removing the digit `3`
results in `121` and `121` is square (`121 = 11 × 11`). Observe that `20` and
`200` are almost-square integers as well, as removing `2` from them gives `0`
(`0 = 0 × 0`). However, `1254` is not almost-square as none of `254`, `154`,
`124` or `125` is square.

Write a function that takes a single integer input `A` (`500 ≤ A ≤ 10000`) and
returns the number of almost-square integers `S` in the range `10 ≤ S ≤ A`.

The entry into the crossword will be the return value of your function when it
is called automatically with input `1234`.
