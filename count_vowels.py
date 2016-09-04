""" Count the number of vowels in a string """

string_input = raw_input('Enter a word or sentence: ')
string_input = string_input.lower()
string_lst = []
for i in string_input:
  string_lst.append(i)
count = 0
for i in string_lst:
  if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
    count += 1
print ('There are {0} vowels in the string \"{1}\"'.format(count,string_input))
