
def removeInvalidParentheses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    def isValid(s):
        left_paren_count = 0
        for c in s:
            if c== '(':
                left_paren_count += 1
            elif c == ')':
                if left_paren_count == 0:
                    return False
                left_paren_count -= 1
            else:
                continue
        return left_paren_count == 0

    def getCount(s):
        rslt = True
        l, r = 0, 0  # extrac l or r parenthesis
        for c in s:
            l += c == '('
            if c == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1
        return (l, r)

    rslt = []

    def dfs(s, idx, l, r):
        if l == 0 and r == 0:
            if isValid(s):
                rslt.append(s)
            return
            # delete extra l or r, every time we only delete one
        for i in range(idx, len(s)):
            c = s[i]
            if i - 1 >= idx and c == s[i - 1]:  # to avoid duplication
                continue
            if c == ')':
                new_s = s[:i] + s[i + 1:]
                dfs(new_s, i, l, r - 1)
            if c == '(':
                new_s = s[:i] + s[i + 1:]
                dfs(new_s, i, l - 1, r)

    rslt = []
    l, r = getCount(s)
    dfs(s, 0, l, r)
    return rslt

a = '(9)((23abc))()'
removeInvalidParentheses(a)