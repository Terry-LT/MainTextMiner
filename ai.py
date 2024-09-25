import ollama

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

def describe_image():
    pass