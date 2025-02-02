inp = [6,9,4]
res = []
subset = []
def dfs(i):
    if i >= len(inp):
        res.append(subset.copy())
        return
    subset.append(inp[i])
    dfs(i+1)
    subset.pop()
    dfs(i+1)
dfs(0)
print(res)