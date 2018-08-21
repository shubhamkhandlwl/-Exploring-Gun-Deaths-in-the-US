
# coding: utf-8

# In[4]:


import csv
f = open('guns.csv', 'r') 
data =list(csv.reader(f))
data[0:5]


# In[5]:


headers = data[:1]
data = data[1:]
print(headers)
print(data[:5])


# In[8]:


years = [row[1] for row in data]
year_counts = {}
for year in years:
    if year in year_counts:
        year_counts[year] = year_counts[year] + 1
    else:
        year_counts[year] = 1
year_counts


# In[9]:


import datetime
dates = []
for row in data:
    year = int(row[1])
    month = int(row[2])
    date = datetime.datetime(year = year, month = month, day = 1)
    dates.append(date)
dates[0:5]


# In[10]:


date_counts = {}
for each in dates:
    if each in date_counts:
        date_counts[each] = date_counts[each] + 1
    else:
        date_counts[each] = 1
date_counts
        


# In[13]:


def col_counts(input):
    column = {}
    for each in data:
        if each[input] in column:
            column[each[input]] = column[each[input]] + 1
        else:
            column[each[input]] = 1
    return column
sex_counts = col_counts(5)
race_counts = col_counts(7)
sex_counts


# In[14]:


race_counts


# After analysing the deaths by gun in America on the basis of year, month, sex, race. I have learned that year and month do not have any effect on deaths. However, it can be easily noticed that in respect to sex, deaths are highly gender biased. Only if we know the total population's race ratio, we can comment on the deaths by race.

# In[17]:


f = open('census.csv', 'r')
census = list(csv.reader(f))
census


# In[25]:


mapping = {
"Asian/Pacific Islander" : 15159516 + 674625,
"Black" : 40250635,
"Hispanic" : 44618105,
"Native American/Native Alaskan" : 3739506,
"White" : 197318956
}
mapping


# In[26]:


race_per_hundredk = {}
for k,v in race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk


# In[27]:


intents = [row[3] for row in data]
races = [row[7] for row in data]
homicide_race_counts = {}
for i,race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i] == "Homicide":
        homicide_race_counts[race] += 1

race_per_hundredk = {}
for k,v in homicide_race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk


# It appears that gun related homicides in the US disproportionately affect people in the Black and Hispanic racial categories.
