
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[4]:


df=pd.DataFrame(np.random.randn(6,4),columns=['a','b','c','d'])


# In[5]:


df


# In[6]:


from sklearn import datasets


# In[7]:


iris=datasets.load_iris()


# In[8]:


iris


# In[9]:


x=pd.DataFrame(iris['data'],columns=iris['feature_names'])


# In[10]:


x


# In[12]:


y=pd.DataFrame(iris['target'],columns=['target_names'])


# In[13]:


y


# In[14]:


data=pd.concat([x,y],axis=1)


# In[16]:


data.head(5)


# In[17]:


data.info()


# In[18]:


data.describe()


# In[20]:


data.columns


# In[26]:


data.sort_values(by='sepal length (cm)').head(8)


# In[27]:


data['sepal length (cm)'].head(8)


# In[29]:


data[['sepal length (cm)','sepal width (cm)']].head(8)


# In[31]:


data.loc[5:10,['sepal length (cm)','sepal width (cm)']].head(8)


# In[32]:


data[data['sepal length (cm)']>7]


# In[34]:


data.groupby(by='target_names').sum()


# In[35]:


data.groupby(by='target_names').mean()

