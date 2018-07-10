
# coding: utf-8

# In[11]:


# "self" = "this" in Java


# In[12]:


# class Robot:
   # def introduce(self):
       # print("My name is " + self.name)


# In[13]:


# r1=Robot()
# r1.name="Jimmy"
# r1.color="blue"
# r1.weight=58

# r2=Robot()
# r2.name="Ruby"
# r2.color="white"
# r2.weight=40


# In[14]:


# r1.introduce()
# r2.introduce()


# In[30]:


class Robot:
    def __init__(self,name,color,weight):
        self.name=name
        self.color=color
        self.weight=weight
    def introduce(self):
        print("My name is " + self.name)


# In[31]:


r1=Robot("Jimmy","blue",58)
r2=Robot("Ruby","white",40)


# In[32]:


r1.introduce()
r2.introduce()

