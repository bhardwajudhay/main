# Q1
# str = input("Enter a string: ")
#         print("Length of the input string is:", len(str))


# # Q2
# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('google.com'))


# Q3
# mystr = "hello"
# if len(mystr) > 1:
#     print(mystr[:2] + mystr[-2:])
# else:
#     print("empty string")
#
# a = "hello"
# b = {}
# for i in a:
#     if i in b:
#         b[i] += 1
#     else:
#         b[i] = 1
# print(a, str(b))





# Q4
# mystr = "hello"
# x = mystr.replace("e", "$")
# print(x)


# Q5
# def charsmixup(a, b):
#   new_a = b[:2] + a[2:]
#   new_b = a[:2] + b[2:]
#   return new_a + ' ' + new_b
# print(charsmixup('abc', 'xyz'))

# Q6
# def add_string(str1):
#   length = len(str1)
#   if length > 2:
#     if str1[-3:] == 'ing':
#       str1 += 'ly'
#     else:
#       str1 += 'ing'
#   return str1
# print(add_string('ab'))
# print(add_string('abc'))
# print(add_string('string'))


#7
# def not_poor(str1):
#   snot = str1.find('not')
#   spoor = str1.find('poor')
#
#   if spoor > snot and snot > 0 and spoor > 0:
#     str1 = str1.replace(str1[snot:(spoor + 4)], 'good')
#     return str1
#   else:
#     return str1
#
#
# print(not_poor('The lyrics is not that poor!'))
# print(not_poor('The lyrics is poor!'))


# Q8
# def find_longest_word(words_list):
#   word_len = []
#   for n in words_list:
#     word_len.append((len(n), n))
#   word_len.sort()
#   return word_len[-1][0], word_len[-1][1]
#
#
# result = find_longest_word(["PHP", "Exercises", "Backend"])
# print("\nLongest word: ", result[1])
# print("Length of the longest word: ", result[0])



#Q9th
# def remove_char(str, n):
#   first_part = str[:n]
#   last_part = str[n + 1:]
#   return first_part + last_part
#
#
# print(remove_char('Python', 0))
# print(remove_char('Python', 3))
# print(remove_char('Python', 5))


# Q10th
# def change_sring(str1):
#   return str1[-1:] + str1[1:-1] + str1[:1]
#
# print(change_sring('abcd'))
# print(change_sring('12345'))

# Q11
# def odd_values_string(str):
#   result = ""
#   for i in range(len(str)):
#     if i % 2 == 0:
#       result = result + str[i]
#   return result
# print(odd_values_string('abcdef'))
# print(odd_values_string('python'))

# Q12
# def word_count(str):
#     counts = dict()
#     words = str.split()
#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#     return counts
# print( word_count('the quick brown fox jumps over the lazy dog.'))

# Q13
# user_input = input("What's your favourite language? ")
# print("My favourite language is ", user_input.upper())
# print("My favourite language is ", user_input.lower())

# Q14
# items = input("Input comma separated sequence of words")
# words = [word for word in items.split(",")]
# print(",".join(sorted(list(set(words)))))

# Q15
# def add_tags(tag, word):
# 	return "<%s>%s</%s>" % (tag, word, tag)
# print(add_tags('i', 'Python'))
# print(add_tags('b', 'Python Tutorial'))

# Q16
# def insert_sting_middle(str, word):
# 	return str[:2] + word + str[2:]
#
# print(insert_sting_middle('[[]]', 'Python'))
# print(insert_sting_middle('{{}}', 'PHP'))
# print(insert_sting_middle('<<>>', 'HTML'))

# Q17
# def insert_end(str):
# 	sub_str = str[-2:]
# 	return sub_str * 4
#
# print(insert_end('Python'))
# print(insert_end('Exercises'))

# Q18
# def first_three(str):
# 	return str[:3] if len(str) > 3 else str
#
# print(first_three('ipy'))
# print(first_three('python'))
# print(first_three('py'))

# Q19
# str1 = 'https://www.w3resource.com/python-exercises/string'
# print(str1.rsplit('/', 1)[0])
# print(str1.rsplit('-', 1)[0])

# Q20
# def reverse_string(str1):
#     if len(str1) % 4 == 0:
#        return ''.join(reversed(str1))
#     return str1
# print(reverse_string('abcd'))
# print(reverse_string('python'))

# Q21
# def to_uppercase(str1):
#     num_upper = 0
#     for letter in str1[:4]:
#         if letter.upper() == letter:
#             num_upper += 1
#     if num_upper >= 2:
#         return str1.upper()
#     return str1
# print(to_uppercase('Python'))
# print(to_uppercase('PyThon'))

# Q22
# str1='Python\n Exercises\n'
# print(str1)
# print(str1.rstrip())


# Q23
# string = "udhay bhardwaj"
# print(string.startswith("ud"))