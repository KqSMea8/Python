
# coding: utf-8

# In[3]:


a=1
b=2
if a<b:
    print("a is less than b")
print("finish compare")


# In[5]:


c=2
d=1
if c<d:
    print("c is less than d")
else:
    print("c is not less than d")
print("finish compare")


# In[6]:


e=1
f=2
if e<f:
    print("e is less than f")
elif e==f:
    print("e is equal to f")
else:
    print("e is greater than f")
print("finish compare")


# In[7]:


e=5
if e<f:
    print("e is less than f")
elif e==f:
    print("e is equal to f")
else:
    print("e is greater than f")
print("finish compare")


# In[14]:


e=2
if e<f:
    print("e is less than f")
elif e==f:
    print("e is equal to f")
else:
    print("e is greater than f")
print("finish compare")


# In[10]:


e=20
if e<f:
    print("e is less than f")
elif e==f:
    print("e is equal to f")
elif e>f+10:
    print("e is greater than f by more than 10")
else:
    print("e is greater than f")
print("finish compare")


# In[11]:


e=2
if e<f:
    print("e is less than f")
else:
    if e==f:
        print("e is equal to f")
    else:
        print("e is greater than f")
print("finish compare")


# In[15]:


if e<f:
    print("e is less than f")
elif e==f:
    print("e is equal to f")
    print("e is equal to f")
    print("e is equal to f")
    print("e is equal to f")
else:
    print("e is greater than f")
print("finish compare")

