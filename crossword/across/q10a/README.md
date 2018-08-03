
# 10a. "Horse-chestnutting around" 

Alice and Bob like playing games together. One day, they collect `N` chestnuts
on a pile (`5 ≤ N ≤ 20000`) and come up with the following game:

  - Alice and Bob randomly pick integers `A`, `B`, `X`, `Y`
    (`2 ≤ A, B, X, Y ≤ 1000`, not necessarily distinct)
    
  - Alice and Bob take turns to play the game, and Alice plays first
    
  - The player loses if the pile is empty at the start of their turn or if they
    are unable to make a valid move
    
  - In each turn, the player must take 1, 2 or 3 chestnuts from the pile as
    follows:
    
      - They can take 1, 2 or 3 chestnuts if it would leave the pile empty
      
      - If they are to leave a non-empty pile of chestnuts after their turn,
        they can only make a move that obeys the following restrictions:
        
          - If it is Alice's turn, the number of chestnuts she leaves on the
            pile must not be divisible by A or B
            
          - If it is Bob's turn, the number of chestnuts he leaves on the pile
            must not be divisible by X or Y

For instance, if N=7, A=5, B=6, X=4, Y=3, the game could proceed as follows:

  - Alice plays first and collects 3 chestnuts, leaving 4 on the pile
  
  - Bob takes 2 chestnuts, leaving 2 on the pile
  
  - Alice takes the last 2 chestnuts from the pile
  
  - The pile is empty at the start of Bob's turn, so Bob loses

Notice that in the first move Alice cannot take 1 or 2 chestnuts, as doing so
would leave a number of chestnuts divisible by A or B. Also, observe that it
does not matter that at the start of Bob's first move, the number of chestnuts
on the pile is divisible by X - it only matters whether this is the case at
the end of his turn.

Write a function that takes as parameters five tuples T^N, T^A, T^B, T^X, T^Y.
Each tuple has five values and together they represent five rounds of the game
that Alice and Bob have played. Specifically, T^N_i, T^A_i, T^B_i, T^X_i, T^Y_i
(0 ≤ i ≤ 4) represents the values of N, A, B, X, Y respectively for the i-th
round.

Your function should return W + 123 where W is the number of rounds that Alice
won. Assume that rounds are independent and that both players play optimally.

For example, if Alice won in 3 out of 5 rounds, you should return 126.

The answer into the crossword will be the output of your function for the
downloadable input file included with this question (in case you're curious).

----

Additional materials

  - [downloadable_input.txt (1 KB)](downloadable_input.txt)