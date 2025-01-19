from zipfile import ZipFile
from pathlib import Path


Path('my_files').mkdir()

with open("my_files/first.txt", 'w') as my_file:
    my_file.write("This is first file")

with open("my_files/second.txt", 'w') as my_file:
    my_file.write("This is second file")

with ZipFile('my_files.zip', 'w') as my_zip_file:

    for file in Path('my_files').iterdir():
        print(file)
        my_zip_file.write(file)

with ZipFile('my_files.zip', 'r') as my_zip_file:
    my_zip_file.extractall('my_files_unzipped')




