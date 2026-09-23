import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"system"
            "content":"i want to teach it to a 5years old kid give me the answer"
        }
        {
            "role": "user",
            "content": "explain ai"
        }
    ]
)
print(response['message']['content'])