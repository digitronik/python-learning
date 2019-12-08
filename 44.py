print('''Dear Alice,
    Eve's cat has been arrested for catnapping, cat burglary, and extortion.
    Sincerely,
    Bob''')
def spam():
     """This is a multiline comment to help
     explain what the spam() function does."""
print('Hello!')
def main():
    while True:
        print('Enter your age:')
        age = input()
        if age.isdecimal():
            break
        print('Please enter a number for your age.')
main()
def age():
    while True:
        print('Select a new password (letters and numbers only):')
        password = input()
        if password.isalnum():
            break
        print('Passwords can only have letters and numbers.')
age()