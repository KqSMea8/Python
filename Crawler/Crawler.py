
# coding: utf-8

# In[4]:


import requests
res = requests.get("https://s.taobao.com/search?q=%E4%BF%9D%E6%BA%AB%E7%93%B6&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180915&ie=utf8")
print(res.text)


# In[18]:


from bs4 import BeautifulSoup
html_sample=' <html>  <body>      <h1 id="title">Hello World</h1>      <a href="#" class="link">This is link1</a>      <a href="# link2" class="link">This is link2</a>  </body> </html>'
soup=BeautifulSoup(html_sample)
print(soup.text)


# In[19]:


print(soup.contents)


# In[21]:


print(soup.select('html'))


# In[23]:


print(soup.select('html')[0])


# In[25]:


print(soup.select('body'))


# In[26]:


print(soup.select('h1'))


# In[27]:


print(soup.select('a'))


# In[28]:


# id: #title
# class: .link
print(soup.select('#title'))


# In[29]:


print(soup.select('.link'))

