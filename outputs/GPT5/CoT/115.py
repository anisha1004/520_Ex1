def max_fill(grid, capacity):
    """
    Return the total number of bucket lowerings needed to empty all wells.
    Each row is a well; each '1' is one unit of water; each well uses a bucket
    with the same capacity. For a well with W units, we need ceil(W / capacity) lowerings.

    Examples:
        >>> max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)
        6
        >>> max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)
        5
        >>> max_fill([[0,0,0], [0,0,0]], 5)
        0
    """
    total_lowerings = 0
    for row in grid:
        water = sum(row)
        if water:
            total_lowerings += (water + capacity - 1) // capacity  # ceil division
    return total_lowerings

