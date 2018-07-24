
# coding: utf-8

# In[1]:


x=10>8
print(x)
x=10>=8
print(x)
x=8<10
print(x)
x=8<=10
print(x)
x=10==10
print(x)
x=8!=10
print(x)


# In[2]:


x=8>10
print(x)
x=8>=10
print(x)
x=10<8
print(x)
x=10<=8
print(x)
x=10==8
print(x)
x=10!=10
print(x)


# In[3]:


x=(10>8)and(20>10)
print(x)


# In[4]:


x=(10>8)or(10>10)
print(x)


# In[7]:


x=not(20>10)
print(x)


# In[3]:


a=1
b=2
if a<b:
    print("a is less than b")
print("finish compare")


# In[5]:


c=2
d=1
if c<d:
    print("c is less than d")
else:
    print("c is not less than d")
print("finish compare")


# In[6]:


e=1
f=2
if e<f:
    print("e is less than f")
elif e==f:
    print("e is equal to f")
else:
    print("e is greater than f")
print("finish compare")


# In[7]:


e=5
if e<f:
    print("e is less than f")
elif e==f:
    print("e is equal to f")
else:
    print("e is greater than f")
print("finish compare")


# In[14]:


e=2
if e<f:
    print("e is less than f")
elif e==f:
    print("e is equal to f")
else:
    print("e is greater than f")
print("finish compare")


# In[10]:


e=20
if e<f:
    print("e is less than f")
elif e==f:
    print("e is equal to f")
elif e>f+10:
    print("e is greater than f by more than 10")
else:
    print("e is greater than f")
print("finish compare")


# In[11]:


e=2
if e<f:
    print("e is less than f")
else:
    if e==f:
        print("e is equal to f")
    else:
        print("e is greater than f")
print("finish compare")


# In[15]:


if e<f:
    print("e is less than f")
elif e==f:
    print("e is equal to f")
    print("e is equal to f")
    print("e is equal to f")
    print("e is equal to f")
else:
    print("e is greater than f")
print("finish compare")


# In[9]:


age=input("age:")
if int(age)<20:
    print("You can't drink beer")


# In[12]:


num=input("num:")
x=int(num)
if x<0:
    x=abs(x)
print(x)


# In[13]:


score=input("score")
sc=int(score)
if sc>=90:
    print("A")
elif sc>=80:
    print("B")
elif sc>=70:
    print("C")
elif sc>=60:
    print("D")
else:
    print("E")


# In[14]:


ch=input("char")
if ord(ch)>=ord("A") and ord(ch)<=ord("Z"):
    print("這是英文大寫")
elif ord(ch)>=ord("a") and ord(ch)<=ord("z"):
    print("這是英文小寫")
elif ord(ch)>=ord("0") and ord(ch)<=ord("9"):
    print("這是數字")
else:
    print("這是特殊字元")


# In[15]:


x=None
print(x)
print(type(x))

