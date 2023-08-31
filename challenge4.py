# Write a program that reads a string from the input and checks if it is a palin-
# drome, which means it is the same whether it is read left-to-right or right-to-left.
# Example: ”abbccbba” is a palindrome, but ”ab” is not.


word = input("Enter a palindrome word: ")



char_list = []
rev_char_list = []

for chars in word:
    char_list.append(chars)


while len(word) != 0:
    index = -1
    rev_char_list.append(word[index]) 
    index -= 1

print(rev_char_list)



print(char_list)

