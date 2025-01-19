# def greeting(greet):
#     def info(name):
#         return f"{greet}, {name}!"
#     return info

def greeting(greet):
    return lambda name: f"{greet}, {name}!"


morning_greeting = greeting("Good Morning")

print(morning_greeting('Maria'))

evening_greeting = greeting("Good Evening")

print(evening_greeting('Pavlo'))
