import os
import  re

def get_windows_username():
    return os.getlogin() + "@:"

def remove_all_spaces(text):
    return re.sub(r"\s+", "", text, flags=re.UNICODE)