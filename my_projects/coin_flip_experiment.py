import random


# Функция для одной попытки броска монеты
def coin_flip_experiment():
    flips = 0
    first_flip = random.choice(['H', 'T'])  # H - Орел (Heads), T - Решка (Tails)
    flips += 1

    while True:
        second_flip = random.choice(['H', 'T'])
        flips += 1
        if second_flip != first_flip:  # Если выпадет другая сторона, эксперимент завершен
            break

    return flips


# Основная функция для проведения 10,000 экспериментов
def main():
    attempts = 10000
    total_flips = 0

    for _ in range(attempts):
        total_flips += coin_flip_experiment()

    average_flips = total_flips / attempts
    print(f"Среднее количество бросков: {average_flips:.2f}")


if __name__ == "__main__":
    main()
