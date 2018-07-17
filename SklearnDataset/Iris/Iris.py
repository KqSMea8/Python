
# coding: utf-8

# In[1]:


from sklearn import datasets


# In[2]:


iris=datasets.load_iris()


# In[3]:


iris


# In[4]:


type(iris.data)


# In[5]:


type(iris.target)


# In[6]:


type(iris.target_names)


# In[7]:


type(iris.feature_names)


# In[8]:


type(iris.DESCR)


# In[10]:


iris.keys()


# In[11]:


print(iris['data'])


# In[12]:


import pandas as pd


# In[19]:


a=pd.DataFrame(iris['data'],columns=iris['feature_names'])


# In[20]:


a


# In[39]:


b=pd.DataFrame(iris['target'],columns=['target_names'])


# In[40]:


b


# In[41]:


data=pd.concat([a,b],axis=1)


# In[42]:


data

