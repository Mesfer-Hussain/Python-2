#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd 
 
yelp_raw_data = pd.read_csv("yelp.csv") 
 
yelp_raw_data.head()


# In[3]:


yelp_raw_data.shape


# In[4]:


type(yelp_raw_data) 


# In[5]:


yelp_raw_data['business_id'] # grabs a single column of the Dataframe 


# In[8]:


type(yelp_raw_data['business_id']) 


# In[9]:


yelp_raw_data['business_id'].describe() 


# In[10]:


yelp_raw_data['review_id'].describe() 


# In[11]:


yelp_raw_data['text'].describe()


# In[12]:


yelp_raw_data['text'].describe()['top'] 


# In[13]:


duplicate_text = yelp_raw_data['text'].describe()['top']


# In[14]:


yelp_raw_data['text'].describe()['top'] 


# In[15]:


text_is_the_duplicate = yelp_raw_data['text'] == duplicate_text


# In[16]:


type(text_is_the_duplicate) # it is a Series of Trues and Falses


# In[17]:


text_is_the_duplicate.head() # shows a few Falses out of the Series


# In[18]:


sum(text_is_the_duplicate) # == 2


# In[19]:


filtered_dataframe = yelp_raw_data[text_is_the_duplicate]


# In[20]:


filtered_dataframe


# In[21]:


yelp_raw_data['type'].describe()


# In[22]:


yelp_raw_data['user_id'].describe()


# In[23]:


yelp_raw_data['stars'].describe()


# In[24]:


yelp_raw_data['stars'].value_counts()


# In[27]:


import datetime
dates = yelp_raw_data['stars'].value_counts()
dates.sort_values
dates.plot(kind='bar')


# In[29]:


import pandas as pd
titanic = pd.read_csv('short_titanic.csv')
titanic.head()


# In[ ]:





# In[ ]:




