from pathlib import Path

files_dir = Path('C:/') / ('Python') / ('files')
files_dir.mkdir(exist_ok=True)

first_file = files_dir / 'first.txt'
second_file = files_dir / 'second.txt'

# with open(files_dir / 'first.txt', 'w') as f:
# with open('C:/Python/files/first.txt', 'w') as f:
with open(first_file, 'w') as f:
    f.write("First line\n")
    f.write("Second line\n")

# with open(files_dir / 'second.txt', 'w') as f:
# with open('C:/Python/files/second.txt', 'w') as f:
with open(second_file,'w') as f:
    lines = [
        "First line in the second file.",
        "Second line in the second file.",
        "Last line in the second file.",
    ]
    for line in lines:
        f.write(f"{line} \n")


with open(files_dir / 'first.txt') as f:
    print(f.read())

with open(files_dir / 'second.txt') as f:
    # Option 1
    # for line in f.readlines():
    #     print(line)

    # Option 2
    # while True:
    #     line = f.readline()
    #     if not line:
    #         break
    #     print(line.strip())  # This one is the best
        # print(line, end=' ')  # This one is worst

    # Option 3
    for line in f:
        print(line.strip())

# first_file.unlink()
# second_file.unlink()
# files_dir.rmdir()



'''dir_files = Path('C:/') / ('Python') / ('files')
if not dir_files.exists():
    dir_files.mkdir()

with open(Path('C:/') / ('Python') / ('files') / ('first.txt'), 'w') as first_file:
    first_file.write('Some string\n')
    first_file.write('Some two string\n')
    first_file.write('Some three string\n')

with open(Path('C:/') / ('Python') / ('files') / ('second.txt'), 'w') as sec_file:
    sec_file.write("Some string\n")
    sec_file.write("Some string\n")
    sec_file.write("Some string\n")

with open(dir_files / 'first.txt') as f_file:
    print(f_file.read())

with open(dir_files / 'second.txt') as sec_file:
    print(sec_file.readline().upper())
    print(sec_file.readline())
    print(sec_file.readline())


if Path('first.txt').exists():
    Path('first.txt').unlink()

if Path('second.txt').exists():
    Path('second.txt').unlink()

# Path('C:/Python/first.txt').unlink()
# Path('C:/Python/second.txt').unlink()'''

