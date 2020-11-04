#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import cdt

from cdt.data import load_dataset
import pandas as pd
#import pypeR as pr
from rpy2.robjects.packages import importr

from matplotlib import pyplot as plt
import rpy2.robjects as robjects
from cdt.independence.stats import MIRegression


# In[ ]:





# In[2]:


importr('bnlearn')


# In[ ]:





# In[4]:


#read data
dd = pd.read_csv(r"C:\Users\shuyi\Desktop\input data\pred.csv", encoding='unicode_escape')
an = pd.read_csv(r"C:\Users\shuyi\Desktop\input data\annotated.csv", encoding='unicode_escape')

dd.head()


# In[5]:


#select columns to feed into the MMPC model
#string data type
dd_ = dd[['emo','prev_emo','next_emo','swda','prev_swda','next_swda']]
an_ = an[['emo','prev_emo','next_emo','swda','prev_swda','next_swda']]

#combine all sessions
new = pd.concat([an_, dd_], axis=0)


#select columns to feed into the GIES model
#numerical data type
dd_indx = dd[['emo_indx','prev_emo_indx','next_emo_indx',
              'swda_indx','prev_swda_indx','next_swda_indx']]
an_indx = an[['emo_indx','prev_emo_indx','next_emo_indx',
              'swda_indx','prev_swda_indx','next_swda_indx']]

#combine all sessions
new_indx = pd.concat([dd_indx, an_indx], axis=0)
#convert to categorical data type
new_indx.astype('category')


# In[9]:


emo_n = ['emo','prev_emo','next_emo']
da_n = ['swda','prev_swda','next_swda']
emo_indx_n = ['emo_indx','prev_emo_indx','next_emo_indx']
da_indx_n = ['swda_indx','prev_swda_indx','next_swda_indx']


# In[15]:


count = 0
for i in t.index:
    for c in t.columns:
        if t.at[i,c] < 5:
            count += 1


# In[6]:


from cdt.causality.graph import MMPC

obj_MMPC = MMPC()

output_MMPC = obj_MMPC.predict(new) 

nx.draw_networkx(output_MMPC, node_size=400, font_size=10)
plt.show()


print(pd.DataFrame(list(output_MMPC.edges), columns=['Cause', 'Effect']))


# In[10]:


#remove unnecessary edges
for edge in list(output_MMPC.edges):
    if edge[0] in emo_n and edge[1] in emo_n:
        output_MMPC.remove_edge(edge[0],edge[1])
    elif edge[0] in da_n and edge[1] in da_n:
        output_MMPC.remove_edge(edge[0],edge[1])
        
#remove nodes not connecting with others
for i in list(output_MMPC.degree):
    if i[1] == 0:
        output_MMPC.remove_node(i[0])
        
        
nx.draw_networkx(output_MMPC, node_size=400, font_size=10)
plt.show()

causation_mmpc = pd.DataFrame(list(output_MMPC.edges), columns=['Cause', 'Effect'])


# In[11]:


#rank the found edges by MI
mmpc_dependency = []
for i in list(output_MMPC.edges):
    node1 = new_indx[i[0]+'_indx']
    node2 = new_indx[i[1]+'_indx']
    obj = MIRegression()
    mi = obj.predict(node1, node2)
    mmpc_dependency.append(mi)
    
causation_mmpc['dependency'] = mmpc_dependency
print(causation_mmpc.sort_values(by=['dependency'], ascending=False))


# In[16]:


from cdt.causality.graph import GIES


obj_gies = GIES()

output_gies = obj_gies.predict(new_indx)   

nx.draw_networkx(output_gies, font_size=8)
plt.show()


print(pd.DataFrame(list(output_gies.edges), columns=['Cause', 'Effect']))


# In[17]:


#remove unnecessary edges
for edge in list(output_gies.edges):
    if edge[0] in emo_indx_n and edge[1] in emo_indx_n:
        output_gies.remove_edge(edge[0],edge[1])
    elif edge[0] in da_indx_n and edge[1] in da_indx_n:
        output_gies.remove_edge(edge[0],edge[1])
        
#remove nodes not connecting with others
for i in list(output_gies.degree):
    if i[1] == 0:
        output_gies.remove_node(i[0])
        


# In[18]:


output_gies.remove_edge('next_emo_indx','swda_indx')
output_gies.remove_edge('next_swda_indx','prev_emo_indx')

        
nx.draw_networkx(output_gies, node_size=400, font_size=10)
plt.show()

causation_gies = pd.DataFrame(list(output_gies.edges), columns=['Cause', 'Effect'])
causation_gies


# In[19]:


gies_dependency = []
for i in list(output_gies.edges):
    node1 = new_indx[i[0]]
    node2 = new_indx[i[1]]
    obj = MIRegression()
    mi = obj.predict(node1, node2)
    gies_dependency.append(mi)


causation_gies['dependency'] = gies_dependency
print(causation_gies.sort_values(by=['dependency'], ascending=False))


# In[20]:


#for clearer plot of relations
pos = nx.spectral_layout(output_gies)
nx.draw_networkx(output_gies, node_size=700, font_size=9, pos=pos)
plt.show()


# In[ ]:





# In[ ]:




