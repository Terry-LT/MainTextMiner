from weblinks import WebLinks
from messages import *
from validate import validate_url, validate_range_response, validate_int
from userinput import *

#TODO: Upload to github
#TODO: To exe file

def main():
    while True:
        weblinks = WebLinks() #each time init will be again
        command = input(f"{get_windows_username()}")
        command = remove_all_spaces(command)

        if command == "help":
            print_help_message()
        elif command == "google":
            range_results = input("How many links do you want to get? From 1 to 10. P.S You can only choose only one!:")
            if validate_range_response(range_results):
                # Save range
                weblinks.range_results = int(range_results)
                search_input  = input("What do you want to search?:")
                weblinks.info_to_search = search_input
                links = weblinks.get_web_links()
                number_of_order = input("Choose number:")
                if validate_int(number_of_order):
                    weblinks.set_url(number_of_order)
                    weblinks.save_text()
                else:
                    print_must_be_int()
        elif command == "paste_link":
            url = input("Paste your url:")
            if validate_url(url):
                weblinks.url = url
                weblinks.save_text()

        elif command == "q":
            break
        else:
            print_command_does_not_exist(command)

if __name__ == "__main__":
    main()