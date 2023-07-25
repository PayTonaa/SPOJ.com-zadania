def bit_reversal(n):
    # Assume n has 8 bits
    result = 0
    for i in range(8):
        # Check if ith bit is set
        if n & (1 << i):
            # Set (7-i)th bit in result
            result |= (1 << (7-i))
    return result