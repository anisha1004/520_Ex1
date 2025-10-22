import math

def max_fill(grid: list[list[int]], capacity: int) -> int:
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    # Correction for Bug 1: Handle invalid non-positive capacity.
    if capacity <= 0:
        # Check if there is any water in the grid at all.
        if any(sum(well) for well in grid):
            raise ValueError("Bucket capacity must be a positive integer.")
        return 0

    # Correction for Bug 2 & 3: Use a concise generator expression and
    # ensure the final return type is an integer.
    # This approach is efficient and correctly handles edge cases like an empty grid.
    total_fills = sum(math.ceil(sum(well) / capacity) for well in grid)
    
    return int(total_fills)
