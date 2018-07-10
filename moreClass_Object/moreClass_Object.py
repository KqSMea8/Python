
# coding: utf-8

# In[1]:


class Robot:
    def __init__(self,name,color,weight):
        self.name=name
        self.color=color
        self.weight=weight
    def introduce(self):
        print("My name is " + self.name)


# In[2]:


r1=Robot("Robot_1","blue",30)
r2=Robot("Robot_2","white",40)


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


p1.robot_owned.introduce()

