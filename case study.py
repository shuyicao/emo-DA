#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import collections
import numpy as np


# In[34]:


#read the file
case = pd.read_csv('/Users/admin/Desktop/annotated.csv', encoding='unicode_escape')
case


# In[37]:


case[['emo','prev_emo','next_emo','swda','prev_swda','next_swda']].describe()


# In[40]:



case['swda'].value_counts()


# In[27]:


def frequency(emo_feature, da_feature, emo):
    print('the DA frequency for ' + emo + ' is ' )
    df = list(case.loc[case[emo_feature]==emo, da_feature])
    df_fre = collections.Counter(df)
    df_fre = df_fre.most_common()
    
    return df_fre


# ## current emo vs. current da

# In[29]:


print(frequency('emo','swda', 'anger'))
print(frequency('emo','swda', 'disgust'))
print(frequency('emo','swda', 'fear'))
print(frequency('emo','swda', 'happiness'))
print(frequency('emo','swda', 'sadness'))
print(frequency('emo','swda', 'surprise'))


# ## previous emo vs. current da

# In[30]:


print(frequency('prev_emo','swda', 'anger'))
print(frequency('prev_emo','swda', 'disgust'))
print(frequency('prev_emo','swda', 'fear'))
print(frequency('prev_emo','swda', 'happiness'))
print(frequency('prev_emo','swda', 'sadness'))
print(frequency('prev_emo','swda', 'surprise'))


# ## current emo vs. previous da

# In[41]:


print(frequency('emo','prev_swda', 'anger'))
print(frequency('emo','prev_swda', 'disgust'))
print(frequency('emo','prev_swda', 'fear'))
print(frequency('emo','prev_swda', 'happiness'))
print(frequency('emo','prev_swda', 'sadness'))
print(frequency('emo','prev_swda', 'surprise'))


# ## current emo vs. next da

# In[31]:


print(frequency('emo','next_swda', 'anger'))
print(frequency('emo','next_swda', 'disgust'))
print(frequency('emo','next_swda', 'fear'))
print(frequency('emo','next_swda', 'happiness'))
print(frequency('emo','next_swda', 'sadness'))
print(frequency('emo','next_swda', 'surprise'))


# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




