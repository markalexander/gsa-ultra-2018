
# GSA ULTRA 2018

This repository contains my submission for GSA ULTRA 2018.


## Structure

Each problem is its own Python package.  Solution functions are not run directly
but rather through the comprehensive unit testing framework.  Each problems
unit tests can be found in the package directory in a file named
`test_[problem_id].py`. These tests can be run using
[pytest](https://docs.pytest.org/en/latest/), either for individual problems
or the entire crossword (see below).

The solutions themselves can be found in the same directory within the
`solutions.py` file.  Some problems also have a `pathological.py` file used for
generating worst-case examples.

Each `solutions.py` file has a short explanation of the approach taken.


## Problems

Problem statements can be found in the README files of the respective
directories.  A list is given below.

### Across

  - [1. Hello world](crossword/across/hello_world)
  - [5. Recreation through recreating](crossword/across/recreation)
  - [7. A cryptic crossword clue](crossword/across/cryptic_clue)
  - [10. Horse-chestnutting around](crossword/across/horse_chestnutting)
  - [12. Mission Demolition](crossword/across/mission_demolition)

### Down

  - [1. Having a ball](crossword/down/having_a_ball)
  - [2. Flower power](crossword/down/flower_power)
  - [3. Fearful symmetry](crossword/down/fearful_symmetry)
  - [4. Fibonarcos](crossword/down/fibonarcos)
  - [6. Alan and Ada](crossword/down/alan_and_ada)
  - [8. Barb the builder](crossword/down/barb_the_builder)
  - [9. Truly a mazing mouse](crossword/down/amazing_mouse)
  - [11. Squared away](crossword/down/squared_away)


## Setup and running

Per the competition rules, the examples run in a Python 3.4 environment.

This can be set up e.g. with 'conda:

    conda create -n ultra python=3.4

The required packages (essentially just pytest) can then be installed with:

    pip install -r requirements.txt

Tests can then be run for individual problems:
    
    pytest crossword/[direction]/[problem_id]/
    
Or for the entire crossword:

    pytest crossword/

