# def gcd(m,n):
#     if m == n:
#         return m

#     smaller = m if m < n else n
#     greater = m if m > n else n

#     max_divisor = greater / 2 if greater / 2 > smaller else smaller

#     for i in range(max_divisor, 0, -1):
#         if m % i == 0 and n % i == 0:
#             return i
#     return 1

# if __name__ == "__main__":
#     print(gcd(int(input("Enter the first number: ")), int(input("Enter the second number: "))))

def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(gcd(num1, num2))