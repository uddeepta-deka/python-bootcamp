"""
We will talk about errors, exceptions
"""

# KeyError
# dict = {"key" : "value"}
# dict["non_existent_key"]

# FileNorFoundError
# with open("filename.txt", "r") as f:
#     f.read()

# IndexError
# arr = [1, 2, 3]
# print(arr[3])

# TypeError
# print("abc" + 13)

"""
In order to get rid of these type of errors we usually use the following keywords
try : something that might cause an exception
except : Do this is there WAS an exception
else : Do this if there were NO exception
finally : Do this no matter what happens 
"""

# Dealing with the errors
# try:
#     file = open("filename.txt")
#     a_dictionary = {"key": "Value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("filename.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} doesn't exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed")
#     raise TypeError("This is an error that I made up")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 metres.")
bmi = weight / height / height
print(bmi)