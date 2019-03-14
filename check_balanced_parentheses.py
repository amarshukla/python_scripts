open_lst = ["{", "(", "["]
close_lst = ["}", ")", "]"]

def check_balanced(pat):
    stack = []
    for i in pat:
        if i in open_lst:
            stack.append(i)
        elif i in close_lst:
            pos = close_lst.index(i)
            if len(stack) > 0 and (open_lst[pos] == stack[len(stack) -1]):
                stack.pop()
            else:
                return "unbalanced"
    if len(stack) == 0:
        return "balanced"

print(check_balanced("{([])}"))

# output should be balanced
