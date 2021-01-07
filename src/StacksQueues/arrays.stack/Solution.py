class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {")": "(", "}": "{", "]": "["}
        for i in range(len(s)):
            flag = True
            for right, left in char_map.items():
                if s[i] == right and stack[-1:] == [left]:
                    stack.pop()
                    flag = False
            if flag:
                stack.append(s[i])
        return bool(len(stack) == 0)


class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if len(s) < 2:
                return False
            if s[i] == ")" and stack[-1:] == ["("]:
                stack.pop()
            elif s[i] == "}" and stack[-1:] == ["{"]:
                stack.pop()
            elif s[i] == "]" and stack[-1:] == ["["]:
                stack.pop()
            else:
                stack.append(s[i])
        return bool(len(stack) == 0)


if __name__ == '__main__':
    stack = []
    print(stack[-1:])
    # print(stack[-1])
    stack = ["111", "{"]
    print(stack[-1:])
    print(stack[-1])

    print(Solution().isValid(")(){}"))
    print(Solution2().isValid(")(){}"))
