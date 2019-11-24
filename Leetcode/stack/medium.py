# 394. Decode String
def decodeString(s: str) -> str:
    stack = [[1, "", ["1"]]]
    num_flag = True
    for i in range(len(s)):
        if 57 >= ord(s[i]) >= 48:
            if num_flag:
                stack.append([0, "", [s[i]]])
                num_flag = False
            else:
                stack[-1][2].append(s[i])
        elif s[i] == '[':
            num_flag = True
            stack[-1][0] = int("".join(stack[-1][2]))
        elif s[i] == ']':
            temp = stack.pop()
            stack[-1][1] += (temp[1] * temp[0])
        else:
            stack[-1][1] += s[i]

    return stack[-1][1] * stack[-1][0]