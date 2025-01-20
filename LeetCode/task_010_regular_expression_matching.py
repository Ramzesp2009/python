def isMatch(input_string, pattern):
    if pattern == '.*' or pattern == '*.':
        return True
    elif pattern == '.':
        return True if len(input_string) == 1 else False
    elif pattern[0] == '*':
        return input_string[-(len(pattern) - 1):] == pattern[-(len(pattern) - 1):]
    elif pattern[0] == '.':
        return input_string[1:] == pattern[1:]
    elif pattern[-1] == '*':
        return input_string[:len(pattern) - 1] == pattern[:len(pattern) - 1]
    elif pattern[-1] == '.':
        return input_string[:-1] == pattern[:-1]
    elif pattern == '*':
        return True
    else:
        return False


print(isMatch("aacc", "a*"))

# print(-(len(pattern) - 1))