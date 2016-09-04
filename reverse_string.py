""" Reversing a string input """

string_input = raw_input('Which string would you like to reverse? ')
reversed_string = []
for i in string_input:
  reversed_string.append(i)
index = len(reversed_string)
for i in reversed_string:
  print reversed_string[index - 1],
  index = index - 1



