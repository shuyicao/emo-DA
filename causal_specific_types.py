#!/usr/bin/env python
# coding: utf-8

#import libraries
import networkx as nx
import cdt

from cdt.data import load_dataset
import pandas as pd
import random
from rpy2.robjects.packages import importr
from matplotlib import pyplot as plt
import rpy2.robjects as robjects
import math

#import algorithms
from cdt.causality.graph import GIES
from cdt.causality.graph import MMPC

#indenpendence test 
from scipy import stats


#import required R packages
importr('pcalg')
importr('kpcalg')
importr('RCIT')
importr('bnlearn')


#read three dataframes

#current emo with current da
trans_curr = pd.read_csv(r'trans_curr.csv', encoding='unicode_escape')

#prev emo with current da
trans_prev = pd.read_csv(r'trans_prev.csv', encoding='unicode_escape')

#next emo with current da
trans_next = pd.read_csv(r'trans_next.csv', encoding='unicode_escape')



#add prefix to emotion of prev and next dataframe 

prev_names = [(i,'prev_'+i) for i in trans_prev.iloc[:, :8].columns.values]
trans_prev.rename(columns = dict(prev_names), inplace=True)

next_names = [(i,'next_'+i) for i in trans_next.iloc[:, :8].columns.values]
trans_next.rename(columns = dict(next_names), inplace=True)



#segment data to 1 emo with all da and remove column that are not related 
def input_data(emo, data):
    emo_d = data[emo]
    da_d = data[data.columns[-41:]]
    output = pd.concat([emo_d, da_d], axis=1)
    
    #remove columns with only one value
    binary_col = []
    for i in output.columns:
        if output[i].nunique() == 2:
            binary_col.append(i)

    binary_output = output[binary_col]

    #perform fisher's exact test
    for i in binary_output.columns[1:]:
        v1 = binary_output[emo]
        v2 = binary_output[i]
        crosstab = pd.crosstab(v1,v2)
        fisher = stats.fisher_exact(crosstab)[1]
        if fisher > 0.05:
            binary_output.drop(i, axis=1, inplace=True)
    
    return binary_output


#define function to run GIES where input data is numerical
def cause_effect(data, emo, alg):
    
    emo_data = input_data(emo, data)

    obj= alg()

    output = obj.predict(emo_data) 
    
    emo_n = ['no_emo', 'anger','disgust','fear','happiness','sadness','surprise', 'emo_null']
    da_n = ['Statement_non_opinion','Backchannel','Statement_opinion','Uninterpretable',
      'Agree_Accept','Appreciation','Yes_No_Question','Yes_Answers','Conventional_closing',
      'Wh_Question','No_Answers','Response_Acknowledgement','Hedge',
      'Declarative_Yes_No_Question','Backchannel_Question_Form','Quotation',
      'Summarize_Reformulate','Other','Affirmative_Non_yes_Answers','Action_directive',
      'Collaborative_Completion','Repeat_phrase','Open_Question','Rhetorical_Question',
      'Hold_Before_Answer','Reject','Negative_Non_no_Answers','Signal_non_understanding',
      'Other_Answers','Conventional_opening','Or_Clause','Dispreferred_Answers',
      'third_party_talk','Offers_Options_Commits','Maybe_Accept_part','Downplayer',
      'Self_talk','Tag_Question','Declarative_Wh_Question','Apology','Thanking']
    
    #remove unnecessary edges (emo - emo  &  da - da)
    for edge in list(output.edges):
        if edge[0] in emo_n and edge[1] in emo_n:
            output.remove_edge(edge[0],edge[1])
        elif edge[0] in da_n and edge[1] in da_n:
            output.remove_edge(edge[0],edge[1])
    
    #remove nodes not connecting with others
    for i in list(output.degree):
        if i[1] == 0:
            output.remove_node(i[0])

    #To view the graph created
    nx.draw_networkx(output, font_size=8)
    plt.show()
    
    #calculate the dependencies between each pair of causal relation
    dependency = []
    for i in list(output.edges):
        node1 = emo_data[i[0]]
        node2 = emo_data[i[1]]
        crosstab = pd.crosstab(node1,node2)
        fisher = stats.fisher_exact(crosstab)[1]
        dependency.append(fisher)
        

    causation = pd.DataFrame(list(output.edges), columns=['Cause', 'Effect'])
    causation['dependency'] = dependency
    #sort dataframe based on dependencies
    print(causation.sort_values(by=['dependency'], ascending=True))
    
    return causation



