
# 5a. "Recreation through recreating"

You are given two strings `A` and `B` consisting of lowercase characters from
the English alphabet. The maximum length of each string is `10^5`.

Your aim is to generate `A` by concatenating a minimum number of copies of `B`.
Before concatenating a copy of string `B` you can choose to remove any number of
characters from that copy.

It is guaranteed that it is possible to create string `A` using a finite number
of copies of string `B` in this way.

Write a function that takes two strings `A` and `B` as inputs, and outputs the
minimum number of copies of string `B` required to make string `A`.

For example, the output of `solution('xyxy', 'xyy')` would be `2`. We can
generate string `xyxy` by concatenating two modified copies of `xyy` as follows:

  - Create a first instance of `xyy`
  
  - Remove either the second or the third character, giving `xy`
  
  - Create a second instance of `xyy`
  
  - Again remove either the second or the third character, giving `xy`
  
  - Concatenate the two strings to give `xyxy`

The answer into the crossword will be the output of your function for the
downloadable input file included with this question (in case you're curious).

----

Additional materials

  - [downloadable_input.txt (196 KB)](downloadable_input.txt)