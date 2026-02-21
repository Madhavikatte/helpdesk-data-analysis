import pandas as pd
import pyodbc

conn=pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=localhost;"
    "DATABASE=HelpdeskDB;"
    "Trusted_Connection=yes;"
)

query = "SELECT * FROM tickets"

df = pd.read_sql(query, conn)

print(df.head())

# Most Common issue
print(df['issue_type'].value_counts())

#Average Resolution Time
print(df['resolution_time'].mean())

#Create Visualization
import matplotlib.pyplot as plt
import seaborn as sns

sns.countplot(x='priority', data=df)

plt.title("Tickets by Priority")

plt.show()