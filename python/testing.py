# This is a test program
print('hello')
mylist = [1,2,3,4,5]
bob = [1,2,4]
print (bob[1])

def fib(end):
    a, b = 0, 1
    while a < end:
        print(a)
        a, b = b, a+b

myanswer = input('Type Something: ') # Comment
print(myanswer)
for x in [1,2,3]:
    print(x)

print()
fib(25)


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
