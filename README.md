Groq LLM Chatbot Demo
A lightweight terminal-based chatbot built using Groq’s LLaMA models and Python.
This project demonstrates how to integrate Groq’s high‑performance inference API into a simple conversational chatbot.

Features
Interactive chat loop (type exit to quit)

Uses llama‑3.1‑8b‑instant model from Groq

Secure API key handling using .env

Clean project structure (src/)

Beginner‑friendly code for learning LLM integration

Project Structure
Code
Demo_python/
│
├── src/
│   ├── demo_LLM_chatbot.py      # Main chatbot script
│   └── demo_env_print.py        # Environment variable test script
│
├── .gitignore                   # Prevents .env and venv from being committed
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
Installation
1. Clone the repository
Code
git clone https://github.com/VijayAIOps/Groq-llm-chatbot-demo.git
cd Groq-llm-chatbot-demo
2. Create a virtual environment
Code
python -m venv .venv
3. Activate the environment
Windows:

Code
.venv\Scripts\activate
4. Install dependencies
Code
pip install -r requirements.txt
5. Add your Groq API key
Create a .env file:

Code
api_key_value=YOUR_GROQ_API_KEY
Run the Chatbot
Code
python src/demo_LLM_chatbot.py
Example:

Code
You: What is Python?
Groq: Python is a high-level programming language...
You: exit
Chat ended.