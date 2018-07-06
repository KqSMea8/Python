
# coding: utf-8

# In[1]:


a=[1,3,-1]


# In[2]:


a.append(1)


# In[3]:


print(a)


# In[4]:


a.append("hi")
print(a)


# In[5]:


a.append('hello')
print(a)


# In[6]:


a.append([1,2])
print(a)


# In[7]:


#delete last item
a.pop()
print(a)


# In[8]:


a.pop(2)
print(a)


# In[9]:


print(a[0])


# In[10]:


print(a[2])


# In[11]:


a[0]=250
print(a)


# In[44]:


b=["apple","banana","computer"]


# In[45]:


temp=b[0]
b[0]=b[2]
b[2]=temp


# In[46]:


print(b)


# In[47]:


b[0],b[2]=b[2],b[0]
print(b)

