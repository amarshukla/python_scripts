# Given a world list and a character list, print all valid words which are possible using characters from the character list.

from collections import Counter 

def create_word(word_lst, char_lst):
  for word in word_lst: 
    # convert word into dictionary 
    my_dict = Counter(word)
    flag = 1
    for key in my_dict.keys():
      if key not in char_lst:
        flag = 0
    if flag:
      print(word, end=" ")

word_lst = ['amar','samsung','ericsson','icreon','sourcebits']
char_lst = ['e','r','i', 'a','m', 'c','s','o','n'] 
create_word(word_lst, char_lst)

# Output would be => amar ericsson icreon
