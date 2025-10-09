# # 1
# def gen_sq(n):
#     for i in range(n+1):
#         yield i*i

# for x in gen_sq(5):
#     print(x, end=" ")

# # 2
# def evens(n):
#     for i in range(n+1):
#         if i%2==0:
#             yield i

# n=int(input())
# print(",".join(str(i) for i in evens(n)))

# # 3
# def div_3_4(n):
#     for i in range(n+1):
#         if i%3==0 and i%4==0:
#             yield i

# n=int(input())
# for x in div_3_4(n):
#     print(x, end=" ")

# # 4
# def squares(a,b):
#     for i in range(a,b+1):
#         yield i*i

# for x in squares(2,5):
#     print(x, end= " ")

# #5
# def down(n):
#     while n>=0:
#         yield n
#         n-=1

# for x in down(5):
#     print(x, end=" ")
