import os
from datetime import timedelta
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient
import pandas as pd

load_dotenv()

LOG_ANALYTICS_WORKSPACE_ID = os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID")
if not LOG_ANALYTICS_WORKSPACE_ID:
    raise SystemExit(
        "AZURE_LOG_ANALYTICS_WORKSPACE_ID is not set. Add it to your .env file.")

log_analytics_client = LogsQueryClient(credential=DefaultAzureCredential())

HOURS_AGO = 1

kql_query = '''
DeviceLogonEvents
| order by TimeGenerated desc
| take 10
| project TimeGenerated, AccountName, ActionType, DeviceName, RemoteIP
'''

response = log_analytics_client.query_workspace(
    workspace_id=LOG_ANALYTICS_WORKSPACE_ID,
    query=kql_query,
    timespan=timedelta(hours=HOURS_AGO)
)

table = response.tables[0]

if len(table.rows) == 0:
    raise SystemExit("No data returned from Log Analytics.")

columns = table.columns
rows = table.rows

df = pd.DataFrame(rows, columns=columns)
df["TimeGenerated"] = pd.to_datetime(
    df["TimeGenerated"]).dt.strftime('%Y-%m-%d %H:%M:%S.%f%z')

records = df.to_csv(index=False)

print(records)

print("fin.")
