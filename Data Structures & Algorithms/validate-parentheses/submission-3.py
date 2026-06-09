class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []

        for char in s:
            try:
                match char:
                    case '(':
                        stack.append('(')
                    case '[':
                        stack.append('[')
                    case '{':
                        stack.append('{')
                    case ')':
                        temp = stack.pop()
                        if temp != '(':
                            return False
                    case ']':
                        temp = stack.pop()
                        if temp != '[':
                            return False
                    case '}':
                        temp = stack.pop()
                        if temp != '{':
                            return False
                    case _:
                        return False
            except IndexError:
                return False
        
        return len(stack) == 0
            



        