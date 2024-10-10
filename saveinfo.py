from cgitb import reset
import sys
from validate import *
import pyperclip
from messages import  *
from userinput import remove_all_spaces

def copy_to_clipboard(text):
    try:
        pyperclip.copy(text)
        print("Text copied to clipboard!")
    except Exception as e:
        print(f"Failed to copy text: {e}")
def create_file(text):
    formats_dict = {
        1: "html",
        2: "txt"
    }
    print(formats_dict)
    number = input(
        "Choose number of file format. P.S if you wrote a number of out of range, it will automatically copy text to clipboard:")
    if validate_int(number):
        number = int(number)
        if (0 < number) and (number <= formats_dict.__len__()):

            format_name = formats_dict[number]
            with open(f"text_from_website.{format_name}", "w", encoding="utf-8") as text_file_main_text_miner:
                if format_name == 'html':
                    template = f'''
                               <!DOCTYPE html>
                               <html>
                               <head>
                               <title>Page Title</title>
                               </head>
                               <body>
                               <h1>Text</h1>
                               <p>{text}</p>
                               </body>
                               </html>
                               '''
                    text_file_main_text_miner.write(template)
                else:
                    text_file_main_text_miner.write(text)
            print("The file was created!")
            print("Goodbye!")
            sys.exit() # in order to save a file
        else:
            print_out_of_range()
    else:
        copy_to_clipboard(text)

def copy_or_create_choice(text):
    choose = input(
        "Do you want to copy text to clipboard or save as a file? Type +(text to clipboard) -(save as a file)")
    if remove_all_spaces(choose) == "+":
        copy_to_clipboard(text)
    else:
        create_file(text)