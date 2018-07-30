
# coding: utf-8

# In[1]:


a={}
# a={"Jimmy":21,"Billy":22}
# Key->Value
# Values can be any type
# Keys are commonly Strings or Numbers and can't be repeated


# In[3]:


a["Jimmy"]=21
a["Billy"]=22


# In[4]:


print(a)


# In[5]:


print(a["Jimmy"])


# In[6]:


a[10]=100


# In[7]:


print(a[10])


# In[26]:


for key,value in a.items():
    print(key)
    print(value)
    print("")


# In[3]:


fruits={'apple':60,'banana':50,'pineapple':90}
print(type(fruits))
print(fruits)
print(fruits['apple'])


# In[4]:


fruits['watermelon']=30
print(fruits['watermelon'])


# In[6]:


soldier={'tag':'red','score':3}
soldier['xpos']=100
soldier['ypos']=30
soldier['speed']='slow'
print(soldier['xpos'])
print(soldier['ypos'])
print(soldier['speed'])


# In[7]:


fruits={'apple':60,'banana':50,'pineapple':90}
fruits['apple']=100
print(fruits['apple'])


# In[10]:


soldier={'tag':'red','score':3}
soldier['xpos']=100
soldier['ypos']=30
soldier['speed']='slow'
print(soldier)
if soldier['speed']=='slow':
    xmove=1
elif soldier['speed']=='medium':
    xmove=3
else:
    xmove=5
soldier['xpos']+=xmove
print(soldier["xpos"])


# In[12]:


fruits={'apple':60,'banana':50,'pineapple':90}
print(fruits)
del fruits['apple']
print(fruits)


# In[14]:


fruits={'apple':60,'banana':50,'pineapple':90}
print(fruits)
fruits.clear()
print(fruits)


# In[15]:


fruits={'apple':60,'banana':50,'pineapple':90}
print(fruits)
del fruits
print(fruits)


# In[20]:


fruits={}
fruits['apple']=10
fruits['banana']=20
print(fruits)


# In[27]:


fruits={'apple':60,'banana':50,'pineapple':90}
cfruits=fruits.copy()
cfruits['pineapple']=10
print(id(fruits))
print(id(cfruits))
print(fruits)
print(cfruits)


# In[29]:


fruits={'apple':60,'banana':50,'pineapple':90,'watermelon':80}
drinks={'tea':10,'coffee':20,'wine':60}
x={}
print(len(fruits))
print(len(drinks))
print(len(x))


# In[34]:


fruits={'apple':60,'banana':50,'pineapple':90}
key=input('key:')
value=input('value:')
if key in fruits:
    print('already in dictionary')
else:
    fruits[key]=value
    print(fruits)


# In[35]:


players={'Stephon Curry':'Golden State Warriors',
        'Kevin Durant':'Golden State Warriors',
        'Lebron James':'Cleveland Cavaliers',
        'James Harden':'Houston Rockets',
        'Paul Gasol':'San Antonio Spurs'}
for name,team in players.items():
    print(name)
    print(team)
    print()


# In[36]:


players={'Stephon Curry':'Golden State Warriors',
        'Kevin Durant':'Golden State Warriors',
        'Lebron James':'Cleveland Cavaliers',
        'James Harden':'Houston Rockets',
        'Paul Gasol':'San Antonio Spurs'}
for name in players.keys():
    print(name)
    print()


# In[37]:


players={'Stephon Curry':'Golden State Warriors',
        'Kevin Durant':'Golden State Warriors',
        'Lebron James':'Cleveland Cavaliers',
        'James Harden':'Houston Rockets',
        'Paul Gasol':'San Antonio Spurs'}
for name in players:
    print(name)
    print()


# In[38]:


players={'Stephon Curry':'Golden State Warriors',
        'Kevin Durant':'Golden State Warriors',
        'Lebron James':'Cleveland Cavaliers',
        'James Harden':'Houston Rockets',
        'Paul Gasol':'San Antonio Spurs'}
for name in sorted(players.keys()):
    print(name)
    print()


# In[39]:


players={'Stephon Curry':'Golden State Warriors',
        'Kevin Durant':'Golden State Warriors',
        'Lebron James':'Cleveland Cavaliers',
        'James Harden':'Houston Rockets',
        'Paul Gasol':'San Antonio Spurs'}
for team in players.values():
    print(team)
    print()


# In[40]:


players={'Stephon Curry':'Golden State Warriors',
        'Kevin Durant':'Golden State Warriors',
        'Lebron James':'Cleveland Cavaliers',
        'James Harden':'Houston Rockets',
        'Paul Gasol':'San Antonio Spurs'}
for team in set(players.values()):
    print(team)
    print()


# In[47]:


soldier0={'tag':'red','score':3,'speed':'slow'}
soldier1={'tag':'blue','score':5,'speed':'medium'}
soldier2={'tag':'green','score':10,'speed':'fast'}
armys=[soldier0,soldier1,soldier2]
for army in armys:
    print(army)

