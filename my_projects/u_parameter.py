def steuer(x):
    if x > 2500:
        print(f"Gehalt ist {x} dann Steuer wird 22% also {x / 100 * 22}Euro")
    else:
        print(f"Gehalt ist {x} dann Steuer wird 18% also {x / 100 * 18}Euro")


gehalt = int(input("Bitte geben Sie Ihre Gehalt ein: "))
steuer(gehalt)