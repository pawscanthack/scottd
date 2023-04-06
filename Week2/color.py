#!/usr/bin/python3
# A script that will prompt for a user name and then for their favorite color then print out

# Versioning
# SDavis-20230406: initial version

# Set up initial variables and imports


# Main routine that is called when script is run
def main():
    username = get_username()
    favcolor = get_favcolor()
    display_userinfo(username, favcolor)

# Subroutines

"""Function prompts user for input and returns username"""
def get_username():
      return input("\nWhat is your name?\n")

"""Function prompts user for input and returns favorite color"""
def get_favcolor():
      return input("\nWhat is your favorite color?\n")

"""Function displays user info"""
def display_userinfo(name, color):
      print(f'\nThe favorite color for {name} is {color}.')

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()
