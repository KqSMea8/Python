
# coding: utf-8

# In[5]:


from sklearn import datasets
#dictionary


# In[2]:


wine=datasets.load_wine()


# In[3]:


wine


# In[4]:


wine.keys()


# In[6]:


import pandas as pd


# In[7]:


a=pd.DataFrame(wine['data'],columns=wine['feature_names'])


# In[8]:


a


# In[9]:


b=pd.DataFrame(wine['target'],columns=['target_names'])


# In[10]:


b


# In[11]:


data=pd.concat([a,b],axis=1)


# In[12]:


data

