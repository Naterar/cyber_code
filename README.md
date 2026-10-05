# cyber_code

Learning repo: building toward an AI-assisted security analysis tool.

## Setup

```bash
python -m venv venv
source venv/bin/activate
python -m pip install python-dotenv azure-identity azure-monitor-query pandas
cp .env.example .env   # then add your Azure workspace ID to .env
```

You also need to be signed in to Azure (for example with the Azure CLI) so `DefaultAzureCredential` can find your login.

## Run

```bash
python log_analytics.py
```

`log_analytics.py` authenticates to Azure and queries Microsoft Defender
telemetry (`DeviceLogonEvents`) via KQL, using the Azure Monitor Query SDK.
Results are sorted most-recent-first, limited to the fields that matter
(time, account, action, device, source IP), and timestamps are formatted
with microsecond precision and UTC offset for forensic accuracy. Confirmed
working against a live Log Analytics workspace, returning real logon data
as CSV.

**Next:** summarize the queried events (for example, failed logons grouped by
source IP) and feed that summary to an LLM so the model performs triage on
real telemetry instead of a placeholder example. This will use the OpenAI
API, so `openai` gets installed and `OPENAI_API_KEY` gets used at that step.

## Notes

- API keys and IDs live in `.env`, which is gitignored. Never commit a key or workspace ID.
- `.env.example` shows the variables: `AZURE_LOG_ANALYTICS_WORKSPACE_ID` (used now) and `OPENAI_API_KEY` (for the LLM step).