#define function to run MMPC where input data is string
def cause_effect_str(data, emo, alg):
    emo_data = input_data(emo, data)
    
    #convert input data to str values
    emo_data1 = emo_data.replace(0,'N')
    emo_data2 = emo_data1.replace(1, 'Y')

    obj= alg()

    output = obj.predict(emo_data2)    
    
    emo_n = ['no_emo', 'anger','disgust','fear','happiness','sadness','surprise', 'emo_null']
    da_n = ['Statement_non_opinion','Backchannel','Statement_opinion','Uninterpretable',
      'Agree_Accept','Appreciation','Yes_No_Question','Yes_Answers','Conventional_closing',
      'Wh_Question','No_Answers','Response_Acknowledgement','Hedge',
      'Declarative_Yes_No_Question','Backchannel_Question_Form','Quotation',
      'Summarize_Reformulate','Other','Affirmative_Non_yes_Answers','Action_directive',
      'Collaborative_Completion','Repeat_phrase','Open_Question','Rhetorical_Question',
      'Hold_Before_Answer','Reject','Negative_Non_no_Answers','Signal_non_understanding',
      'Other_Answers','Conventional_opening','Or_Clause','Dispreferred_Answers',
      'third_party_talk','Offers_Options_Commits','Maybe_Accept_part','Downplayer',
      'Self_talk','Tag_Question','Declarative_Wh_Question','Apology','Thanking']
    
    #remove unnecessary edges
    for edge in list(output.edges):
        if edge[0] in emo_n and edge[1] in emo_n:
            output.remove_edge(edge[0],edge[1])
        elif edge[0] in da_n and edge[1] in da_n:
            output.remove_edge(edge[0],edge[1])
    
    #remove nodes not connecting with others
    for i in list(output.degree):
        if i[1] == 0:
            output.remove_node(i[0])

    #To view the graph created
    nx.draw_networkx(output, font_size=8)
    plt.show()
    
    #calculate the dependencies between each pair of causal relation
    dependency = []
    for i in list(output.edges):
        node1 = emo_data[i[0]]
        node2 = emo_data[i[1]]
        crosstab = pd.crosstab(node1,node2)
        fisher = stats.fisher_exact(crosstab)[1]
        dependency.append(fisher)
        

    causation = pd.DataFrame(list(output.edges), columns=['Cause', 'Effect'])
    causation['dependency'] = dependency
    #sort dataframe based on dependencies
    print(causation.sort_values(by=['dependency'], ascending=True))
    
    return causation


# # Current emo vs. current DA

#for iterate through each type of emo
emo_list = ['anger','disgust','fear','happiness','sadness','surprise']


# ### Greedy Interventional Equivalence Search

random.seed(123)
for emo in emo_list:
    print('current ' + emo)
    cause_effect(trans_curr, emo, GIES)


# ### Max-Min Parents-Children

random.seed(123)
for emo in emo_list:
    print('current ' + emo)
    cause_effect_str(trans_curr, emo, MMPC)


    
# # Previous emotion vs. current DA

#for iterate through each type of emo
prev_emo_list = ['prev_anger','prev_disgust','prev_fear','prev_happiness','prev_sadness','prev_surprise']


# ### Greedy Interventional Equivalence Search

random.seed(123)
for emo in prev_emo_list:
    print('previous utterance emotion is ' + emo)
    cause_effect(trans_prev, emo, GIES)


# ### Max-Min Parents-Children 

random.seed(123)
for emo in prev_emo_list:
    print('previous utterance emotion is  ' + emo)
    cause_effect_str(trans_prev, emo, MMPC)


