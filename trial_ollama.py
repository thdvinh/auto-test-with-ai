import ollama


response = ollama.chat(
            model='llama3.2:3b',
            messages=[{'role': 'user', 'content': 'what is the capital of France?'}],
            # temperature=0.7,
        )

print(response.message)