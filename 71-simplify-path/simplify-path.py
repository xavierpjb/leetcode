class Solution:
    def simplifyPath(self, path: str) -> str:
        # split string on /

        # process from start of string
        # for each element:
        # if . proceed
        # if .., if stack non-empty remove from stack
        # else, add to stack
        # join route on /

        subPaths = filter(lambda x: len(x) > 0, path.split("/"))
        stack = []

        for subPath in subPaths:
            if subPath == "..":
                if len(stack) > 0:
                    stack.pop()
            elif subPath != ".":
                stack.append(subPath)

        return "/" + "/".join(stack)
        