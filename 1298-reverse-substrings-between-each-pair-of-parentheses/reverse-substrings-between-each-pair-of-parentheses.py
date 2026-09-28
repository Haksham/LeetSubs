class Solution(object):
    def reverseParentheses(self, s):
        stack = []

        for c in s:
            if c == ")":
                temp = ""

                while stack[-1] != "(":
                    temp += stack.pop()

                stack.pop()  # remove "("

                for c in temp:
                    stack.append(c)

            else:
                stack.append(c)

        return "".join(stack)