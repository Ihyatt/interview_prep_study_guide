from collections import defaultdict


def min_window(s: str, t: str) -> str:
    len1 = len(s)
    len2 = len(t)
    if len1 < len2:
        return ""
    
    hash_pat = defaultdict(int)
    hash_str = defaultdict(int)
    
    for c in t:
        hash_pat[c] += 1
    
    count = 0 
    l = 0
    min_window = ""
        
    for r in range(len(s)):
        if s[r] in hash_pat:
            hash_str[s[r]] += 1
            if hash_str[s[r]] <= hash_pat[s[r]]:
                count += 1
        while count == len2:
            window = s[l: r + 1]
            if not len(min_window) or len(window) < len(min_window):
                min_window = window
            if s[l] in hash_str:
                hash_str[s[l]] -= 1
                if hash_str[s[l]] < hash_pat[s[l]]:
                    count -= 1
            l += 1
    return min_window