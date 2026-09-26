import ollama
response = ollama.chat(
    model1="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": """
1.cat - Animal
2.Rose - Plant
3.Dog - """
        }
    ]
)