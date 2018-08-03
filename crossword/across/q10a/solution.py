# -*- coding: utf-8 -*-

"""
10a. Horse-chestnutting around

Recursive/DP method for subtraction/nim-like games.  Could have done something
more analytic, but it's a little painful and the DP approach seems to be fine
computationally.

I've used a class to represent the game here for convenience.

See e.g.:

  - https://www.cs.cmu.edu/afs/cs/academic/class/15859-f01/www/notes/comb.pdf
  - http://www.users.miamioh.edu/fishert4/docs/fisher-algo.pdf

"""


def solution(t_n, t_a, t_b, t_x, t_y) -> int:
    """Get the number of times Alice wins in the given set of games.

    Args:
        t_n: The values of N for each round.
        t_a: The values of A for each round.
        t_b: The values of B for each round.
        t_x: The values of X for each round.
        t_y: The values of Y for each round.

    Returns:
        The number of times Alice wins.

    """
    alice_win_count = 0
    for r in range(len(t_n)):
        n, a, b, x, y = t_n[r], t_a[r], t_b[r], t_x[r], t_y[r]
        g = AliceBobGame(n, a, b, x, y)
        # N.B. Alice is player 0, Bob is player 1
        if g.winner == 0:
            alice_win_count += 1
    return alice_win_count + 123


def crossword_solution() -> int:
    """Get the solution output for the crossword clue input.

    (Used in local testing framework; not needed for the GSA web environment).

    Returns:
        The crossword entry.

    """
    import os
    input_f = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                           'downloadable_input.txt')
    with open(input_f, 'r') as f:
        lines = f.readlines()
    t_n, t_a, t_b, t_x, t_y = [], [], [], [], []
    for line in lines:
        line = [int(x) for x in line.split(' ')]
        t_n.append(line[0])
        t_a.append(line[1])
        t_b.append(line[2])
        t_x.append(line[3])
        t_y.append(line[4])
    t_n, t_a, t_b, t_x, t_y = tuple(map(tuple, (t_n, t_a, t_b, t_x, t_y)))
    return solution(t_n, t_a, t_b, t_x, t_y)


class AliceBobGame:
    """Class that defines an instance of the game."""

    def __init__(self, n: int, a: int, b: int, x: int, y: int) -> None:
        """Create a new game.

        Args:
            n: The value of N.
            a: The value of A.
            b: The value of B.
            x: The value of X.
            y: The value of Y.
        """
        self.n = n
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.cache = {}
        for i in range(n + 1):
            self.cache[i] = {}

    def valid_moves(self, n: int, p: int):
        """Get the valid moves for the given player at the given state.

        Args:
            n: The number left in the pile.
            p: The player (0 or 1).

        Returns:
            The valid moves for the player, in terms of the number of chestnuts
            they may take on this turn.

        """
        moves = []
        if p == 0:
            d = (self.a, self.b)
        else:
            d = (self.x, self.y)
        if d[0] == d[1]:
            d = (d[0],)
        for move in [1, 2, 3]:
            next_n = n - move
            if next_n == 0:
                moves.append(move)
            elif next_n > 0:
                for div in d:
                    if (n - move) % div != 0:
                        moves.append(move)
        return moves

    @property
    def winner(self) -> int:
        """Get the overall winner of the game from starting n.

        Returns:
            The winner (0 or 1 for player 0 or player 1).

        """
        return self.get_winner(self.n)

    def get_winner(self, n: int, p: int = 0) -> int:
        """Get the overall winner of the game for arbitrary n and player.

        Returns:
            The winner (0 or 1 for player 0 or player 1).

        """
        other_p = 1 - p
        # If we are at n=0 then we already lost, other player wins
        if n == 0:
            return other_p
        # Check cache
        if p in self.cache[n]:
            return self.cache[n][p]
        # For each of our possible moves on this turn
        for this_p_move in self.valid_moves(n, p):
            # Look for a winning move
            if self.get_winner(n - this_p_move, other_p) == p:
                # We win, so take this move
                self.cache[n][p] = p
                return p
        # We couldn't find a winning move
        self.cache[n][p] = other_p
        return other_p
