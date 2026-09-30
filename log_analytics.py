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

hours_ago = 1

kql_query = f'''
DeviceLogonEvents
| take 10
'''

response = log_analytics_client.query_workspace(
    workspace_id=LOG_ANALYTICS_WORKSPACE_ID,
    query=kql_query,
    timespan=timedelta(hours=hours_ago)
)

table = response.tables[0]

if len(response.tables[0].rows) == 0:
    print("No data returned from Log Analytics.")
    exit

record_count = len(response.tables[0].rows)

columns = table.columns
rows = table.rows

df = pd.DataFrame(rows, columns=columns)
records = df.to_csv(index=False)

print(records)

print("fin.")
