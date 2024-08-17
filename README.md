








<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



This is an SDK for an AI Chatbot. It's written with Flask/Python and is powered by Toolhouse. You can ask it a variety of things related to financial markets. You can also expand its capablities with the Toolhouse Tool Store.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With


* Python
* Toolhouse API
* HTML/CSS
* Flask Library
* OpenAI API
* Dotenv

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get up and running:
Clone this Rep. 

### Prerequisites

You'll need to install or set your venv to Python 3.12.5
You'll also need the [OpenAI API](https://platform.openai.com/api-keys) Keys and the [Toolhouse API keys](https://app.toolhouse.ai/settings/api-keys)

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API keys from above
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. PIP install requirements.text
   ```sh
   pip install requirements.txt
   ```
4. Enter your API tokens in `.env` file using the following format
   ```js
   TOOLHOUSE_API_KEY=
   OPENAI_API_KEY=
   ```
5. Run the file on your local machine
   ```sh
   run 'app.py'
   ```

6. Run the file on your local machine
   

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Sample app code:

``from flask import Flask, render_template, request, jsonify
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
    
    # Set the assistant's params as a financial advisor
    messages: List = [
        {"role": "system", "content": "You are a highly knowledgeable financial analyst."},
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

   ```


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments



