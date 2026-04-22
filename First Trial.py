# from contextlib import nullcontext
#
# name = 'Rohit'
# age = 23
#
# print("My name is {age} and age is {name}",name,age,end = None)
#
# print("wow this is crazy")
#
# range_ex = range(4,10,3)
#
# print(list(range_ex)[0:0])
#
# print(age//2)
#
# value = 1
# if value is None:
#     print("The value is None.")
# import time
import string

# example_for_lower = "hell is this 12"
# print(example_for_lower.islower())
#
#
# a = int(input())
# b = input(int())
# c = int()
# print(a,b,c)
# print(type(a), type(b), type(c))

#
# if 18 > int(time.strftime('%H')) > 12:
#     print("Good Afternoon")
# elif 6 < int(time.strftime('%H')) < 12:
#     print("Good Morning")
# elif 18 < int(time.strftime('%H')) < 23:
#     print("Good Evening")

# while True:
#     a = float(input('Enter First Number: '))
#     b = float(input('Enter Second Number: '))
#
#     print(max(a,b))
#     if a==b:
#         break


# def max_n(a = 100, b = 200):
#     return max(a, b)
#
# print(max_n(23,233))


# new_list = list_of_no_1+list_of_no_2
# print(new_list)

# list_of_no_1 = [3, 6, 8, 5]
# list_of_no_2 = [4, 9, 2]
# #
# print(list_of_no_2[:1])
# print(list_of_no_2)
# new_list = []
# new_num = 0
# for i in range(0,(len(max(list_of_no_1,list_of_no_2)))):
#     new_num = list_of_no_1[i]*list_of_no_2[i]
#     new_list.append(new_num)
#
# print(new_list)




# tup_1 = (34, 435, 65, 35, 658, 90)
# print(tup_1[2:4])
#
# tup_list = list(tup_1)
# print(tup_list[1:3])
#
# print(tup_list)
# print(tup_1)



# import this


# list_tobe_set = [1214, 46, 567, True, "nsoinc", 46]
# set_data = set(list_tobe_set)
# print(set_data)

# print(set_data[1])
# set_data_to_be_merge = {1232, 46458, 2358, False, 567}
# set_data.update(set_data_to_be_merge)
# print(set_data)

# num = input("Enter any value between 3-9 to run the program again: ")
#
# if num == "quit":
#     print("Good Work")
#
# elif 3 <= int(num) <= 9:
#     print("That's Good")
# elif 3 >= int(num) >= 9:
#     raise ValueError("Value is not valid")
#
# else:
#     raise NameError("That's Not Right")

########################Quiz Game#########################################
# list_of_questions = [" Which of the three banks will be merged with the other two to create India’s third-largest bank?",
#                      " What is the name of the weak zone of the earth’s crust?"]
#
# dict_of_opt_available = {0:["A. Punjab National Bank", "B. Indian Bank", "C. Bank of Baroda", "D. Dena Bank"],
#                          1:["A. Seismic", "B. Cosmic", "C. Formic", "D. Anaemic"],}
#
# list_of_ans = ["b", "a"]
#
# score = 0
#
# new_opt_list = []
# for i in range(0,len(list_of_questions)):
#
#     print(list_of_questions[i])
#
#     new_opt_list = dict_of_opt_available.pop(i)
#
#     for j in range(0,4):
#         print(new_opt_list[j])
#
#     user_ans = input("Enter your answer as a, b, c or d: ")
#
#     if user_ans.lower() == list_of_ans[i]:
#         score += 1
#         print("You're Correct")
#     else:
#         print("You're Wrong")
#
# print(f"Congratulations!!! You have finished the game with score {score}")


