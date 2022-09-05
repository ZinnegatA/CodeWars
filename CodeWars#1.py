# 1
# def spin_words(sentence):
#     words = [word for word in sentence.split()]
#     words = [word if len(word) < 5 else word[::-1] for word in words]
#     return " ".join(words)
#
#
# print(spin_words("Stop gninnipS My sdroW!"))

# 2
# def find_uniq(arr):
#     s = set(arr)
#     for e in s:
#         if arr.count(e) == 1:
#             return e
#
#
# print(find_uniq([1, 1, 1, 2, 1, 1]))

# 3
# def lovefunc(f1, f2):
#     return len(list(filter(lambda x: x % 2 == 0, (f1, f2)))) < 2
#
#
# print(lovefunc(2, 4))

# 4
# def convert(array):
#     return list(i for i in array[::-1])
#
#
# print(convert('348597'))

# 5
# def isogram(word):
#     return len(set(word.lower())) == len(word)
#
#
# print(isogram('Dermatoglyphics'))

# 6
# def solution(number):
#     return sum([num for num in range(3, number) if num % 3 == 0 or num % 5 == 0]) if number > 0 else 0
#
#
# print(solution(int(input())))

# 7
# def two_sum(numbers, target):
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             if numbers[i] + numbers[j] == target:
#                 return i, j
#
#
# print(two_sum([1, 2, 3], 4))

# 8
# def pig_it(text):
#     result = ''
#     for word in text.split():
#         if word.isalpha():
#             result += word[1:] + word[0] + 'ay '
#         else:
#             result += word
#     return result.rstrip()

# 9
# def first_non_repeating_letter(string):
#     res = ''
#     for l in string:
#         if string.lower().count(l.lower()) == 1:
#             res += l
#             return res
#
#
# print(first_non_repeating_letter('sTreSS'))

# 10
# def title_case(title, minor_words=''):
#     title = title.capitalize().split()
#     minor_words = minor_words.lower().split()
#     return ' '.join([word if word in minor_words else word.capitalize() for word in title])
#
#
# print(title_case('THE WIND IN THE WILLOWS', 'The In'))
