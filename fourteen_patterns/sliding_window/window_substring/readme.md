# Window Substring


```python
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
```

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```


```
hash_pat = {
"A": 1
"B": 1
"C": 1
}
hash_str = {}
count = 0 
l = 0 
min_window = ""

HASH_PAT dictionary contains frequency of pattern characters. 
HASH_STR dictionary will keep track of patterns characters found in string.
COUNT will keep track of character frequency match of HASH_STR with HASH_PAT
```

```
A D O B E C O D E B A N C
L
R

hash_str = {
 "A":1
}

hash_pat = {
 "A": 1
 "B": 1
 "C": 1
}

count = 1

If there is a character match with HASH_PAT, add and increment in HASH_STR
If the frequencies match, then increment count
```


```
A D O B E C O D E B A N C
L
          R

hash_str = {
 "A": 1
 "B": 1
 "C": 1
}

hash_pat = {
 "A": 1
 "B": 1
 "C": 1
}

count = 3

A match has been found as shown by COUNT
Move LEFT pointer until COUNT is no longer equal to the length of HASH_PAT
Keep track of MIN_WINDOW so far
```


```
A D O B E C O D E B A N C
                  L
                        R

hash_str = {
 "A": 1
 "B": 1
 "C": 1
}

hash_pat = {
 "A": 1
 "B": 1
 "C": 1
}

count = 3

A while loop is important to use to detract window
```
