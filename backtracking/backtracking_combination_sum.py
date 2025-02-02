target = 7
candidates = [2,3,6,7]

res = []
def dfs(i, cur, total):
    if total == target:
        res.append(cur.copy())
        return
    if i>=len(candidates) or total > target:
        return
    
    cur.append(candidates[i])
    # total = total + candidates[i]
    dfs(i,cur,total + candidates[i])
    cur.pop()
    dfs(i+1, cur, total)
dfs(0,[],0)
print(res)
