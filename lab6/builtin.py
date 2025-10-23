
# from functools import reduce
# import math
# import time

# #1
# nums = [2, 4, 6, 7, 5]
# result = reduce(lambda x, y: x*y ,nums)
# print(result)

# #2
# str = input()
# sumup = sum(1 for x in str if x.isupper())
# sumlow = sum(1 for x in str if x.islower())
# print("low: ", sumlow, "," , "up: ", sumup)

# #3
# str = input()
# ispulin = str == "".join(reversed(str))
# print(ispulin)

# #4
# num = 25100
# ms = 2123
# time.sleep(ms/1000)
# result = math.sqrt(num)
# print(f"Square root of {num} after {ms} miliseconds is {result}")

# #5
# tup1 = (True, True, 1)
# tup2 = (True, False, 1)
# print(all(tup1))
# print(all(tup2))

