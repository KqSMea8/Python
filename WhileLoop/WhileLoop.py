
# coding: utf-8

# In[ ]:


#while condition
#    code block


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


# In[6]:


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


# In[3]:


msg=''
while msg!='q':
    msg=input('input:')
    print('='+msg)


# In[4]:


msg=''
while msg!='q':
    msg=input('input:')
    if msg!='q':
        print('='+msg)


# In[1]:


msg=''
active=True
while active:
    msg=input('input:')
    if msg!='q':
        print('='+msg)
    else:
        active=False


# In[3]:


answer=30
active=True
while active:
    number=int(input('enter a number:'))
    if number>answer:
        print('guess smaller')
    elif number==answer:
        print('congradulations')
        active=False
    else:
        print('guess larger')


# In[4]:


index=1
while index<=5:
    print(index)
    index+=1


# In[7]:


i=1
j=1
while i<=9:
    while j<=9:
        print('%d*%d=%-3d'%(i,j,i*j),end=' ')
        j+=1
    j=1
    i+=1
    print("")


# In[8]:


msg=''
while True:
    msg=input('input:')
    if msg=='q':
        break
    else:
        print('='+msg)


# In[2]:


index=0
while index<=10:
    index+=1
    if index%2!=0:
        continue
    else:
        print(index)


# In[4]:


fruits=['apple','banana','orange','apple','apple']
fruit='apple'
while fruit in fruits:
    fruits.remove(fruit)
print(fruits)


# In[7]:


buyers=[['James',1030],['Curry',893],['Durant',2050],['Jordan',990],['David',2110]]
goldenbuyer=[]
vipbuyer=[]
while buyers:
    index_buyer=buyers.pop()
    if index_buyer[1]>1000:
        vipbuyer.append(index_buyer)
    else:
        goldenbuyer.append(index_buyer)
print(vipbuyer)
print(goldenbuyer)
print(buyers)


# In[12]:


drinks=['tea','coffee','wine']
edrinks=enumerate(drinks)
print(list(edrinks))
for drink in enumerate(drinks):
    print(drink)
for count,drink in enumerate(drinks):
    print(count,drink)

