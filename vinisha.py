#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[31]:


df=pd.read_csv('D:\arabica_ratings_raw.csv',encoding='latin-1')
df.head()


# In[3]:


df=pd.read_csv('d:\\arabica_ratings_raw.csv',encoding='latin-1')
df.head()


# In[4]:


df.describe()


# In[5]:


df.info()


# In[6]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12, 6)
sns.barplot(x="Owner",y="quality_score",data=df)


# In[7]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12, 6)
sns.barplot(x="Flavor",y="Acidity",data=df)


# In[8]:


plt.pie(Owner_val[:60],labels=Owner_names[:50],autopct='%1.2f%%'


# In[9]:


plt.pie(Owner_val[:60],labels=Owner_names[:50],autopct='%1.2f%%'


# In[10]:


Owner_names=final_df.Owner.value_counts().index


# In[11]:


Owner_names=df.Owner.value_counts().index


# In[12]:


country_val=df.Country.value_counts().values


# In[13]:


Owner_val=df.Owner.value_counts().values


# In[14]:


plt.pie(Owner_val[:60],labels=Owner_names[:50],autopct='%1.2f%%'


# In[15]:


plt.pie(Owner_val[:3],labels=Owner_names[:3],autopct='%1.2f%%'


# In[16]:


plt.pie(Owner_val[:3],labels=Owner_names[:3],autopct='%1.2f%%')


# In[17]:


df.corr()


# In[18]:


sns.heatmap(df.corr())


# In[19]:


df.isnull().sum()


# In[21]:


df['Flavor'].count()


# In[22]:


sns.countplot(x="Flavor",data=df,palette=['blue','red','orange','yellow','green','green'])


# In[23]:


sns.jointplot(x='Flavor',y='Acidity',data=df,kind='hex')


# In[25]:


sns.distplot(df['Flavor'])


# In[27]:


sns.countplot('Flavor',data=df)


# In[28]:


sns.boxplot('Flavor','Acidity', data=df)


# In[29]:


sns.violinplot(x="Flavor", y="Acidity", data=df,palette='rainbow')


# In[ ]:




