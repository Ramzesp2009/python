from array import array

my_int_array = array('i', [4, 5, 10, 5, 7])

with open('my_array.bin', 'wb') as my_file:
    my_int_array.tofile(my_file)

imported_array = array('i')

with open('my_array.bin', 'rb') as my_file:
    imported_array.fromfile(my_file, 3)
    print(imported_array)

imported_array.reverse()
print(imported_array)