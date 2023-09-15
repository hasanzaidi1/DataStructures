from random import randrange as rand


def generate_rand_num(lowEnd, highEnd):
    randomNum = rand(lowEnd, highEnd)
    return randomNum

rand_num = generate_rand_num(12,22)
print(rand_num)
gues_num = 1
guess = int(input("Enter a number b/w 12 and 22: "))

while guess != rand_num:
    guess = int(input("Enter a number b/w 12 and 22: "))
    if guess == rand_num:
        print("Good Job")
        gues_num += 1
    else:
        gues_num += 1
        continue

print("you made total of guesses: ", gues_num)



