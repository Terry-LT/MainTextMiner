from trafilatura.downloads import PROXY_URL

from weblinks import WebLinks
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

        elif command == "paste_youtube":
            url = input("Paste your url:")
            weblinks.url = url
            weblinks.youtube_video()

        elif command == "my_text":
            print("WARNING: The text should fit in one line. Otherwise it will cause bags.")
            text = input("Put your text to summarize here:")
            weblinks.user_input_text(text)

        elif command == "q":
            break
        else:
            print_command_does_not_exist(command)

if __name__ == "__main__":
    main()