def inch_to_cm(inch):
    cm = inch * 2.54
    return cm


list_inch = [15, 20, 25, 30, 35, 40]

print(f"{'Inch':>6}{'cm':>8}")

for i in list_inch:
    print(f"{i:>6.2f}{inch_to_cm(i):>8}")
