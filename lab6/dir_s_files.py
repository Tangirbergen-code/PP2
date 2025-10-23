# #1
# import os

# path = input("Enter the path: ")

# print("Directories:")
# for item in os.listdir(path):
#     if os.path.isdir(os.path.join(path, item)):
#         print(item)

# print("Files:")
# for item in os.listdir(path):
#     if os.path.isfile(os.path.join(path, item)):
#         print(item)

# print("All directories and files:")
# for item in os.listdir(path):
#     print(item)

# #2
# import os

# path = input("Enter the path: ")

# print(f"\nChecking access for: {path}")
# print("Exists:", os.path.exists(path))

# print("Readable:", os.access(path, os.R_OK))
# print("Writable:", os.access(path, os.W_OK))
# print("Executable:", os.access(path, os.X_OK))

# #3
# import os

# path = input("Enter the path: ")

# if os.path.exists(path):
#     filename = os.path.basename(path)
#     print("File name:", filename)

#     directory = os.path.dirname(path)
#     print("Directory:", directory)

# else:
#     print("The specified path does not exist.")

# #4
# filename = input("Enter the filename: ")

# opening = open(filename, 'r')
# lines = opening.readlines()  
# print("Number of lines in the file:", len(lines))
# opening.close()

# #5
# my_list = ["Yeldar", "Tima", "Nurali"]
# filename = input("Enter the filename: ")

# opening = open(filename, 'w')
# for i in my_list:
#     opening.write(i)
# opening.close()

# #6
# n = 26
# word = "A"
# for i in range(n):
#     filename = f"{(chr(ord('A') + i))}.txt"
#     file = open(filename, 'w')
#     file.write(f"this is file {filename}\n")
#     file.close()

# #7
# filename1 = input("Enter file 1: ")
# filename2 = input("Enter file 2: ")

# file_1 = open(filename1, 'r')
# file_2 = open(filename2, 'w')

# content = file_1.read()
# file_2.write(content)

# file_1.close()
# file_2.close()

# #8
# import os

# path = input("Enter the path to delete: ")

# if os.path.exists(path):
#     print("File exists")

#     if os.access(path, os.W_OK):
#         os.remove(path)  
#         print("File deleted successfully")
#     else:
#         print("You don't have permission to delete this file")
# else:
#     print("The specified path does not exist")