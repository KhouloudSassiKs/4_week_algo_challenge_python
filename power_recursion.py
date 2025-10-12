def solution(n, pos=1):
    """
    Recursively compute the sum of digits of n, 
    each raised to an increasing power based on its position from right to left.
    
    Example:
        solution(123) 
        -> 3^1 + 2^2 + 1^3 = 3 + 4 + 1 = 8
    """
    if n == 0:
        return 0
    
    digit = n % 10
    return (digit ** pos) + solution(n // 10, pos + 1)


if __name__ == "__main__":
    print(solution(123))   # Output: 8  (3^1 + 2^2 + 1^3)
    print(solution(45))    # Output: 29 (5^1 + 4^2)
    print(solution(0))     # Output: 0