############################################# Program for the Secret Language #########################################################
# import random
# letters = list(string.ascii_letters)
# secret_message = input("Enter the Message that you want to Convert to Secret Language: ")
# msg_to_be = int(input("Enter 1 to encode or 2 to decode: "))
# secret_message_list = secret_message.split(' ')
#
#
#
#
# def rand_prefix_suffix():
#     rand_combo = "".join([random.choice(letters) for i in range(3)])
#     return rand_combo
#
# def encoding_message(secret_message_lis):
#     encoded_msg_list = []
#     encoded_msg = ""
#     for word in secret_message_lis:
#         new_msg_list = []
#         letter_of_word = []
#         if len(word) >= 3:
#             letter_of_word = list(word)
#             first_letter = letter_of_word.pop(0)
#             letter_of_word.append(first_letter)
#             puzzled_word = "".join(letter_of_word)
#             encoded_word = rand_prefix_suffix() + puzzled_word + rand_prefix_suffix()
#         else:
#             encoded_word = word[::-1]
#
#         encoded_msg_list.append(encoded_word)
#         encoded_msg = " ".join(encoded_msg_list)
#
#     return encoded_msg
#
# def decoding_message(secret_message_lis):
#     decoded_msg_list = []
#     decoded_msg = ""
#     for word in secret_message_lis:
#         new_msg_list = []
#         letter_of_word = []
#         if len(word) >= 3:
#             letter_of_word = list(word)
#             puzzled_word = letter_of_word[3:-3]
#             f_letter = puzzled_word.pop()
#             decoded_word = f_letter + "".join(puzzled_word)
#         else:
#             decoded_word = word[::-1]
#
#         decoded_msg_list.append(decoded_word)
#         decoded_msg = " ".join(decoded_msg_list)
#
#     return decoded_msg
#
# if msg_to_be == 1:
#     print(encoding_message(secret_message_list))
#
# elif msg_to_be == 2:
#     print(decoding_message(secret_message_list))


# report = {"Technical": 0, "Billing": 0, "General": 0}
# tickets = [
#     {"id": 101, "issue": "My password is not working and I cannot login"},
#     {"id": 102, "issue": "I was overcharged for my last subscription"},
#     {"id": 103, "issue": "How do I change my profile picture?"},
#     {"id": 104, "issue": "The website is crashing when I click pay"},
#     {"id": 105, "issue": "While login to pay the amount I am getting error"}
# ]
#
# category_keywords = {
#     "Technical": ["password", "login", "crashing", "website"],
#     "Billing": ["overcharged", "subscription", "pay", "invoice"]
# }
#
#
# for ticket in tickets:
#
#     ticket["category"] = "General"
#
#
#     for category, keywords in category_keywords.items():
#         for word in keywords:
#
#             if word in ticket["issue"].lower():
#                 ticket["category"] = category
#                 break
#
#     current_cat = ticket["category"]
#     report[current_cat] += 1
#
# for t in tickets:
#     print(f"Ticket ID {t['id']} is categorized as: {t['category']}")


# import pandas as pd
# import numpy as np

# data = {
#     "ticket_id": [101, 102, 103, 104, 105],
#     "issue": [
#         "My password is not working",
#         "I was overcharged for my last subscription",
#         "How do I change my profile picture?",
#         "The website is crashing",
#         np.nan
#     ]
# }
#
# df = pd.DataFrame(data)
#
#
# print(df.isnull().sum())



## Imagine we added a 'category' column to our 'df'
# df['category'] = ['Technical', 'Billing', 'General', 'Technical']

## What will this line produce?
# print(df['issue'].describe())


# logins = [8.0, 9.5, np.nan, 8.5, 10.0, np.nan]

# df = pd.DataFrame(logins)
#
# print(df.isnull().sum())
#
#
# df = df.replace(np.nan, df.mean())
#
# print(df)
#
# import matplotlib.pyplot as plt
#
# days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
# logins = [8.0, 9.5, 8.7, 8.5, 10.0, 9.0]
#
# plt.plot(days, logins, marker='h', color='green', linestyle='')
#
#
# plt.title('Employee Login Trends Over a Week')
# plt.xlabel('Days of the Week')
# plt.ylabel('Login Time (AM)')
#
# plt.show()

# import pandas as pd
# import openpyxl as op
# # Read the first sheet
# df = pd.read_excel(C:\Different Folder\Code\python\Scrapping the Data\Book1.xlsx)
#
# print(df.head())

# Basic read
# df = pd.read_csv('C:\Different Folder\Code\python\Scrapping the Data\Book1.csv')
# def func_to_print(file_path):
#     de = pd.read_excel(file_path)
#     return de
# print(func_to_print("Book1.xlsx"))
# print(df)







