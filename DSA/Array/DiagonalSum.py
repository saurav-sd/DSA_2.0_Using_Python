def diagonalSum(mat):
    n = len(mat)
    total_sum = 0

    for i in range(n):
        # Add primary diagonal element
        total_sum += mat[i][i]
        # Add secondary diagonal element
        # Row is 'i', Column is 'n - 1 - i'
        total_sum += mat[i][n-1-i]

    # If 'n' is odd, the center element was added twice. 
    # We must subtract it once.
    if n%2 != 0:
        center_index = n//2
        total_sum -= mat[center_index][center_index]

    return total_sum

if "__main__" == __name__:
    mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

    print("Total sum : ", diagonalSum(mat))