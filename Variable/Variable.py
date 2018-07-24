
# coding: utf-8

# In[1]:


x=y=z=10


# In[3]:


print(x)
print(y)
print(z)


# In[4]:


x,y,z=1,2,3


# In[6]:


print(x)
print(y)
print(z)


# In[7]:


x,y=1,2
x,y=y,x


# In[8]:


print(x)
print(y)


# In[9]:


del x


# In[15]:


x=1;y=2;print(x);print(y)


# In[16]:


# can't add comment on the right of \
x=1+  2+  3
print(x)


# In[17]:


y=(1+ #can add comment
   2+
   3)
print(y)


# In[1]:


x=0b111001
print(x)


# In[2]:


x=57
print(bin(x))


# In[3]:


x=0o57
print(x)


# In[4]:


x=47
print(oct(x))


# In[6]:


x=0x55
print(x)


# In[8]:


x=85
print(hex(x))


# In[9]:


x=5.5
print(x)
print(type(x))


# In[12]:


y=int(x)+5
print(y)
print(type(y))


# In[14]:


x=-10
x=abs(x)
print(x)
print(type(x))


# In[16]:


x=3
y=4
z=pow(3,4)
print(z)


# In[17]:


x="Hello "
y="World"
z=x+y
print(z)


# In[18]:


x='''123456789
1111'''
print(x)


# In[21]:


x="I can't do that"
print(x)


# In[22]:


x='I can\'t do that'
print(x)


# In[23]:


x="I \tcan't do \nthat"
print(x)


# In[1]:


x='''hello hello
 world'''
print(x)


# In[24]:


x=222
y=333
z=str(x)+str(y)
print(z)


# In[25]:


x="222"
y="333"
z=int(x)+int(y)
print(z)


# In[4]:


x1=97
x2=chr(x1)
print(x2)
x3=ord(x2)
print(x3)
x4='林'
print(ord(x4))


# In[26]:


x="Hi "
y=x*10
print(y)


# In[27]:


x="Hi"
y="Hello"
z="How do you do"
w=x+"\n"+y+"\n"+z
print(w)


# In[1]:


str="HelloWorld"
print(str.upper())
print(str.lower())
print(str.title())


# In[3]:


str=" HelloWorld "
print(str.lstrip())
print(str.rstrip())
x=str.lstrip()
x=x.rstrip()
print(x)
print(str.strip())


# In[4]:


string="abC"
dir(string)


# In[5]:


x=string.islower()
print(x)


# In[28]:


# This is comment

'''
This is comment
'''
"""
This is comment
"""

