# cyber_code

Learning repo: building toward an AI-assisted security analysis tool.

## Setup

```bash
python -m venv venv
source venv/bin/activate
python -m pip install openai python-dotenv
cp .env.example .env   # then add your OpenAI key to .env
```

## Run

```bash
python main_openai.py
```

## Notes

- API keys live in `.env`, which is gitignored. Never commit a key.
- `.env.example` shows the variables required.
