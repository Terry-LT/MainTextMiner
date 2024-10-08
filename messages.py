def print_help_message():
    print('''
    The available commands: google, paste_link, paste_youtube, my_text, q
    ''')

def print_command_does_not_exist(command):
    print(f"The command '{command}' does not exist! Write 'help' to get all available commands.")

def print_out_of_range():
    print("The number is out of range!")

def print_must_be_int():
    print("Must be number!")

def print_main_text(text):
    print("")
    print("Wait...")
    print("")
    print(f"Result: {text}")

def print_url_not_valid():
    print("The url is not valid!")

def print_ai_should_be_on_conf():
    print("You can use  this function only with AI.")
    print("Change setting in confing, then reopen this app.")