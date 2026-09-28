import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise SystemExit(
        "OPENAI_API_KEY is not set. Copy .env.example to .env and add your key.")

openai_client = OpenAI(api_key=api_key)

prompt = '''
Please describe a STIG in JSON format with the following fields:
- id
- title
- description
- severity
- status
- references
- remediation
- check
- fix
- notes
'''

response = openai_client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": prompt}],
    response_format={"type": "json_object"}
)

answer = response.choices[0].message.content
answer_dict = json.loads(answer)

# print(f"\n{answer}\n")

print(answer_dict["id"])
print(answer_dict["title"])
