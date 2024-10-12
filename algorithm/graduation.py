# using bitmask
# first input test case C<=50
# second input number of total subject 1<=N<=12
# number of subject he is going to listen 0<=K<=N
# number of semester 1<=M<=10
# number of maximum can listen 1<=L<=10
INF = 987654321
MAXN = 12
results = []

def bit_count(x: int):
    if x == 0:
        return 0
    return x % 2 + bit_count(x // 2)

def graduate(
    prerequisite,
    classes,
    cache,
    semester: int,
    taken: int,
    n: int,
    k: int,
    m: int,
    l: int
) -> int:
    if bit_count(taken) >= k: return 0
    if semester == m: return INF
    ret = cache[semester][taken]
    if ret != -1: return ret
    ret = INF
    can_take = (classes[semester] & ~taken)
    for i in range(n):  
        if (can_take & (1 << i)) and ((taken & prerequisite[i]) != prerequisite[i]):
            can_take &= ~(1 << i)
    take = can_take
    while take > 0:
        if bit_count(take) > l:
            take = ((take - 1) & can_take)
            continue
        ret = min(
            ret,
            graduate(
                prerequisite,
                classes,
                cache,
                semester + 1,
                taken | take,
                n,
                k,
                m,
                l
            ) + 1
        )
        take = ((take - 1) & can_take)

    ret = min(
        ret,
        graduate(
            prerequisite,
            classes,
            cache,
            semester + 1,
            taken,
            n,
            k,
            m,
            l
        )
    )
    cache[semester][taken] = ret
    return ret

test_case = int(input("test case>> "))
for t in range(0, test_case):
    prerequisite: list[int] = [0 for _ in range(MAXN)]
    classes: list[int] = [0 for _ in range(10)]
    cache: list[list[int]] = [[-1 for _ in range(1 << 12)] for _ in range(10)]
    n, k, m, l = map(int, input("info>> ").split(" "))
    # number of n and m
    for i in range(0, n):
        r = input("R>> ")
        nums = list(map(int, r.split(" ")))
        if len(nums) > 1:
            for num in nums[1:]:
                prerequisite[i] |= (1 << num)

    for i in range(0, m):
        c = input("C>> ")
        nums = list(map(int, c.split(" ")))
        if len(nums) > 1:
            for num in nums[1:]:
                classes[i] |= (1 << num)

    res = graduate(
        prerequisite,
        classes,
        cache,
        0,
        0,
        n,
        k,
        m,
        l
    )
    if res <= m:
        results.append(res)
    else:
        results.append("IMPOSSIBLE")

for result in results:
    print(result)
