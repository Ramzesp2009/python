def myAtoi(s: str) -> int:
    """
    Implement the myAtoi(string s) function, which converts a string s to a 32-bit signed integer.

    The algorithm for myAtoi(string s) is as follows:
    1. Read in and ignore any leading whitespace.
    2. Check if the next character (if not already at the end of the string) is '-' or '+'.
       Read this character in if it is either.
       This determines if the final result is negative or positive respectively.
       Assume the result is positive if neither is present.
    3. Read in next the characters until the next non-digit charcter or the end of the input string is reached.
       The rest of the string is ignored.
    4. Convert these digits into an integer in range [-2^31, 2^31 - 1].
       If no digits were read, then the integer is 0.
       Change the sign as necessary (from step 2).
    5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1],
       then clamp the integer so that it remains within the 32-bit signed integer range.
    6. Return the integer as the result.

    :param s: input string
    :return: integer in range [-2^31, 2^31 - 1]
    """
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
