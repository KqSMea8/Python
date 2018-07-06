
# coding: utf-8

# In[1]:


a=["apple","banana","computer"]


# In[2]:


print(a[0])
print(a[1])
print(a[2])


# In[5]:


for element in a:
    print(element)


# In[8]:


b=[20,10,50]
total=0
for i in b:
    print(i)
    total+=i
print(total)


# In[11]:


#list function
c=list(range(1,5))
print(c)


# In[12]:


for i in c:
    print(i)


# In[13]:


for i in range(1,5):
    print(i)


# In[16]:


print(list(range(1,8)))


# In[20]:


sum=0
for i in range(1,8):
    if i%3==0:
        sum+=i
print(sum)

