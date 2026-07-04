"""This is First demo to create an LLM using groq API and python.this acts as chat bot
Author:Vijayalakshmi
Date:2026-07-04
"""
"""
This is First demo to create an LLM using Groq API and Python.
Author: Vijayalakshmi
Date: 2026-07-04
"""

import os
from groq import Groq
from dotenv import load_dotenv

def main():
    load_dotenv()
    print("hai..")

    api_key = os.getenv("api_key_value")
    print("post key...")

    if not api_key:
        raise ValueError("Groq API key is not set. Please add it to your .env variables")

    client = Groq(api_key=api_key)

    model = "llama-3.1-8b-instant"
    while True:
        user_input = input("you: ")
        if user_input.lower() == "exit":
            break
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user",  "content": user_input}
                                                            
            ]
        )
        print(response.choices[0].message.content)    
    
if __name__ == "__main__":
    main()

       



