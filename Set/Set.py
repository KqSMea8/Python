
# coding: utf-8

# In[1]:


#can't add list, set, and dictionary
set1={'apple','banana',123}
print(type(set1))
print(set1)


# In[1]:


set1={'Java','Python','C','Python','Java'}
print(set1)


# In[2]:


set1={1,2,5}
print(set1)
set1={1,'Python',(2,5,6)}
print(set1)


# In[3]:


set1={1,'Python',[2,5,6]}


# In[5]:


x={}
print(x)
print(type(x)) # not set


# In[7]:


empty_dict={}
empty_set=set()
print(type(empty_dict))
print(type(empty_set))


# In[9]:


string='Hello World'
set1=set(string)
print(set1)


# In[10]:


fruits=['apple','banana','orange','watermelon']
set1=set(fruits)
print(set1)


# In[11]:


fruits=('apple','banana','orange','watermelon')
set2=set(fruits)
print(set2)


# In[12]:


fruits=['apple','banana','orange','watermelon','apple','banana']
x=set(fruits)
fruits2=list(x)
print(fruits)
print(fruits2)


# In[13]:


math={'Kevin','Peter','Eric'}
physics={'Peter','Jimmy','Tom'}
same=math&physics
print(same)


# In[15]:


math={'Kevin','Peter','Eric'}
physics={'Peter','Jimmy','Tom'}
same=math.intersection(physics)
print(same)
same1=physics.intersection(math)
print(same1)


# In[16]:


math={'Kevin','Peter','Eric'}
physics={'Peter','Jimmy','Tom'}
allp=math|physics
print(allp)


# In[17]:


math={'Kevin','Peter','Eric'}
physics={'Peter','Jimmy','Tom'}
allp=math.union(physics)
print(allp)
allp1=physics.union(math)
print(allp1)


# In[18]:


math={'Kevin','Peter','Eric'}
physics={'Peter','Jimmy','Tom'}
diff=math-physics
print(diff)

