import sqlite3, pandas as pd
df=pd.read_csv('../data/cleaned_spacex_falcon9.csv')
con=sqlite3.connect('../data/spacex.sqlite')
df.to_sql('SPACEXTBL',con,if_exists='replace',index=False)
queries=[
"SELECT LaunchSite, COUNT(*) AS launches FROM SPACEXTBL GROUP BY LaunchSite ORDER BY launches DESC",
"SELECT LaunchSite, ROUND(AVG(Class)*100,1) AS success_rate_pct FROM SPACEXTBL GROUP BY LaunchSite ORDER BY success_rate_pct DESC",
"SELECT Year, COUNT(*) AS launches, ROUND(AVG(Class)*100,1) AS success_rate_pct FROM SPACEXTBL GROUP BY Year ORDER BY Year",
"SELECT Orbit, COUNT(*) AS launches, ROUND(AVG(Class)*100,1) AS success_rate_pct FROM SPACEXTBL GROUP BY Orbit ORDER BY success_rate_pct DESC"
]
for q in queries: print(pd.read_sql_query(q,con))
con.close()
