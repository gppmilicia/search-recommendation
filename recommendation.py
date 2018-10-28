#!/usr/bin/env python

import warnings as warn
from datetime import datetime as dt

import pandas as pd
from scipy.spatial.distance import cosine

warn.filterwarnings('ignore')

# Read CSV with signals
df = pd.read_csv('./signals/21B_tag_views_dataset.csv', encoding='latin-1')
df.head()

# Create DataFrame with only user_id and tag_id column
user_tag_view = pd.DataFrame(df, columns=['user_id', 'tag_id'])
user_tag_view.head()

# Count unique users and tags are in the sample
n_users = df.user_id.unique().shape[0]
n_tags = df.tag_id.unique().shape[0]
print(
    'Number of users = ' + str(n_users) + ' | Number of tags = ' + str(n_tags))

# add column of action with value 1
user_tag_view['view'] = '1'
user_tag_view.head()

# Create Pivot table
viewPivot = user_tag_view.pivot_table(index=['user_id'],
                                      columns=['tag_id'],
                                      values='view',
                                      aggfunc=lambda x: len(x.unique()),
                                      fill_value=0)
viewPivot.head()

# Reindex DataFrame to remove the user data
viewPivot.reset_index(inplace=True)
viewPivot = viewPivot.drop('user_id', axis=1)
viewPivot.head()

# Create temp matrix to store the similarity
tmpViewMatrix = pd.DataFrame(index=viewPivot.columns, columns=viewPivot.columns)
tmpViewMatrix.head()

# Start calculating the similarity
print(dt.now().strftime("%Y-%m-%d %H:%M"))

for i in range(0, len(tmpViewMatrix.columns)):
  for j in range(0, len(tmpViewMatrix.columns)):
    tmpViewMatrix.ix[i, j] = 1 - cosine(viewPivot.ix[:, i], viewPivot.ix[:, j])

tmpViewMatrix.head()

print(dt.now().strftime("%Y-%m-%d %H:%M"))

# Create DataFrame with ordered tags by similarity
similarTags = pd.DataFrame(index=tmpViewMatrix.columns,
                           columns=range(1, len(tmpViewMatrix.columns)))
for i in range(0, len(tmpViewMatrix.columns)):
  similarTags.ix[i, :len(tmpViewMatrix.columns) - 1] = tmpViewMatrix.ix[
                                                       0:, i].sort_values(
    ascending=False)[:len(tmpViewMatrix.columns) - 1].index

# Top 10 tags with their recommended tags
topSimilarTags = similarTags.head(10).ix[:10, 2:11]

print(dt.now().strftime("%Y-%m-%d %H:%M"))

# Save data to csv to use in your own recommendation system
tmpViewMatrix.to_csv('temp_matrix_result.csv')
topSimilarTags.to_csv('similar_result.csv')
