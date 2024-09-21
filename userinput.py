import os
import  re
from validate import  *


def get_windows_username():
    return os.getlogin() + "@:"

def remove_all_spaces(text):
    return re.sub(r"\s+", "", text, flags=re.UNICODE)

def get_user_command():
    command = input(f"{get_windows_username()}")
    return remove_all_spaces(command)

