
# coding: utf-8

# In[11]:


# "self" = "this" in Java


# In[12]:


# class Robot:
   # def introduce(self):
       # print("My name is " + self.name)


# In[13]:


# s1=Robot()
# s1.name="Jimmy"
# s1.color="blue"
# s1.weight=58

# s2=Robot()
# s2.name="Ruby"
# s2.color="white"
# s2.weight=40


# In[14]:


# s1.introduce()
# s2.introduce()


# In[15]:


class Robot:
    def __init__(self,name,color,weight):
        self.name=name
        self.color=color
        self.weight=weight
    def introduce(self):
        print("My name is " + self.name)


# In[28]:


s1=Robot("Jimmy","blue",58)
s2=Robot("Ruby","white",40)


# In[29]:


s1.introduce()
s2.introduce()

