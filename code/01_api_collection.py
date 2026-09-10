import requests, pandas as pd
BASE='https://api.spacexdata.com/v4'
# Example pipeline: collect launches, rockets, payloads, launchpads, then normalize.
launches=requests.get(f'{BASE}/launches/past',timeout=30).json()
df=pd.json_normalize(launches)
falcon9=df[df['rocket'].notna()].copy()
falcon9.to_csv('../data/api_raw_launches.csv',index=False)
print('Collected',len(falcon9),'historical launch records')
