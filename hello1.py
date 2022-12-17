from termcolor import colored, cprint

# comments - Print "hello, world!" to the terminal 
print('Hello, World!')

text = colored("Hello, World!", "red")
print(text)
cprint("Hello, World!", "green", "on_red")

