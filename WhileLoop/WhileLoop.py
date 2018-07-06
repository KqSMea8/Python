
# coding: utf-8

# In[2]:


total=0
i=1
while i<5:
    total+=i
    i+=1
print(total)


# In[3]:


# a is a given sorted list
a=[5,4,4,3,2,1,-1,-2,-3,-5]
sum=0
i=0
while a[i]>0:
    sum+=a[i]
    i+=1
print(sum)


# In[5]:


a=[5,4,4,3,2,1]
sum=0
i=0
while i<len(a) and a[i]>0:
    sum+=a[i]
    i+=1
print(sum)


# In[7]:


a=[5,4,4,3,2,1,-1,-2,-3,-5]
sum=0
for element in a:
    if element<0:
        break
    sum+=element
print(sum)


# In[8]:


a=[5,4,4,3,2,1,-1,-2,-3,-5]
sum=0
i=0
while True:
    if a[i]<0:
        break
    sum+=a[i]
    i+=1
print(sum)

