
# coding: utf-8

# In[1]:


import googlemaps
import pandas as pd

gmaps = googlemaps.Client(key='AIzaSyBSumCqmtCwegLo2rf-AWJS8OvYLpVpx-Y')


# In[2]:


cities= ["澎湖縣"]


# In[3]:


geocode_result= gmaps.geocode("臺北市")
geocode_result


# In[5]:


ids = []
for city in cities:
    geocode_result = gmaps.geocode(city)
    loc = geocode_result[0]['geometry']['location']
    print("以"+city+"為中心半徑25000公尺的寵物店家數量: "+str(len(gmaps.places_radar(keyword="寵物",location=loc, radius=1000)['results'])))
    for place in gmaps.places_radar(keyword="寵物", location=loc, radius=1000)['results']:
        ids.append(place['place_id'])


# In[6]:


stores_info = []
# 去除重複id
ids = list(set(ids)) 
stores_info.append(gmaps.place(place_id=ids[1], language='zh-TW')['result'])


# In[7]:


output = pd.DataFrame.from_dict(stores_info)


# In[8]:


output

