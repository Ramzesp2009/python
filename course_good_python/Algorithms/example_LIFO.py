# a = input("Enter a string: ")
# a = "<p>Title</p>"
a = "[]<(>){}"

stack = []
flVerfy = True

for i in a:
    if i in "([{":
        stack.append(i)
    elif i in ")]}":
        if len(stack) == 0:
            flVerfy = False
            break

        br = stack.pop()
        if br == '(' and i == ')':
            continue
        if br == '[' and i == ']':
            continue
        if br == '{' and i == '}':
            continue
        flVerfy = False
        break

if flVerfy and len(stack) == 0:
    print("Balanced")
else:
    print("Not Balanced")