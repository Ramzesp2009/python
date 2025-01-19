import sys

print(sys.argv)

if len(sys.argv) < 3:
    raise IOError("You must provide username and password")

# username = sys.argv[1]
# password = sys.argv[2]

filename, username, password = sys.argv

print(username, password)