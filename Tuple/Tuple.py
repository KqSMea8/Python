
# coding: utf-8

# In[1]:


#unchangeable list


# In[2]:


numbers=(1,5,6,8,2)


# In[3]:


fruits=('apple','banana')


# In[4]:


mixed=('james',23)


# In[5]:


onlyone=(1,) #should add ',' if only one element


# In[6]:


print(numbers)
print(fruits)
print(mixed)
print(onlyone)


# In[7]:


print(type(fruits))


# In[8]:


numbers=(1,5,6,8,2)
fruits=('apple','banana')
mixed=('james',23)
print(numbers[0])
print(numbers[4])
print(fruits[1])
print(mixed[0])


# In[9]:


keys=('apple','banana',23)
for key in keys:
    print(key)


# In[10]:


fruits=('apple','banana')
fruits[0]='pineapple'


# In[12]:


# Tuple is unchangeable 
# only way to change is to reassign
fruits=('apple','banana')
for fruit in fruits:
    print(fruit)
fruits=('watermelon','pineapple')
for fruit in fruits:
    print(fruit)


# In[14]:


fruits=('apple','banana','watermelon','pineapple','grape')
print(fruits[:3])
print(fruits[3:])
print(fruits[-3:])
print(fruits[1:3])
print(fruits[0:5:2])


# In[15]:


fruits=('apple','banana','watermelon','pineapple','grape')
print(len(fruits))


# In[16]:


fruits=('apple','banana','watermelon','pineapple','grape')
fruits.pop()


# In[17]:


fruits=('apple','banana','watermelon','pineapple','grape')
fruits.append(20)


# In[18]:


fruits=('apple','banana','watermelon','pineapple','grape')
listfruits=list(fruits)
listfruits.append('hi')
print(fruits)
print(listfruits)


# In[20]:


fruits=['apple','banana','watermelon','pineapple','grape']
tuplefruits=tuple(fruits)
print(tuplefruits)
print(fruits)
tuplefruits.append('hi')


# In[21]:


tup=(1,5,6,9,2)
print(max(tup))
print(min(tup))

