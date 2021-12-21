
def longestCommonPrefix(strs):
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 

def longestCommonPrefix2(m):
    if not m: 
        return ''
    s1 = min(m)
    s2 = max(m)

    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i] #stop until hit the split index
    return s1   

def longestCommonPrefix3(strs):
    if not strs:
        return ""
    min_len = len(min(strs, key=len))
    low = 1
    high = min_len
    while low <= high:
        mid = (low + high)//2
        prefix = strs[0][:mid]
        if all(s.startswith(prefix) for s in strs[1:]):
            low = mid + 1
        else:
            high = mid - 1
    return strs[0][:(low + high)//2]         

strs = ["flower","flow","flight"]
print(longestCommonPrefix3(strs))
