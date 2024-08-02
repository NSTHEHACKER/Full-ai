import ollama

# text = 'how to enter the bank'

def fun(text):
    response = ollama.chat(model='moondream:latest', messages=[
        {
            'role': 'user',
            'content': text,
        },
    ])
    return response['message']['content']

print(fun('how much day in an year'))
