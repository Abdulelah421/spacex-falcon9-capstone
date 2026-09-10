import pandas as pd, matplotlib.pyplot as plt
df=pd.read_csv('../data/cleaned_spacex_falcon9.csv')
df.groupby('Year')['Class'].mean().mul(100).plot(marker='o',title='Yearly landing success rate')
plt.ylabel('Success rate (%)'); plt.tight_layout(); plt.show()
