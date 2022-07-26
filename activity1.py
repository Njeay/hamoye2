#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd


# In[15]:


df = pd.read_csv("FoodBalanceSheets_e_Africa_NOFLAG.csv", encoding="latin1")


# In[16]:


df


# In[26]:


df.describe()


# In[31]:


import pandas as pd


# In[32]:


import numpy as np


# In[34]:


df.isnull().sum()


# In[36]:


df.groupby('Area')['Area'].count()


# In[39]:


a= df.groupby(['Element', 'Y2014']


# In[ ]:




