Expanding Nebula
================================================================================
You've escaped Commander Lambda's exploding space station along with numerous
escape pods full of bunnies. But -- oh no! -- one of the escape pods has flown
into a nearby nebula, causing you to lose track of it. You start monitoring
the nebula, but unfortunately, just a moment too late to find where the pod
went. However, you do find that the gas of the steadily expanding nebula follows
a simple pattern, meaning that you should be able to determine the previous
state of the gas and narrow down where you might find the pod.

Write a function solution(g) where g is an array of array of bools saying
whether there is gas in each cell (the current scan of the nebula), and return
an int with the number of possible previous states that could have resulted in
that grid after 1 time step.  For instance, if the function were given the
current state c above, it would deduce that the possible previous states were
p (given above) as well as its horizontal and vertical reflections, and would
return 4. The width of the grid will be between 3 and 50 inclusive, and the
height of the grid will be between 3 and 9 inclusive.  The solution will always
be less than one billion (10^9).

--------------------------------------------------------------------------------
- NEBULA:
    -- Modeled as a 2D grid
        -- Flat
        -- Distributed in distinct patches
- Current existence of gas in a cell (within grid) is determined by:
    - 4 Adjacent Cells:
            1. Cell in question (specified)
            2. Cell below it
            3. Cell to the right
            4. Cell below & to the right
For instance:
Let's say the previous state of the grid (p) was:
        .O..
        ..O.
        ...O
        O...

To see how this grid will transform into current grid (c) over the next
time step, consider the 2x2 blocks of cells around each cell.
Of the 2x2 block of
    [
    p[0][0]     (1)
    p[0][1],    (2)    {True}
    p[1][0],    (3)
    p[1][1]     (4)
    ],
Only p[0][1] has gas in it.
p[0][1] (2x2 block) would become:
    c[0][0] with gas in the next time step:
        .O -> O
        ..
Likewise, in the next 2x2 block to the right consisting of [p[0][1], p[0][2],
p[1][1], p[1][2]], two of the containing cells have gas, so in the next state
of the grid, c[0][1] will NOT have gas:
O. -> .
.O

Following this pattern to its conclusion, from the previous state p, the current
state of the grid c will be:
O.O
.O.
O.O

================================================================================
================================================================================
                        ====== OBJECTIVES =======
--------------------------------------------------------------------------------
Write a function solution(g) where g is an array of array of bools saying
whether there is gas in each cell (the current scan of the nebula), and return
an int with the number of possible previous states that could have resulted in
that grid after 1 time step.
--------------------------------------------------------------------------------
- Write fx. {{ solution(g) }}
    - Accepts INPUT (g):
        - Array of an array of bools (True or False)
            - State whether gas in in q cell (current scan of nebula)
    - Returns OUTPUT (int):
        - Number of possible previous states - after 1 time step.
--------------------------------------------------------------------------------
Details:
--------------------------------------------------------------------------------
- NEBULA:
    -- Modeled as a 2D grid
        -- Flat
        -- Distributed in distinct patches
- Current existence of gas in a cell (within grid) is determined by:
    - 4 Adjacent Cells:
            1. Cell in question (specified)
            2. Cell below it
            3. Cell to the right
            4. Cell below & to the right
    - Therefore:
        - If (in current state):
            1 of 4 cells in the 2 x 2 block has gas (True)
        - Then:
            Specified cell will also have gas (true) in the next state
        - Else:
            Cell will be empty (False) in the next state
SOLUTION:
-The solution will always be less than one billion (10^9).
- Resulting output will have - 1 row & column, since the
    - Bottom & rightmost cells do not have a cell below and to the right.
- Grid:
    - Width of grid == 3 and 50 (inclusive)
    - Height of grid will == 3 and 9 (inclusive)
--------------------------------------------------------------------------------
Given Argument(s):
{ (g) }
    --- Array of an array of bools
        - State whether gas in in q cell (current scan of nebula)
================================================================================
================================================================================
                    ========== Test cases ==========
--------------------------------------------------------------------------------
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.
--------------------------------------------------------------------------------
                       ====== Python cases ======
--------------------------------------------------------------------------------
Input:
solution.solution(
        [
    [True, True, False, True, False, True, False, True, True, False],
    [True, True, False, False, False, False, True, True, True, False],
    [True, True, False, False, False, False, False, False, False, True],
    [False, True, False, False, False, False, True, True, False, False]
        ]
    )
Output:
    11567
--------------------------------------------------------------------------------
Input:
solution.solution(
        [
    [True, False, True],
    [False, True, False],
    [True, False, True]
        ]
    )
Output:
    4
--------------------------------------------------------------------------------
Input:
solution.solution(
        [
    [True, False, True, False, False, True, True, True],
    [True, False, True, False, False, False, True, False],
    [True, True, True, False, False, False, True, False],
    [True, False, True, False, False, False, True, False],
    [True, False, True, False, False, True, True, True]
        ]
    )
Output:
    254
