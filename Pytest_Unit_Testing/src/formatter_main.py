import sys
import formatter

user_input = int(input("Enter an integer: "))
if isinstance( user_input, int):
    try:
        formatted_size = formatter.format_file_size(user_input)
        print(formatted_size)
    except ValueError:
        print("Please provide a valid file size in bytes as a command-line argument.")
else:
    print("Please provide the file size in bytes as a command-line argument.")