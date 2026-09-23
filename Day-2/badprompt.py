import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "what is an AI in 3 lines"
        }
    ]
) 
print(response["message"]["content"]) 