
# coding: utf-8

# In[3]:


a=[1,3,-1]


# In[4]:


a.append(1)


# In[5]:


print(a)
print(type(a))


# In[4]:


a.append("hi")
print(a)


# In[5]:


a.append('hello')
print(a)


# In[6]:


a.append([1,2])
print(a)


# In[7]:


#delete last item
a.pop()
print(a)


# In[8]:


a.pop(2)
print(a)


# In[9]:


print(a[0])


# In[10]:


print(a[2])


# In[11]:


a[0]=250
print(a)


# In[44]:


b=["apple","banana","computer"]


# In[45]:


temp=b[0]
b[0]=b[2]
b[2]=temp


# In[46]:


print(b)


# In[47]:


b[0],b[2]=b[2],b[0]
print(b)


# In[15]:


james=[23,19,22,31,18]
game1,game2,game3,game4,game5=james
print("各場得分:",game1,  game2,  game3,  game4,  game5)


# In[19]:


print(james[0:7])


# In[20]:


print(james[1:3])


# In[21]:


print(james[:2])


# In[22]:


print(james[2:])


# In[23]:


print(james[-2:])


# In[24]:


print(james[:])


# In[25]:


print(james[0:5:2])


# In[27]:


print(james[-1])


# In[28]:


print(james[-2])


# In[29]:


print(max(james))


# In[30]:


print(min(james))


# In[31]:


print(sum(james))


# In[32]:


james=['james',23,19,22,31,18]


# In[33]:


print(max(james))


# In[34]:


print(max(james[1:6]))


# In[35]:


print(min(james[1:]))


# In[36]:


print(sum(james[-5:]))


# In[37]:


print(len(james))


# In[38]:


james=[23,19,22,31,18]


# In[39]:


james[2]=28


# In[40]:


print(james)


# In[41]:


cars1=['Toyota','Nissan','Honda']
cars2=['Audi',"BMW"]
cars1+=cars2
print(cars1)


# In[43]:


num1=[1,2,3]
num2=[4,5,6]
num3=num1+num2
print(num3)


# In[44]:


num3=num1*3
print(num3)


# In[45]:


cars1=cars1*3
print(cars1)


# In[48]:


warriors=['Curry','Durant','Iquodala','Bell','Thompson']
print(warriors)
del warriors[2]
print(warriors)


# In[51]:


james=[23,19,22,31,18]
print(james)
del james[0:5:2]
print(james)


# In[52]:


x=[1,2,3]
print(x)
del x
print(x)

