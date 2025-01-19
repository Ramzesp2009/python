import sys
try:
    d = open('formatiert.txt', 'r+')
except:
    print('Datei nicht geoffnet')
    sys.exit(0)

dslange = 51
for i in range(3):
    d.seek(30 + dslange*i)
    gehalt = float(d.read(8))
    gehalt = round(gehalt *1.05, 2)
    # gehalt = round(gehalt / 1.05, 2)
    d.seek(30 + dslange*i)
    d.write(f'{gehalt:8.2f}')

d.close()