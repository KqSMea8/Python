
# coding: utf-8

# In[1]:


def bmi(height,weight):
    bmi=weight/(height**2)
    if bmi<18.5:
        print("You are underweight")
    elif 18.5<=bmi<24:
        print("You are healthy")
    else:
        print("You are overweight")


# In[2]:


print("height(m):")
height=float(input())


# In[3]:


print("weight(kg):")
weight=float(input())


# In[4]:


bmi(height,weight)


# In[5]:


def bmireturn(height,weight):
    bmi=weight/(height**2)
    if bmi<18.5:
        return "You are underweight"
    elif 18.5<=bmi<24:
        return "You are healthy"
    else:
        return "You are overweight"


# In[6]:


print("height(m):")
height=float(input())


# In[7]:


print("weight(kg):")
weight=float(input())


# In[8]:


result=bmireturn(height,weight)


# In[9]:


print(result)

