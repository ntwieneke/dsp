import pandas as pd


# In[24]:

df = pd.read_csv('python/faculty.csv')
df.head()


# In[25]:

df.columns


# In[26]:

df[' degree'].value_counts()


# In[36]:

df['clean_degree'] = df[' degree'].str.replace(".","").str.lower()


# In[37]:

df['clean_degree']


# In[38]:

degree_list = ['phd','scd','jd','ma','mph','ms','bs','ed','md']

for degree in degree_list:
    df[degree] = df['clean_degree'].str.contains(degree)


# In[39]:

df.head()


# In[46]:

for degree in degree_list:
    print str(degree) + ':' + str(sum(df[degree]))


# In[49]:

df[' title'].value_counts()


# In[64]:

prof_keywords = ['Associate','Assistant']
for key in prof_keywords:
    df[key] = df[' title'].str.contains(key)

df.head()


# In[68]:

# for row in df:
#     if df['Associate'][row] == False and df['Assistant'][row] == False:
#         df['Professor'][row] = True


# In[62]:

df.head()


# In[71]:

df.info


# In[75]:

total_nonprof = 0
for p in prof_keywords:
    total_nonprof += sum(df[p])
    print str(p) + ':' + str(sum(df[p]))
print "Professor" + ':' + str(37 - total_nonprof)


# In[76]:

email_list = list(df[' email'])
print email_list


# In[78]:


email_split = df[' email'].apply(lambda email: pd.Series(email.split('@')))
email_set = set(email_split[1])
print email_set


# In[79]:

df[' email'].to_csv('python/emails.csv')


# In[83]:

split = lambda x: x.split('')
name_split = [split for x in df['name']]


# In[84]:

print name_split


# In[ ]:

