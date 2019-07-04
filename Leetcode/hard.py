import math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def findSubstring(s: str, words: list) -> list:
    s_l = len(s)
    ws_l = len(words)
    ret = []
    if not s_l or not ws_l:
        return []
    
    w_l = len(words[0])
    words_map = {}
    for item in words:
        if item in words_map:
            words_map[item] += 1
        else:
            words_map[item] = 1
    
    for i in range(s_l - w_l * ws_l + 1):
        w_map_temp = words_map.copy()
        if s[i:i + w_l] in w_map_temp:
            flag = True
            for j in range(ws_l):
                temp_str = s[i + w_l * j:i + w_l * (j + 1)]  
                if temp_str in w_map_temp and w_map_temp[temp_str] != 0:
                    w_map_temp[temp_str] -= 1
                else:
                    flag = False
                    break
            
            if flag:
                ret.append(i)
                
    return ret

def isNumber(s: str) -> bool:
    def isSign(s):
        return s == '+' or s == '-'
    
    def isUnsignedInt(s):
        if not len(s):
            return False
        
        for i in s:
            if ord(i) < 48 or ord(i) > 57:
                return False
        return True
    
    def isSignedInt(s):
        if not len(s):
            return False
        s = s[1:] if isSign(s[0]) else s
        
        return isUnsignedInt(s)
    
    def isDecimals(s):
        if not len(s):
            return False
        s_dot = s.split('.')
        
        if len(s_dot) > 2:
            return False
        if len(s_dot) == 1:
            return isSignedInt(s)
        
        if len(s_dot[0]):
            if len(s_dot[1]):
                return (isSignedInt(s_dot[0]) or isSign(s_dot[0])) and isUnsignedInt(s_dot[1])
            else:
                return isSignedInt(s_dot[0])
        else:
            if len(s_dot[1]):
                return isUnsignedInt(s_dot[1])
            else:
                return False
    
    s = s.strip()
    s_e = s.split('e')
    
    if len(s_e) > 2:
        return False
    if len(s_e) == 1:
        return isDecimals(s)
    
    return isDecimals(s_e[0]) and isSignedInt(s_e[1])
        

