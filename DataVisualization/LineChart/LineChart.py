
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


from matplotlib import pyplot as plt


# In[6]:


a=[1,2,3]
b=[1,4,9]


# In[23]:


plt.plot(a,b)
plt.title("Test")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


# In[24]:


x=[1,3,6]
y=[1,9,36]
z=[1,27,216]


# In[25]:


plt.plot(x,y)
plt.plot(x,z)
plt.title("Test")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["x and y","x and z"])
plt.show()


# In[26]:


SimpleData=pd.read_csv("SimpleData.csv")


# In[31]:


SimpleData


# In[32]:


SimpleData.column_c


# In[33]:


SimpleData.column_c.iloc[1]


# In[34]:


type(SimpleData)


# In[35]:


type(SimpleData.column_c)


# In[36]:


type(SimpleData.column_c.iloc[1])


# In[42]:


plt.plot(SimpleData.column_a,SimpleData.column_b)
plt.plot(SimpleData.column_a,SimpleData.column_c)
plt.title("SimpleData")
plt.xlabel("column_a")
plt.ylabel("column_b and column_c")
plt.legend(["column_a and column_b","column_a and column_c"])
plt.show()


# In[44]:


plt.plot(SimpleData.column_a,SimpleData.column_b,'o')
plt.plot(SimpleData.column_a,SimpleData.column_c)
plt.title("SimpleData")
plt.xlabel("column_a")
plt.ylabel("column_b and column_c")
plt.legend(["column_a and column_b","column_a and column_c"])
plt.show()


# In[45]:


CountryPopulation=pd.read_csv("CountryPopulation.csv")


# In[46]:


CountryPopulation


# In[50]:


US=CountryPopulation[CountryPopulation.country=="United States"]


# In[51]:


US


# In[52]:


China=CountryPopulation[CountryPopulation.country=="China"]


# In[53]:


China


# In[60]:


plt.plot(US.year,US.population/10**6)
plt.plot(China.year,China.population/10**6)
plt.xlabel("Year")
plt.ylabel("Population (million)")
plt.title("Country's Population")
plt.legend(["US","China"])
plt.show()


# In[63]:


plt.plot(US.year,US.population/US.population.iloc[0]*100)
plt.plot(China.year,China.population/China.population.iloc[0]*100)
plt.xlabel("Year")
plt.ylabel("Population Growth (First Year = 100)")
plt.title("Country's Population Growth")
plt.legend(["US","China"])
plt.show()

