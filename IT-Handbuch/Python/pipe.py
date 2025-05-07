import os, sys

reader, writer = os.pipe()
pid = os.fork()

if pid == 0:
    os.close(reader)
    write = os.fdopen(writer, 'w')
    for i in range(1, 101):
        print(f"    Child ist bei: {i}")
        write.write(str(i) + "\n")
    sys.exit()
else:
    os.close(writer)
    reader = os.fdopen(reader, 'r')
    while True:
        line = reader.readline()
        if not line:
            sys.exit(0)
        i = int(line)
        print(f"Parent berechnet Quadrat von {i}: {i ** 2}")
    
