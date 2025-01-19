
while True:
    try:
        num_1 = float(input("Enter number one number: "))
        num_2 = float(input("Enter number two number: "))
    except ValueError as e:
        print(e)
        print("You must enter numbers!")
        continue

    try:
        print(num_1 / num_2)
    except ZeroDivisionError as e:
        print(e)
        print("The second numbers must be not zero! Try one more time.")
        continue


    answer_user = input("Do you want to continue? Yes / No: ")

    if answer_user.lower() == 'yes':
        continue
    elif answer_user.lower() == 'no':
        break
    else:
        print("You entered incorrect answer, we'll continue.")