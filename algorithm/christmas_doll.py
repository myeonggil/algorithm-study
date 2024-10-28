
# first
# calculate partial sum
def partial_sum(a: list[int]):
    ret: list[int] = [-1 for _ in range(len(a))]
    ret[0] = a[0]
    for i in range(1, len(a)):
        ret[i] = ret[i - 1] + a[i]
    return ret

# partial sum vector psum, find sum from a to b
def range_sum(psum: list[int], a: int, b: int):
    if a == 0: return psum[b]
    return psum[b] - psum[a - 1]

# find variance
def variance(sqsum: list[int], psum: list[int], a: int, b: int):
    mean = range_sum(psum, a, b) / (b - a + 1)
    ret = range_sum(sqsum, a, b) - \
            2 * mean * range_sum(psum, a, b) + \
            (b - a + 1) * mean * mean
    return ret / (b - a + 1)

scores = [100, 97, 86, 79, 66, 52, 49, 42, 31]
psum = partial_sum(scores)

