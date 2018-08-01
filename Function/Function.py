
# coding: utf-8

# In[1]:


#This is a practice
def printfunction():
    print("Hi!")
    print("I'm function")
print("Out of function")


# In[4]:


printfunction()


# In[5]:


def doublefunction(x):
    return 2*x


# In[7]:


a=doublefunction(2)
print(a)


# In[8]:


def plusfunction(x,y):
    return x+y


# In[11]:


b=plusfunction(2,3)
print(b)


# In[21]:


def function(x):
    print(x)
    print("I'm in the function")
    return 3*x


# In[14]:


c=function(3)


# In[15]:


print(c)


# In[24]:


def function2(x):
    print(x)
    print("I'm in the function")


# In[25]:


function2(3)


# In[14]:


def greeting(name):
    print('Hi!'+name+'. How are you?')


# In[16]:


greeting('Jimmy')


# In[17]:


def sub(x,y):
    return x-y


# In[18]:


a=int(input('a:'))
b=int(input('b:'))
c=sub(a,b)
print(c)

