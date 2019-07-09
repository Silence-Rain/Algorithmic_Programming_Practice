# 3. Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s: str) -> int:
    dic, length, i, j = {}, 0, 0, 0
    while i < len(s) and j < len(s):
        if s[j] not in dic:
            dic[s[j]] = 1
            j += 1
            length = max(length, j - i)  
        else:
            dic.pop(s[i])
            i += 1
    
    return length

# 5. Longest Palindromic Substring
def longestPalindrome(s: str) -> str:
    if len(s) < 2:
        return s

    n, maxLen, start, i = len(s), 0, 0, 0
    for i in range(0, n):
        if len(s) - i <= maxLen / 2:
            break

        left, right = i, i
        while right < n - 1 and s[right + 1] == s[right]:
            right += 1

        while right < n - 1 and left > 0 and s[right + 1] == s[left - 1]:
            right += 1
            left -= 1

        if maxLen < right - left + 1:
            maxLen = right - left + 1
            start = left

    return s[start:maxLen + start]