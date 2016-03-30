df['first_name'] = df['name'].str.split(' ').str.get(0)
df['first_name'].head()


# In[32]:

df['last_name'] = df['name'].str.rsplit(' ', n=1).str.get(1)
df['last_name'].head()


# In[36]:

df[['first_name','last_name']].head()


# In[37]:

df.head()


# In[49]:

df.loc[1]['name']


# In[56]:

Professorship = []

for index, row in df.iterrows():
    if row['Associate'] == True:
        Professorship.append('Associate')
#         row['Professorship'] = 'Associate'
    elif row['Assistant'] == True:
        Professorship.append('Assistant')
#         row['Professorship'] = 'Assistant'
    else:
        Professorship.append('Professor')
#         row['Professorship'] = 'Professor'

df['Professorship'] = Professorship
df.head()


# In[42]:




# In[92]:


info = []
for index, row in df.iterrows():
        info.append([row['clean_degree'],row['Professorship'],row[' email']])

df['info'] = info
df.head()


# In[93]:

df_dict = df[['last_name','info']]
df_dict.head()


# In[95]:


new_dict = df_dict.set_index('last_name')['info'].T.to_dict()
print new_dict


# In[84]:

new_dict['Bellamy']


# In[100]:

name_tuple = zip(df['first_name'],df['last_name'])

df['name_tuple'] = name_tuple

df.head()


# In[101]:

df_dict = df[['name_tuple','info']]
df_dict.head()


# In[104]:

new_dict_tuple = df_dict.set_index('name_tuple')['info'].T.to_dict()
print new_dict_tuple


# In[107]:

df_sorted = df.sort_values(by='last_name', ascending=True)
df_sorted.head()


# In[108]:

df_dict_sorted = df_sorted[['name_tuple','info']]
df_dict_sorted.head()


# In[109]:

new_dict_tuple_sorted = df_dict_sorted.set_index('name_tuple')['info'].T.to_dict()
print new_dict_tuple_sorted


# In[ ]:



