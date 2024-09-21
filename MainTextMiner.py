from weblinks import WebLinks
from messages import *
from validate import validate_url, validate_range_response, validate_int
from userinput import *

def main():
    while True:
        weblinks = WebLinks() #each time init will be again
        command = get_user_command()

        if command == "help":
            print_help_message()

        elif command == "google":
            range_results = input("How many links do you want to get? From 1 to 10. P.S You can only choose only one!:")
            weblinks.google_command(range_results)

        elif command == "paste_link":
            url = input("Paste your url:")
            weblinks.paste_link_command(url)

        elif command == "q":
            break
        else:
            print_command_does_not_exist(command)

if __name__ == "__main__":
    main()