import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "what is ai explain in 6 lines and also explain different types of ai"
        }
    ]
)
print(response['message']['content'])