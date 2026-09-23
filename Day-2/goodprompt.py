import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "what is ai and types of an ai and give examples give in 3 lines"
        }
    ]
) 
print(response["message"]["content"]) 