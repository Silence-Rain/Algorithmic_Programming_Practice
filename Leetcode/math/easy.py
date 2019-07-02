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

# 69. Sqrt(x)
def mySqrt(x: int) -> int:
    r = x
    while r * r > x:
        r = (r + x / r) // 2
    return int(r)