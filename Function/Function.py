
# coding: utf-8

# In[1]:


#This is a practice
def printfunction():
    print("Hi!")
    print("I'm function")
print("Out of function")


# In[4]:


printfunction()


# In[5]:


def doublefunction(x):
    return 2*x


# In[7]:


a=doublefunction(2)
print(a)


# In[8]:


def plusfunction(x,y):
    return x+y


# In[11]:


b=plusfunction(2,3)
print(b)


# In[21]:


def function(x):
    print(x)
    print("I'm in the function")
    return 3*x


# In[14]:


c=function(3)


# In[15]:


print(c)


# In[24]:


def function2(x):
    print(x)
    print("I'm in the function")


# In[25]:


function2(3)


# In[14]:


def greeting(name):
    print('Hi!'+name+'. How are you?')


# In[16]:


greeting('Jimmy')


# In[17]:


def sub(x,y):
    return x-y


# In[18]:


a=int(input('a:'))
b=int(input('b:'))
c=sub(a,b)
print(c)


# In[2]:


def interest(a,b):
    print(a+' is my favorite sport')
    print(b+' is my favorite fruit')
interest(b='banana',a='basketball')


# In[6]:


def interest(a,b='apple'):#如有預設的,要放在最右邊
    print(a+' is my favorite sport')
    print(b+' is my favorite fruit')
    print()
interest('basketball')
interest(a='basketball')
interest('basketball','banana')
interest(a='basketball',b='banana')
interest(b='banana',a='basketball')


# In[9]:


def test(a):
    print(a)
a=test('hi')#自動return none
print(a)
print(type(a))


# In[8]:


def test(a):
    print(a)
    return
a=test('hi')
print(a)
print(type(a))


# In[10]:


def subtract(a,b):
    x=a-b
    return x
a=int(input('a:'))
b=int(input('b:'))
print('a-b=',subtract(a,b))


# In[13]:


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
print('1:add')
print('2:sub')
x=int(input('1/2:'))
a=int(input('a:'))
b=int(input('b:'))
if x==1:
    print('a+b=',add(a,b))
elif x==2:
    print('a-b=',sub(a,b))
else:
    print('error')


# In[14]:


def op(x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    return a,b,c,d
a=10
b=10
add,sub,mul,div=op(a,b)
print('add',add)
print('sub',sub)
print('mul',mul)
print('div',div)


# In[15]:


def greet(name,gender):
    if gender=='M':
        x=name+'先生歡迎您'
    else:
        x=name+'小姐歡迎您'
    return x
name=input('name:')
gender=input('gender(M/F):')
x=greet(name,gender)
print(x)


# In[16]:


def dic(id,name):
    x={'id':id,'name':name}
    return x
x=dic('a','Jimmy')
print(x)


# In[19]:


def dic(id,name,tel=''):
    x={'id':id,'name':name}
    if tel:
        x['tel']=tel
    return x
x=dic('a','Jimmy')
y=dic('b','Tom','123456789')
print(x)
print(y)


# In[1]:


def dic(id,name,tel=''):
    x={'id':id,'name':name}
    if tel:
        x['tel']=tel
    return x
while True:
    id=input('id:')
    name=input('name:')
    tel=input('tel:')
    x=dic(id,name,tel)
    print(x)
    repeat=input('Y/N:')
    if repeat=='N':
        break


# In[1]:


def abc(x):
    str1='banana'
    for i in x:
        str2=i+' loves '+str1
        print(str2)
x=['Jimmy','Amy','Ruby']
abc(x)


# In[4]:


def kitchen(unserved,served):
    print('廚房處理顧客所點的餐點')
    while unserved:
        current_meal=unserved.pop()
        print('菜單:',current_meal)
        served.append(current_meal)

def show_unserved_meal(unserved):
    print('===下列是尚未服務的餐點===')
    if not unserved:
        print('***沒有餐點***','\n')
    for unserved_meal in unserved:
        print(unserved_meal)

def show_served_meal(served):
    print('===下列是已經服務的餐點===')
    if not served:
        print('***沒有餐點***','\n')
    for served_meal in served:
        print(served_meal)    

unserved=['大麥克','勁辣雞腿堡','麥克雞塊']
served=[]
show_unserved_meal(unserved)
show_served_meal(served)
kitchen(unserved,served)
print('\n','===廚房處理結束===','\n')
show_unserved_meal(unserved)
show_served_meal(served)

