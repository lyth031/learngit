begin = 0
end = 100
ans = (begin + end) / 2

print("Please think of a number between 0 and 100!")
print("Is your secret number %d?" % ans)

c = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate \
the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while c != 'c':
    while not(c == 'h' or c == 'l' or c == 'c'):
        print("Sorry, I did not understand your input.")
        print("Is your secret number %d?" % ans)
        c = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate \
the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if c == 'c':
        pass
    else:
        if c == 'h':
            end = ans
        else:
            begin = ans
        ans = (begin + end) / 2
        print("Is your secret number %d?" % ans)
        c = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate \
the guess is too low. Enter 'c' to indicate I guessed correctly. ")

print("Game over. Your secret number was: %d" % ans)
print("Let's go!")
