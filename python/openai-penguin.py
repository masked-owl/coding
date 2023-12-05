# ASCII art for a penguin and a log
penguin = """
    _
   (_)
    H
    H
    H
   _H_
 _/: :\_
/ : : : \
H : : : H
H : : : H
H : : : H
H : : : H
 HHHHHHH
"""

log = """
 /^^^^^^^\
|          |
|          |
|          |
 \________/
"""

# Print the initial scene
print(penguin)
print(log)

# Read a line of input from the user
input("Press enter to make the penguin jump over the log")

# Clear the screen and print the updated scene
print("\033[2J")  # ANSI escape code to clear the screen
print(log)
print(penguin)
