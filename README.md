# Research-GPT
A CLI research assistant that helps you find and summarize information from arXiv, wikipedia, DuckDuckGo, and summarize it using OpenRouter's API.

# Installation and Usage
To set up and run the Research-GPT project, follow these steps:
1. Clone the repository:
```bash
git clone https://github.com/Armxyz1/research-gpt
```

2. Navigate to the project directory:
```bash
cd research-gpt
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your environment variables:
- Copy the `.env.example` file to `.env`:
```bash
cp .env.example .env
```
- Open the `.env` file and set your `OPENROUTER_API_KEY`, `SITE_URL`, and `SITE_NAME`.

5. Run the application:
```bash
python cli.py
```

