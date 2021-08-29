list1 = ["duck", "rabbit", "hare", "bear"]
list2 = ["plane", "helicopter", "jet", "car",]
list1.append(list2)
print(list1)

2
# number1 = int(input("Please enter in the first number: "))
# number2 = int(input("Please enter in the second number: "))
# number3 = int(input("Please enter in the third number: "))
# if (number1 >= number2) and (number1 >=number3):
#         print(f"The largest number is:{number1}")
# elif (number2 >= number1) and (number2 >= number3):
#         print(f"The largest number is:{number2}")
# elif (number3 >= number1) and (number3 >= number2):
#         print(f"The largest number is:{number3}")

3
import string
alphabet = list(string.ascii_lowercase)
for letter in alphabet:
    vowels = ["a", "e", "i", "o", "u"]
    if letter in vowels:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant")
4

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# user_names = input("Please enter in a name: ")
#
# if user_names in names:
#     print(names.index(user_names))

5

user_words1= input("Please enter in seven words:")
# words = user_words1.split(" ")
# words1 = list(words)
# print(words1)
# user_input1 = str(input("Please enter a letter to see if it is the words: "))
for word in user_words1:
    user_input1 = str(input("Please enter a leter to see if it is the words: "))
    if user_input1 in user_words1:
        print (user_words1.index(user_input1))
        break
    else:
        print(f"The letter that you chose {user_input1} is not in one of the words")
        break


