import pandas as pd, folium
from folium.plugins import MarkerCluster
df=pd.read_csv('../data/cleaned_spacex_falcon9.csv')
m=folium.Map(location=[29,-95],zoom_start=4)
cluster=MarkerCluster().add_to(m)
for _,r in df.iterrows():
    color='green' if r.Class==1 else 'red'
    folium.CircleMarker([r.Latitude,r.Longitude],radius=5,color=color,fill=True,
        popup=f"Flight {r.FlightNumber} | {r.LaunchSite} | {'Success' if r.Class else 'Failure'}").add_to(cluster)
m.save('../figures/folium_launch_map.html')
