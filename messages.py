def print_help_message():
    print('''
    The available commands: google, paste_link, q
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