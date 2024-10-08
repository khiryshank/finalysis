from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from toolhouse import Toolhouse
from openai import OpenAI
from typing import List

# Load environment variables
load_dotenv()

# Initialize OpenAI and Toolhouse clients
client = OpenAI()
tools = Toolhouse()

# Set metadata for Toolhouse (e.g., timezone)
tools.set_metadata("timezone", -7)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    
    system_prompt_content = """
You are an AI agent designed to synthesize information about the stock market and investing. You should respond with a concise answer that only answers the exact question the user asked. Your responses should be helpful and capture all the important information you have access to. Include all references in a separate section after your answer.
"""
    # Set the assistant's params as a financial advisor
    messages: List = [
        {"role": "system", "content":  system_prompt_content},
        {"role": "user", "content": user_input}
    ]

    # First API call to OpenAI using GPT-4o
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=messages,
        tools=tools.get_tools(),
        tool_choice="auto"
    )

    # Run tools and update messages
    messages += tools.run_tools(response)

    # Second API call to OpenAI using GPT-4o-mini
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools.get_tools(),
        tool_choice="auto"
    )

    # Extract and return the response content
    chatgpt_reply = response.choices[0].message.content

    return jsonify({'reply': chatgpt_reply})

if __name__ == '__main__':
    app.run(debug=True)
