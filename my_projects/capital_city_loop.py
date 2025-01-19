import random

capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': "Sacramento",
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Tallahassee',
    'Georgia': 'Atlanta',
}

state, capital = random.choice(list(capitals_dict.items()))

while True:
    answer_user = input(f"What is the capital of {state}: ").lower()
    if answer_user == capital.lower():
        print("Correct")
        break
    elif answer_user == 'exit':
        print(f"Correct answer is {capital}. Goodbye")
        break
