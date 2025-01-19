import time

'''start_time = time.time()
print(time.ctime(23452345348))
time.sleep(2)
end_time = time.time()
print(end_time - start_time)'''


start_time = time.time()
my_range = list(range(500000000))
print(my_range[10000])
end_time = time.time()
print("Total duration of the operation: ", end_time - start_time)
