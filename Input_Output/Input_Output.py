
# coding: utf-8

# In[1]:


help(print)


# In[5]:


a="Hello"
b=5
print(a,b,sep=" $$$ ")


# In[7]:


c="World"
d=10
print(a,b,end="\t")
print(c,d,sep=" $$$ ")


# In[8]:


score=90
name="林冠宇"
count=1
print("%s this is your %d grade of math exam : %d" % (name,count,score))


# In[9]:


score=90
name="林冠宇"
count=1
str="%s this is your %d grade of math exam : %d"
print(str % (name,count,score))


# In[10]:


x=100
print("16進位:%x \n8進位:%o" %(x,x))


# In[11]:


x=100
print("float:%f \nint:%d \nstr:%s" %(x,x,x))


# In[20]:


x=100
print("x=/%6d/"%x)
y=10.5
print("y=/%6.2f/"%y)
s="hello"
print("s=/%6s/"%s)
print("Don't have enough space")
print("x=/%2d/"%x)
print("y=/%2.2f/"%y)
print("s=/%2s/"%s)


# In[21]:


x=100
print("x=/%-6d/"%x)
y=10.5
print("y=/%-6.2f/"%y)
s="hello"
print("s=/%-6s/"%s)


# In[22]:


x=100
print("x=/%+6d/"%x)
y=10.5
print("y=/%+6.2f/"%y)
s="hello"
print("s=/%+6s/"%s)


# In[23]:


score=90
name="林冠宇"
count=1
print("{} this is your {} grade of math exam : {}".format(name,count,score))


# In[24]:


score=90
name="林冠宇"
count=1
str="{} this is your {} grade of math exam : {}"
print(str.format(name,count,score))


# In[26]:


help(open)


# In[42]:


file_obj1=open("output1.txt",mode="w")


# In[43]:


print("Test1",file=file_obj1)


# In[44]:


file_obj1.close()


# In[54]:


file_obj2=open("output2.txt",mode="a")


# In[55]:


print("World",file=file_obj2)


# In[56]:


file_obj2.close()


# In[57]:


name=input("name:")
grade=input("grade:")
print(type(name))
print(type(grade))


# In[58]:


name=input("name:")
math_grade=input("math_grade:")
english_grade=input("english_grade:")
sum=int(math_grade)+int(english_grade)
print("{} your sum of grade is {}".format(name,sum))


# In[67]:


dir(__builtins__)

