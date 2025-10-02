import math
import random

# 1. Проверка палиндрома
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# 2. Гистограмма
def histogram(lst):
    for num in lst:
        print("*" * num)

# 3. Объем сферы
def sphere_volume(r):
    return (4/3) * math.pi * (r ** 3)

# 4. Фильтр простых чисел
def filter_prime(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return [x for x in lst if is_prime(x)]

# 5. Игра "Угадай число"
def guess_game():
    print("Hello! What is your name?")
    name = input()
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < number:
            print("Your guess is too low.\n")
        elif guess > number:
            print("Your guess is too high.\n")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break