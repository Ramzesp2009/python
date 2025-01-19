from os import path
from pathlib import Path

# from os import path
print(path.abspath('.'))  # C:\Python\training_code
print(type(path))  # <class 'module'>
print()

# from pathlib import Path
print(Path('.').absolute())  # C:\Python\training_code
print(type(Path))  # <class 'type'>
print()

print(Path.cwd())  # C:\Python\training_code
print()

directory = Path('C:/') / ('Python') / ('django')
if not directory.exists():
    directory.mkdir()

if directory.exists():
    directory.rmdir()

print(Path('C:/') / ('Python') / ('training_code'))
print(Path('C:/').joinpath('Python').joinpath('training_code'))
print(type(Path('.')))

