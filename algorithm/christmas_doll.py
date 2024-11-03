
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
# def variance(sqsum: list[int], psum: list[int], a: int, b: int):
#     mean = range_sum(psum, a, b) / (b - a + 1)
#     ret = range_sum(sqsum, a, b) - \
#             2 * mean * range_sum(psum, a, b) + \
#             (b - a + 1) * mean * mean
#     return ret / (b - a + 1)

# def grid_sum(psum: list[list[int]], y1: int, x1: int, y2: int, x2: int):
#     ret = psum[y2][x2]
#     if y1 > 0: ret -= psum[y1 - 1][x2]
#     if x1 > 0: ret -= psum[y2][x1 - 1]
#     if y1 > 0 and x1 > 0: ret += psum[y1 - 1][x1 - 1]
#     return ret

def ways_to_buy(psum: list[int], k: int) -> int:
    mod = 20091101
    ret = 0
    count = [0 for _ in range(100000)]
    for i in range(len(psum)):
        count[psum[i]] += 1
    for i in range(0, k):
        if count[i] >= 2:
            ret = (ret + ((count[i] * (count[i] - 1)) / 2)) % mod
    return ret


def max_buys(psum: list[int], k: int):
    ret = [0 for _ in range(len(psum))]
    prev = [-1 for _ in range(100000)]
    for i in range(len(psum)):
        if i > 0:
            ret[i] = ret[i - 1]
        else:
            ret[i] = 0
        loc = prev[psum[i]]
        if loc != -1: ret[i] = max(ret[i], ret[loc] + 1)
        prev[psum[i]] = i
    return ret[-1]


c = int(input("test case > "))
for _ in range(c):
    n, k = map(int, input("num of doll box, num of children > ").split(" "))
    dolls = list(map(int, input("num of doll in box > ").split(" ")))
    # get partial sum
    psum = partial_sum(dolls)
