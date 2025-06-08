# Official Documentation
## Persona AI Chatbot
The persona AI Chatbot is nothing but a GPT model mimicking human behaviour of someone with the help of `SYSTEM_PROMPT` as context. In this application I have made an AI Persona . I am now going to guide you on how to make this project yourself. However, no explanation required concepts will be given.
## Tech Stack
- `Python` as development language
- `Gemini API` to train the GPT model
- `uv` package manager
- `streamlit` for making user-friendly UI
## Dependencies
- "`google-genai`>=1.18.0",
- "`pillow`>=11.2.1",
- "`python-dotenv`>=1.1.0",
- "`streamlit`>=1.45.1"
> Also don't forget to install "`python`>=3.13" for this project
## Project Structure
```
persona-ai-chatbot/
├── .venv               #where you store your api key
├── assets                         
├── .env
├── .gitignore
├── .python-version   
├── main.py             # Main source code
├── pyproject.toml      #contains project metadata
├── README.md
└── uv.lock             #similar to package-lock.json
```
## Project Build Guide
1. Project Initialization
    - Download **uv** package manager

    ```bash
    pip install uv
    ```
    - Check if uv is installed properly or not

    ```bash
    uv --version
    #Output
    #uv 0.7.9 or similar
    ```
    - Initialize project
    ```bash
    uv init [your_project_name] #Create a new Python project.
    ```
    This will create `.venv` and other important files like `pyproject.toml`
2. Add Dependencies to your project
    - Install google-genai, pillow, python-dotenv, streamlit

    ```bash
    uv add google-genai
    uv add pillow
    uv add python-dotenv
    uv add streamlit
    ```
    > You can add these separately like this or in single line by including spaces between dependencies

    >Also ensure python>=3.13 is also downloaded in your machine
3. Add your Gemini API key (or other)
    - Make a `.env` file

    ```bash
    touch .env
    ```
    - Store your API key inside .env

    ```.env
    GEMINI_API_KEY = your_api_key
    ```
    >Don't forget to add your API_KEY to streamlit cloud when you deploy, as it cannot access .env
4. Define your SYSTEM_PROMPT (prompt engineering)
    - This is where you define your persona
    - In this case I used data of of my friend
    - Ensure to declare Rules in your prompt settings
    - Give about 50-80 examples
    - Use the concept of zero-shot prompting
    - Write in plain english in details
    - Example

    ```python
    SYSTEM_PROMPT = """
        You are now a cat called neko. Your job is to reply meows in random order. etc.
    """
    ```
    Just update the `SYSTEM_PROMPT` to create your own persona
5. Streamlit App (main.py)
    - Visit `main.py` in added files
6. Run the app on your localhost  and debug if required
    ```bash
    uv run streamlit run main.py
    ```
    Visit: `http://localhost:8501`
7. Test my live app
    - [Persona AI chatbot]-(https://amisha.streamlit.app/)
8. Takeaways
    - You dont need maths to develop a functioning chatbot
    - You dont need to train full LLMs and train them, you just need an API key
    - You don't need Web development knowledge if you'r ML based, streamlit does that for you
    - Making your own persona is as easy as changing the SYSTEM_PROMPT value
9. License
    - This project is open source and available under the [MIT License](LICENSE).
10. Contributions
    - Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues).
11. Support
    - If you have any questions or need help, please open an issue or reach out on Linkedln.

Happy Coding!!!
