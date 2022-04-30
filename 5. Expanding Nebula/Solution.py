

--------------------------------------------------------------------------------
def solution(g):
    # Columns (not rows) for efficiency
    transposed = tuple(zip(*g))
    # Generate first column's preimages
    preimgs = precol(transposed[0])

    # Initialize first pair end values to 1
    precount = dict()
    for pair in preimgs:
        precount[pair[0]] = 1
    """
    Loop through, adding paths to get to the first value in the pair in the
    previous iteration to the location of the second value in the pair for th
    current iteration.
    """
    for col in transposed:
        # Generate preimage
        preimgs = precol(col)
        count = dict()
        for pair in preimgs:
            # Check all values initialized
            if pair[0] not in precount: precount[pair[0]] = 0
            if pair[1] not in count: count[pair[1]] = 0
            """
            Check left side of next column with right side of previous column.
            Achieve by adding previous iteration of left num sum to current
            iteration of right num sum.
            """
            count[pair[1]] += precount[pair[0]]
        # Reset prev for next iteration
        precount = count

    return sum(precount.values())

def precol(col):
    """
    Fx for generating first column's preimages.
    """
    possib = ((0, 0), (0, 1), (1, 0), (1, 1))
    curr = devol[col[0]]
    for i in range(1, len(col)):
        new = []
        for tes in curr:
            for comb in possib:
                if evol[(tes[i], comb)] == col[i]:
                    new.append(tes+(comb,))
        curr = tuple(new)
    bin_ret = [tuple(zip(*i)) for i in curr]
    # Convert to decimal pair
    return [tuple([bitlist(nu) for nu in possibl]) for possibl in bin_ret]

def bitlist(bitsl):
    """
    Fx to convert list of bits to integers.
    """
    out = 0
    for bit in bitsl:
        out = (out << 1) | bit
    return out

# Base matrices (evolution/devolution)
evol = {((0, 0), (0, 0)): 0, ((0, 0), (0, 1)): 1, ((0, 0), (1, 0)): 1,
        ((0, 0), (1, 1)): 0, ((0, 1), (0, 0)): 1, ((0, 1), (0, 1)): 0,
        ((0, 1), (1, 0)): 0, ((0, 1), (1, 1)): 0, ((1, 0), (0, 0)): 1,
        ((1, 0), (0, 1)): 0, ((1, 0), (1, 0)): 0, ((1, 0), (1, 1)): 0,
        ((1, 1), (0, 0)): 0, ((1, 1), (0, 1)): 0, ((1, 1), (1, 0)): 0, ((1, 1), (1, 1)): 0}
devol = {0: (((0, 0), (0, 0)), ((0, 0), (1, 1)), ((0, 1), (0, 1)), ((0, 1), (1, 0)),
             ((0, 1), (1, 1)), ((1, 0), (0, 1)), ((1, 0), (1, 0)), ((1, 0), (1, 1)),
             ((1, 1), (0, 0)), ((1, 1), (0, 1)), ((1, 1), (1, 0)), ((1, 1), (1, 1))),
         1: (((1, 0), (0, 0)), ((0, 1), (0, 0)), ((0, 0), (1, 0)), ((0, 0), (0, 1)))}
