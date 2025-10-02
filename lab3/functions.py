# task-1
# def grams_to_ounces(grams):
#     return 28.3495231 * grams
# print(grams_to_ounces(100))

# task-2
# def fahrenheit_to_celsius(f):
#     return (5 / 9) * (f - 32)
# f = float(input("Введите температуру: "))
# c = fahrenheit_to_celsius(f)
# print(f"{f}°F = {c:.2f}°C")

# task-3
# def solve(numheads, numlegs):
#     for chickens in range(numheads + 1):
#         rabbits = numheads - chickens
#         if 2 * chickens + 4 * rabbits == numlegs:
#             return chickens, rabbits
#     return None, None

# heads = 35
# legs = 94
# chickens, rabbits = solve(heads, legs)
# if chickens is not None:
#     print(f"Курицы: {chickens}, Кролики: {rabbits}")
# else:
#     print("Нет решения!")

# task-4
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def filter_prime(numbers):
#     return [x for x in numbers if is_prime(x)]


# nums = list(map(int, input("Введите числа через пробел: ").split()))
# primes = filter_prime(nums)
# print("Простые числа:", primes)

# task-5
# from itertools import permutations

# def string_permutations(s):
#     perms = [''.join(p) for p in permutations(s)]
#     return perms

# if __name__ == "__main__":
#     user_input = input("Введите строку: ")
#     result = string_permutations(user_input)
#     print("Все перестановки:")
#     for r in result:
#         print(r)

# task-6
# def reverse_sentence(sentence):
#     words = sentence.split()         
#     reversed_words = words[::-1]     
#     return " ".join(reversed_words)  

# if __name__ == "__main__":
#     user_input = input("Введите предложение: ")
#     result = reverse_sentence(user_input)
#     print("Результат:", result)

# task-7
# def has_33(nums):
#     for i in range(len(nums) - 1):   
#         if nums[i] == 3 and nums[i+1] == 3:
#             return True
#     return False

# print(has_33([1, 3, 3]))      
# print(has_33([1, 3, 1, 3]))   
# print(has_33([3, 1, 3]))      

# task-8
# def spy_game(nums):
#     code = [0, 0, 7]   
#     for n in nums:
#         if n == code[0]:   
#             code.pop(0)    
#         if not code:       
#             return True
#     return False

# print(spy_game([1,2,4,0,0,7,5]))  
# print(spy_game([1,0,2,4,0,5,7]))  
# print(spy_game([1,7,2,0,4,5,0])) 

# task-9
# def sphere_volume(r):
#     return (4/3) * 3,14 * (r ** 3)

# print(sphere_volume(1))   
# print(sphere_volume(3))  

# task-10
# def unique_list(lst):
#     result = []
#     for item in lst:
#         if item not in result:  
#             result.append(item)
#     return result

# print(unique_list([1, 2, 2, 3, 4, 4, 5]))   
# print(unique_list(["a", "b", "a", "c"]))    

# task-11
# def is_palindrome(s):
#     s = s.replace(" ", "").lower()
#     return s == s[::-1]

# print(is_palindrome("madam"))          
# print(is_palindrome("Madam"))          
# print(is_palindrome("nurses run"))     
# print(is_palindrome("hello"))          

# task-12
# def histogram(lst):
#     for num in lst:
#         print("*" * num)

# histogram([5, 9, 3])

# task-13
# import random

# def guess_game():
#     print("Hello! What is your name?")
#     name = input()

#     print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

#     number = random.randint(1, 20)  
#     guesses_taken = 0

#     while True:
#         print("Take a guess.")
#         guess = int(input())
#         guesses_taken += 1

#         if guess < number:
#             print("Your guess is too low.\n")
#         elif guess > number:
#             print("Your guess is too high.\n")
#         else:
#             print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
#             break

# guess_game()


