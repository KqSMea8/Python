
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


# In[1]:


class Robota:
    def __init__(self,name,color,weight):
        self.name=name
        self.color=color
        self.weight=weight
    def introduce(self):
        print("My name is " + self.name)


# In[2]:


r1=Robota("Robot_1","blue",30)
r2=Robota("Robot_2","white",40)


# In[3]:


class Person:
    def __init__(self,name,personality,is_sitting):
        self.name=name
        self.personality=personality
        self.is_sitting=is_sitting
    def sit_down(self):
        self.is_sitting=True
    def stand_up(self):
        self.is_sitting=False


# In[4]:


p1=Person("Jimmy","friendly",True)
p2=Person("Ruby","talkative",False)


# In[5]:


p1.robot_owned=r1
p2.robot_owned=r2


# In[6]:


p2.robot_owned.introduce()

