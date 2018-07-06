
# coding: utf-8

# In[4]:


print("height(m):")
height=float(input())


# In[5]:


print("weight(kg):")
weight=float(input())


# In[6]:


bmi=weight/(height**2)


# In[7]:


if bmi<18.5:
    print("You are underweight")
elif 18.5<=bmi<24:
    print("You are healthy")
else:
    print("You are overweight")

