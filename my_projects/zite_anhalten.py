import time

startzeit = time.time()
print("Start:", startzeit)
for i in range(5):
    time.sleep(2)
    print(time.time())
endzite = time.time()
print("Ende:", endzite)

differenz = endzite - startzeit
print("Differenz:", differenz)