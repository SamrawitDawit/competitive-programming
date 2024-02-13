t = int(input())
for _ in range(t):
    n = int(input())
    nums= list(map(int, (s for s in input())))
    prefix_dic = {}
    prefix_dic[0] = 1
    prefix, ans = 0, 0
    for i in range(n):
        prefix += nums[i]
        ans += prefix_dic.get(prefix-(i+1), 0)
        prefix_dic[prefix-(i+1)] = prefix_dic.get(prefix-(i+1), 0) + 1
    print(ans)