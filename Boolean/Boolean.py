
# coding: utf-8

# In[1]:


type("Jimmy")


# In[2]:


type(10)


# In[3]:


type(10.2)


# In[4]:


type(True)


# In[5]:


a=3
b=1


# In[6]:


if a>b:
    print("a is greater than b")


# In[7]:


if True:
    print("a is greater than b")


# In[8]:


type(a>b)


# In[10]:


boolean_value=a>b
print(boolean_value)


# In[11]:


if boolean_value:
    print("a is greater than b")


# In[21]:


def are_you_sad(is_rainy,have_umbrella):
    # if is_rainy==True and have_umbrella==False:
        # return True
    # else:
        # return False
    
    # if is_rainy and not have_umbrella:
        # return True
    # else:
        # return False
    
    return is_rainy and not have_umbrella


# In[22]:


are_you_sad(True,False)


# In[23]:


are_you_sad(True,True)


# In[1]:


a=True
b=False
print(int(True))
print(int(False))


# In[6]:


if 1:
    print("hi")
elif 0:
    print("hello")

