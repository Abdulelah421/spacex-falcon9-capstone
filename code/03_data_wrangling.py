import pandas as pd, numpy as np
df=pd.read_csv('../data/spacex_falcon9_historical.csv')
df['Date']=pd.to_datetime(df['Date'])
df['Year']=df['Date'].dt.year
for c in ['GridFins','Reused','Legs']:
    df[c]=df[c].astype(int)
df['LandingOutcome']=df['Class'].map({1:'Success',0:'Failure'})
df['PayloadMass']=df['PayloadMass'].fillna(df['PayloadMass'].median())
df.to_csv('../data/cleaned_spacex_falcon9.csv',index=False)
