import ollama
from saveinfo import create_file, copy_to_clipboard
from userinput import  remove_all_spaces

def summarize_info(text):
    print("It will take some times, please wait!")
    command = "Summarize main info of the text and keep it simple."
    stream = ollama.chat(
        model='llama3.1',
        messages=[{'role': 'user', 'content': f'''{text}. {command}'''}],
        stream=True,
    )
    final_text = ''''''
    for chunk in stream:
        final_text += chunk['message']['content']
        #print(chunk['message']['content'], end='', flush=True)

    print("The text is ready! ")
    return final_text