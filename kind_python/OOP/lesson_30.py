def func2():
    try:
        return 1 / 0
    except Exception as e:
        print(e)

def func1():
    # try:
    #     return func2()
    # except Exception as e:
    #     print(e)
    return func2()

print("something1")
print("something2")
print("something3")
# try:
#     func1()
# except Exception as e:
#     print(e)
func1()
print("something4")
print("something5")
print("something6")