import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"system"
            "content":"give answer in two lines"
        }
        {
            "role": "user",
            "content": "you ar a python teacher.give me a definition of ai in 2 lines"
        }
    ]
)
print(response['message']['content'])