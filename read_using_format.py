#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


datexx = '221024'


# In[4]:


df = pd.read_csv('marketing{}.csv'.format(datexx), sep='\t')
df.head(5)


# In[ ]:




