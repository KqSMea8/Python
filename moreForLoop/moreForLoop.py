
# coding: utf-8

# In[1]:


a=["apple","banana","computer"]


# In[2]:


for element in a:
    print(element)


# In[10]:


for i in range(len(a)): # 0,1,2
    for j in range(i+1): # range(2) means range(0,2) => 0~1
        print(a[i])


# In[13]:


# calculate sum of multiples of 3 or 5 that are less than 100
b=list(range(1,100))


# In[22]:


sum=0
for i in range(len(b)):
    if b[i]%3==0 or b[i]%5==0:
        sum+=b[i]
print(sum)


# In[23]:


# calculate sum of negative number
c=[7,5,4,4,3,1,-2,-3,-5,-7]
sum=0
for i in range(len(c)):
    if c[i]<0:
        sum+=c[i]
print(sum)


# In[24]:


sum=0
j=len(c)-1
while c[j]<0:
    sum+=c[j]
    j-=1
print(sum)

