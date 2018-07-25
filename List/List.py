
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


# In[53]:


cars=['bmw','benz','audi']
car1=cars[0].title()
car2=cars[1].upper()
print(car1,car2)


# In[61]:


stringlist=['bmw','benz','audi']
dir(stringlist)


# In[62]:


numlist=[1,2,3]
dir(numlist)


# In[63]:


lisr=[1,2,'hi']
dir(list)


# In[70]:


cars=['bmw','benz','audi']
cars.append('toyota')
print(cars)
cars.append('honda')
print(cars)
cars.append('ford')
print(cars)


# In[74]:


cars=['bmw','benz','audi']
cars.insert(1,'toyota')
print(cars)
cars.insert(1,'honda')
print(cars)


# In[75]:


popedcar=cars.pop()
print(popedcar)
print(cars)
popedcar=cars.pop(1)
print(popedcar)
print(cars)


# In[77]:


#if don't know the index
cars=['bmw','benz','audi','bmw']
cars.remove('bmw')
print(cars)


# In[85]:


cars=['bmw', 'honda', 'toyota', 'benz', 'audi']
cars.reverse()
print(cars)
print(cars[::-1])#*********************


# In[90]:


cars=['bmw', 'honda', 'toyota', 'benz', 'audi']
cars.sort()
print(cars)
cars.reverse()
print(cars)


# In[89]:


num=[5,6,8,2,3,4]
num.sort()
print(num)
num.reverse()
print(num)


# In[91]:


cars=['bmw', 'honda', 'toyota', 'benz', 'audi']
cars.sort(reverse=True)
print(cars)


# In[94]:


num=[5,6,8,2,3,4]
num.sort(reverse=True)
print(num)


# In[95]:


cars=['bmw', 'honda', 'toyota', 'benz', 'audi']
sortcars=sorted(cars)
print(sortcars)


# In[97]:


num=[5,6,8,2,3,4]
sortnum=sorted(num)
print(sortnum)


# In[98]:


cars=['bmw', 'honda', 'toyota', 'benz', 'audi']
sortcars=sorted(cars,reverse=True)
print(sortcars)


# In[99]:


num=[5,6,8,2,3,4]
sortnum=sorted(num,reverse=True)
print(sortnum)


# In[101]:


cars=['bmw', 'honda', 'toyota', 'benz', 'audi']
index=cars.index('bmw')
print(index)


# In[102]:


num=[5,6,8,2,3,4]
index=num.index(2)
print(index)


# In[103]:


num=[5,6,8,6,3,4]
count=num.count(6)
print(count)


# In[104]:


cars=['bmw', 'honda', 'toyota', 'benz', 'bmw']
count=cars.count('bmw')
print(count)


# In[108]:


char='-'
cars=['bmw', 'honda', 'toyota', 'benz', 'audi']
print(char.join(cars))
char='***'
print(char.join(cars))
char='\n'
print(char.join(cars))


# In[109]:


num=[2,3,8,5,2,[2,6,8]]
print(num[5][0])
print(num[5][1])
print(num[5][2])


# In[111]:


James=[['Lebron James','SF','12/30/84'],23,19,22,31,18]
games=len(James)
score_Max=max(James[1:games])
i=James.index(score_Max)
name=James[0][0]
position=James[0][1]
born=James[0][2]
print("name:%s"%name)
print("position:%s"%position)
print("born:%s"%born)
print("在第%d場分數最高:%d"%(i,score_Max))


# In[112]:


a=['bmw', 'honda', 'toyota']
b=['benz', 'bmw']
a.append(b)
print(a)


# In[114]:


a=['bmw', 'honda', 'toyota']
b=['benz', 'bmw']
a.extend(b)
print(a)


# In[5]:


#deep copy
mysport=['basketball','baseball']
friendsport=mysport #copy address
print(mysport)
print(friendsport)
print(id(mysport))
print(id(friendsport))
mysport.append('football')
friendsport.append('soccer')
print(mysport)
print(friendsport)
print(id(mysport))
print(id(friendsport))


# In[6]:


#shallow copy
mysport=['basketball','baseball']
friendsport=mysport[:]
print(mysport)
print(friendsport)
print(id(mysport))
print(id(friendsport))
mysport.append('football')
friendsport.append('soccer')
print(mysport)
print(friendsport)
print(id(mysport))
print(id(friendsport))


# In[7]:


string="python"
string[0]='d'


# In[10]:


string="python"
print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])
print(string[5])
print(string[-1])
print(string[-2])
print(string[-3])
print(string[-4])
print(string[-5])
print(string[-6])
s1,s2,s3,s4,s5,s6=string
print(s1,s2,s3,s4,s5,s6)


# In[11]:


string='Deep Learning'
print(string[0:3])
print(string[1:4])
print(string[1:6:2])
print(string[1:])
print(string[-3:])


# In[16]:


string='Deep Learning'
strlen=len(string)
strmax=max(string)
strmin=min(string)
print(strlen)
print(strmax)
print(strmin)


# In[20]:


string='python'
x=list(string)
print(x)


# In[24]:


x[1:]='hello'
print(x)


# In[26]:


str1='Silicon Stone Education'
str2='DeepDtone'
str3='深度學習'
str1list=str1.split()
str2list=str2.split()
str3list=str3.split()
print(str1list)
print(len(str1list))
print(str2list)
print(len(str2list))
print(str3list)
print(len(str3list))


# In[27]:


#in & not in to determine if an object belongs to another object
password='deepstone'
ch=input('input:')
if ch in password:
    print('belongs to password')
else:
    print('not belongs to password')
if ch not in password:
    print('not belongs to password')
else:
    print('belongs to password')


# In[28]:


fruits=['apple','banana','pineapple']
fruit=input('fruit:')
if fruit in fruits:
    print('already in fruits')
else:
    fruits.append(fruit)
    print('add into fruits')


# In[37]:


x=10
y=10
z=15
w=20
print(id(x),id(y),id(z),id(w))
z=10
print(id(x),id(y),id(z),id(w))
list1=['a','b','c']
list2=['a','b','c']
print(id(list1),id(list2)) #list seems not to point to the same address
str1='abc'
str2='abc'
print(id(str1),id(str2))


# In[40]:


#is & not is to determine if an object has the same address as another object
x=10
y=10
z=15
w=z-5
boolvalue=x is y
print(boolvalue)
boolvalue=x is z
print(boolvalue)
boolvalue=x is w
print(boolvalue)
boolvalue=x is not y
print(boolvalue)
boolvalue=x is not z
print(boolvalue)
boolvalue=x is not w
print(boolvalue)


# In[44]:


list1=['a','b','c']
list2=list1
list3=list1[:]
print(id(list1),id(list2),id(list3))
boolvalue=list1 is list2
print(boolvalue)
boolvalue=list1 is list3
print(boolvalue)
boolvalue=list1 is not list2
print(boolvalue)
boolvalue=list1 is not list3
print(boolvalue)


# In[49]:


#enumerate
drinks=['tea','coffee','wine']
x=enumerate(drinks)
print(x) #return an address
print(type(x))
print(list(x))
x=enumerate(drinks,start=10)
print(list(x))

