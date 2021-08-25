# Remove Island

You're given a two-dimensional array (a matrix) of potentially unequal height
and width containing only 1's and 0's. The matrix represents a two-toned image, where each 1 represents black and each
0 represents white. An island is defined as any number of 1's that are horizontally or vertically adjacent (but not diagonally adjacent) and that don't touch the border of the image. In other words, a group of horizontally or vertically adjacent 1's isn't an island if any of those 1's are in the first row, last row, first column, or last column of the input matrix.

Naturally, you're allowed to mutate the input matrix.

Sample Input

 matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
  ]

Output:
expected = [
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ]
