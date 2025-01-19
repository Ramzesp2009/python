import os, time

info = os.stat('formatiert.txt')
print('Grosse in Bute:', info.st_size)
aus = '%d.%m.%Y %H.%M.%S'
print('Letzter Zugriff:', time.strftime(aus, time.localtime(info.st_atime)))
print('Letzte Modification:', time.strftime(aus, time.localtime(info.st_mtime)))
print("Erste Erstellung:", time.strftime(aus, time.localtime(info.st_birthtime)))