
# coding: utf-8

# In[1]:


a=["apple","banana","computer"]


# In[2]:


print(a[0])
print(a[1])
print(a[2])


# In[ ]:


#for 變數 in 物件:
#    code block


# In[5]:


for element in a:
    print(element)


# In[8]:


b=[20,10,50]
total=0
for i in b:
    print(i)
    total+=i
print(total)


# In[7]:


#list function
c=list(range(1,5))
d=list(range(5))
print(c)
print(d)


# In[12]:


for i in c:
    print(i)


# In[13]:


for i in range(1,5):
    print(i)


# In[16]:


print(list(range(1,8)))


# In[20]:


sum=0
for i in range(1,8):
    if i%3==0:
        sum+=i
print(sum)


# In[2]:


players=['curry','jordan','james','durant','obama']
for player in players:
    print(player)


# In[6]:


players=['curry','jordan','james','durant','obama']
for player in players[:3]:
    print(player)
for player in players[-2:]:
    print(player)


# In[17]:


x=list(range(6))
print(x)
for i in range(6):
    print(i)


# In[18]:


x=list(range(0,6))
print(x)
for i in range(0,6):
    print(i)


# In[19]:


x=list(range(0,6,2))
print(x)
for i in range(0,6,2):
    print(i)


# In[23]:


n=int(input("input:"))
x=list(range(1,n+1))
y=sum(x)
print(y)


# In[26]:


n=int(input("input:"))
total=0
for i in range(1,n+1):
    total+=i
print(total)


# In[27]:


list1=[]
n=int(input('input:'))
for i in range(n+1):
    a=i*i
    list1.append(a)
print(list1)


# In[30]:


#advanced
n=int(input('input:'))
list1=[i**2 for i in range(n+1)]
print(list1)


# In[33]:


for i in range(1,10):
    for j in range(1,10):
        print("%d*%d=%-3d"%(i,j,i*j),end=' ')
    print("")


# In[38]:


print("test1")
for i in range(1,11):
    if i==5:
        break
    print(i,end=' ')
print('')
print('test2')
for i in range(0,11,2):
    if i==5:
        break
    print(i,end=' ')


# In[39]:


for i in range(1,11):
    if i==5:
        continue
    print(i)


# In[41]:


scores=[33,22,41,25,39,43,27,38,40]
count=0
for i in scores:
    if i<30:
        continue
    count+=1
print("%d games higher than 30 scores"%count)


# In[45]:


#for...else
for i in range(11):
    print(i,end=' ')
    if i==5:
        break
else: #execute if for loop condition(last time) is false
    print(i)


# In[46]:


for i in range(11):
    print(i,end=' ')
else: 
    print('')
    print(i)

