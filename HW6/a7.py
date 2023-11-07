"""
File: a7.py

"""

from stack import Stack

def isPalindrome(sentence):          
    """Returns True if sentence is a palindrome
    or False otherwise."""
    stk = Stack() 

    sentence = sentence.lower()

    for char in sentence:
        if char != ' ':
            stk.push(char)

    for char in sentence:
        if char != ' ':
            if char != stk.pop():
                return False
    
    return True


# *** Do not modify main() ***
def main():
    while True:
        sentence = input("Enter some text or just hit Enter to quit: ")
        if sentence == "":
            break
        elif isPalindrome(sentence):
            print("It's a palindrome.")
        else:
            print("It's not a palindrome.")

main()
