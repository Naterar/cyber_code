# cyber_code

Learning repo: building toward an AI-assisted security analysis tool.

## Setup

```bash
python -m venv venv
source venv/bin/activate
python -m pip install openai python-dotenv azure-identity azure-monitor-query pandas
cp .env.example .env   # then add your OpenAI key and Azure workspace ID to .env
```

## Run

```bash
python main_openai.py
```

Sends a prompt to OpenAI and parses the structured JSON response.

```bash
python log_analytics.py
```

Authenticates to Azure and queries Microsoft Defender telemetry
(`DeviceLogonEvents`) via KQL, using the Azure Monitor Query SDK. Confirmed
working against a live Log Analytics workspace, returning real logon event
data as CSV.

**Next:** feed a queried record into an LLM call so the model performs
triage on real telemetry instead of a placeholder example.

## Notes

- API keys and IDs live in `.env`, which is gitignored. Never commit a key or workspace ID.
- `.env.example` shows the variables required: `OPENAI_API_KEY`, `AZURE_LOG_ANALYTICS_WORKSPACE_ID`.
