def myAtoi(s: str) -> int:
    # Remove leading whitespace
    s = s.lstrip()

    # Check for sign
    sign = 1
    if s and s[0] in ['-', '+']:
        if s[0] == '-':
            sign = -1
        s = s[1:]

    # Read digits
    digits = ''
    for char in s:
        if char.isdigit():
            digits += char
        else:
            break

    # Convert to integer
    num = int(digits) if digits else 0

    # Apply sign
    num *= sign

    # Clamp to 32-bit signed integer range
    num = max(-2**31, min(num, 2**31 - 1))

    return num


print(myAtoi('1337c0d3'))
print(myAtoi(' -042'))
print(myAtoi('0-1'))
print(myAtoi("words and 987"))

