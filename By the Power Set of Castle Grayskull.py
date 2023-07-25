# Write a function that returns all of the sublists of a list/array.

# Example:
# power([1,2,3]);=>[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# For more details regarding this, see the power set entry in wikipedia.


def power(a):
    n = len(a)
    res = []
    for i in range(2**n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(a[j])
        res.append(subset)
    return res



a = [1, 2, 3, 4, 5, 6, 7]
print(power(a))