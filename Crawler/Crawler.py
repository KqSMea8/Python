
# coding: utf-8

# In[4]:


import requests
res = requests.get("https://s.taobao.com/search?q=%E4%BF%9D%E6%BA%AB%E7%93%B6&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180915&ie=utf8")
print(res.text)

