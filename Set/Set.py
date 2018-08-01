
# coding: utf-8

# In[1]:


#can't add list, set, and dictionary
set1={'apple','banana',123}
print(type(set1))
print(set1)


# In[1]:


set1={'Java','Python','C','Python','Java'}
print(set1)


# In[2]:


set1={1,2,5}
print(set1)
set1={1,'Python',(2,5,6)}
print(set1)


# In[3]:


set1={1,'Python',[2,5,6]}


# In[5]:


x={}
print(x)
print(type(x)) # not set


# In[7]:


empty_dict={}
empty_set=set()
print(type(empty_dict))
print(type(empty_set))


# In[9]:


string='Hello World'
set1=set(string)
print(set1)


# In[10]:


fruits=['apple','banana','orange','watermelon']
set1=set(fruits)
print(set1)


# In[11]:


fruits=('apple','banana','orange','watermelon')
set2=set(fruits)
print(set2)


# In[12]:


fruits=['apple','banana','orange','watermelon','apple','banana']
x=set(fruits)
fruits2=list(x)
print(fruits)
print(fruits2)


# In[13]:


math={'Kevin','Peter','Eric'}
physics={'Peter','Jimmy','Tom'}
same=math&physics
print(same)


# In[15]:


math={'Kevin','Peter','Eric'}
physics={'Peter','Jimmy','Tom'}
same=math.intersection(physics)
print(same)
same1=physics.intersection(math)
print(same1)


# In[16]:


math={'Kevin','Peter','Eric'}
physics={'Peter','Jimmy','Tom'}
allp=math|physics
print(allp)


# In[17]:


math={'Kevin','Peter','Eric'}
physics={'Peter','Jimmy','Tom'}
allp=math.union(physics)
print(allp)
allp1=physics.union(math)
print(allp1)


# In[18]:


math={'Kevin','Peter','Eric'}
physics={'Peter','Jimmy','Tom'}
diff=math-physics
print(diff)


# In[20]:


math={'Kevin','Peter','Eric'}
physics={'Peter','Jimmy','Tom'}
diff=math.difference(physics)
print(diff)
diff1=physics.difference(math)
print(diff1)


# In[21]:


math={'Kevin','Peter','Eric'}
physics={'Peter','Jimmy','Tom'}
only=math^physics
print(only)


# In[22]:


math={'Kevin','Peter','Eric'}
physics={'Peter','Jimmy','Tom'}
only=math.symmetric_difference(physics)
print(only)
only1=physics.symmetric_difference(math)
print(only1)


# In[23]:


math={'Kevin','Peter','Eric'}
physics={'Peter','Jimmy','Tom'}
English={'Kevin','Peter','Eric'}
print(math==English)
print(math==physics)


# In[24]:


math={'Kevin','Peter','Eric'}
physics={'Peter','Jimmy','Tom'}
English={'Kevin','Peter','Eric'}
print(math!=English)
print(math!=physics)


# In[25]:


fruit=set('orange')
print('o'in fruit)
print('q'in fruit)
cars={'Nissan','Ford','Toyota'}
print('Audi'in cars)
print('Ford'in cars)


# In[26]:


fruit=set('orange')
print('o'not in fruit)
print('q'not in fruit)
cars={'Nissan','Ford','Toyota'}
print('Audi'not in cars)
print('Ford'not in cars)


# In[27]:


cities={'Taipei','Beijing','Tokyo'}
print(cities)
cities.add('Chicago')
print(cities)
cities.add('Taipei')
print(cities)
cities.add((1,2,3))
print(cities)


# In[32]:


x={1,2,3}
y=x
y.add(5)
print(x)
print(y)
z=x.copy()
z.add(100)
print(x)
print(z)


# In[33]:


cities={'Taipei','Beijing','Tokyo'}
print(cities)
cities.remove('Beijing')
print(cities)


# In[34]:


cities={'Taipei','Beijing','Tokyo'}
print(cities)
cities.remove('Tainan')
print(cities)


# In[35]:


cities={'Taipei','Beijing','Tokyo'}
print(cities)
cities.discard('Beijing')
print(cities)
cities.discard('Tainan')
print(cities)


# In[36]:


cities={'Taipei','Beijing','Tokyo'}
print(cities.discard('Beijing'))
print(cities.discard('Tainan'))


# In[37]:


cities={'Taipei','Beijing','Tokyo'}
x=cities.pop()
print(cities)
print(x)


# In[39]:


cities={'Taipei','Beijing','Tokyo'}
print(cities)
cities.clear()
print(cities)
cities=set()
print(cities)
cities.clear()
print(cities)


# In[41]:


A={'a','b','c'}
B={'q','w','e'}
C={'a','i','o'}
x=A.isdisjoint(B)
print(x)
y=A.isdisjoint(C)
print(y)


# In[42]:


A={'a','b','c','d','e'}
B={'q','b','c'}
C={'a','b','c'}
x=C.issubset(A)
print(x)
y=B.issubset(A)
print(y)


# In[43]:


A={'a','b','c','d','e'}
B={'q','b','c'}
C={'a','b','c'}
x=A.issuperset(C)
print(x)
y=A.issuperset(B)
print(y)


# In[47]:


A={'a','b','c','d'}
B={'a','k','c'}
C={'c','f','w'}
x=A.intersection_update(B)
print(x)
print(A)
print(B)
x=A.intersection_update(B,C)
print(x)
print(A)
print(B)
print(C)


# In[48]:


cars1={'Audi','Ford','Toyota'}
cars2={'Nissan','Toyota'}
print(cars1)
print(cars2)
cars1.update(cars2)
print(cars1)
print(cars2)


# In[49]:


cars1={'Audi','Ford','Toyota'}
cars2={'Nissan','Toyota'}
print(cars1)
print(cars2)
cars1.difference_update(cars2)
print(cars1)
print(cars2)


# In[51]:


cars1={'Audi','Ford','Toyota'}
cars2={'Nissan','Toyota'}
print(cars1)
print(cars2)
cars1.symmetric_difference_update(cars2)
print(cars1)
print(cars2)


# In[53]:


num={1,3,5,9,8,5,6}
ch={'g','a','b','z'}
print(max(num))
print(min(num))
print(sum(num))
print(max(ch))
print(min(ch))


# In[55]:


num={1,3,5,9,8,5,6}
x={1,'f456a',(1,2,3)}
print(len(num))
print(len(x))


# In[57]:


cars={'Nissan','Toyota','Ford'}
carslist=sorted(cars) #list
carslist1=sorted(cars,reverse=True) #list
print(carslist)
print(carslist1)


# In[71]:


drinks={'coffee','tea','wine'}
enumerate_drinks=enumerate(drinks)
print(enumerate_drinks)
print(type(enumerate_drinks))
print(list(enumerate_drinks))
#########################
#for i in enumerate_drinks:
   # print(i)
for i in enumerate(drinks):
    print(i)
for i,j in enumerate(drinks):
    print(i,j)


# In[72]:


x=frozenset([1,3,5])
y=frozenset([1,5,9])
a=x&y
b=x|y
c=x-y
print(x)
print(y)
print(a)
print(b)
print(c)
x.add(1)


# In[73]:


x=set([1,2,3])
print(x)
x.append(1)

