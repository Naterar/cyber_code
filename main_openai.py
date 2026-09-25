import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise SystemExit(
        "OPENAI_API_KEY is not set. Copy .env.example to .env and add your key.")

openai_client = OpenAI(api_key=api_key)

prompt = "Give me a very short recipe for a cake."

response = openai_client.chat.completions.create(
    model="gpt-4o-mini",  # swap for whatever the course uses
    messages=[{"role": "user", "content": prompt}],
)

answer = response.choices[0].message.content
print(f"\n{answer}\n")
