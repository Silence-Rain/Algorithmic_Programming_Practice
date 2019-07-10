# 7. Reverse Integer
def reverse(x: int) -> int:
    xlist = list(str(x))
    xlist.reverse()
    
    if xlist[-1] == '-':
        xlist.pop()
        xlist.insert(0, '-')
        
    ret = int("".join(xlist))
    return ret if ret >= - 2 ** 31 and ret <= 2 ** 31 - 1 else 0

# 9. Palindrome Number
def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reverted = 0
    while x > reverted:
        reverted = reverted * 10 + x % 10
        x = int(x / 10)
        
    return x == reverted or x == int(reverted / 10)

# 13. Roman to Integer
def romanToInt(s: str) -> int:
    mapping, ret, n = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }, 0, len(s)

    for i in range(n - 1):
        cur, next = mapping[s[i]], mapping[s[i + 1]]
        if cur >= next:
            ret += cur
        else:
            ret -= cur
            
    return ret + mapping[s[n - 1]]

# 69. Sqrt(x)
def mySqrt(x: int) -> int:
    r = x
    while r * r > x:
        r = (r + x / r) // 2
    return int(r)