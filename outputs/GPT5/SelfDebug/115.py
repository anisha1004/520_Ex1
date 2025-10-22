import math
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    """
    Calculate the total number of bucket lowerings needed to empty all wells.
    Each row is a well; each '1' is one unit of water. A single lowering for a well
    can remove up to `capacity` units from that same well.

    Args:
        grid: 2D list of 0/1 integers where each row represents a well.
        capacity: Positive integer bucket capacity (>=1).

    Returns:
        Total number of times buckets must be lowered across all wells.

    Examples:
        >>> max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)
        6
        >>> max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)
        5
        >>> max_fill([[0,0,0], [0,0,0]], 5)
        0
    """
    # Edge cases considered and fixed:
    # 1) Avoid float rounding issues from math.ceil on floats by using integer ceil: (x + cap - 1) // cap.
    # 2) Handle rows safely even if any contain non-0/1 values by counting explicit 1s only.
    # 3) Gracefully handle empty rows (count = 0) without division concerns.
    total_lowerings = 0
    for row in grid:
        water_units = sum(1 for v in row if v == 1)
        if water_units == 0:
            continue
        total_lowerings += (water_units + capacity - 1) // capacity
    return total_lowerings
