
# coding: utf-8

# In[1]:


a={}
# a={"Jimmy":21,"Billy":22}
# Key->Value
# Values can be any type
# Keys are commonly Strings or Numbers


# In[3]:


a["Jimmy"]=21
a["Billy"]=22


# In[4]:


print(a)


# In[5]:


print(a["Jimmy"])


# In[6]:


a[10]=100


# In[7]:


print(a[10])


# In[26]:


for key,value in a.items():
    print(key)
    print(value)
    print("")

