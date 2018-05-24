#!/usr/bin/env python
import sys

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

print(num_list)
numb = input('Enter the number in the list: ')
print(word_list)
word = input('Enter the word in the list: ')

last_num = len(num_list) - num_list[::-1].index(int(numb)) - 1
last_word = len(word_list) - word_list[::-1].index(word) - 1

print(last_num)
print(last_word)
