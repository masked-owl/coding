# Pebble Game
pebbles = 20

while pebbles > 0:
    # pebstr = str(pebbles)
    print("There are ", pebbles, " pebbles")
    remove = input('How many do you want to remove? ')
    pebbles = pebbles - int(remove)
    


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'Y', 'ye', 'yes', 'Yes', 'YES', 'yep', 'Yep', 'YEP'):
            return True
        if ok in ('n', 'N', 'no', 'No', 'NO', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

answer2 = ask_ok('Continue? ',2,'What?')
print(answer2)
