#!/usr/bin/env python

import warnings as warn
import sys
import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

warn.filterwarnings('ignore')


def calculate_cosine_similarity(data_items):
  data_sparse = sparse.csr_matrix(data_items)
  similarities = cosine_similarity(data_sparse.transpose())
  sim = pd.DataFrame(data=similarities, index=data_items.columns,
                     columns=data_items.columns)
  return sim


def similarity_function(signals_csv):
  print('Read CSV with signals')
  df = pd.read_csv('./signals/' + signals_csv, encoding='latin-1')
  df.head()

  print('Create DataFrame with only user_id and tag_id column')
  user_tag_view = pd.DataFrame(df, columns=['user_id', 'tag_id'])
  user_tag_view.head()

  print('Count unique users and tags are in the sample')
  n_users = df.user_id.unique().shape[0]
  n_tags = df.tag_id.unique().shape[0]
  print(
      'Number of users = ' + str(n_users) + ' | Number of tags = ' + str(n_tags))

  print('Add column of action with value 1')
  user_tag_view['view'] = '1'
  user_tag_view.head()

  print('Create Pivot table')
  viewPivot = user_tag_view.pivot_table(index=['user_id'],
                                        columns=['tag_id'],
                                        values='view',
                                        aggfunc=lambda x: len(x.unique()),
                                        fill_value=0)
  viewPivot.head()

  print('Reindex DataFrame to remove the user data')
  viewPivot.reset_index(inplace=True)
  viewPivot = viewPivot.drop('user_id', axis=1)
  viewPivot.head()

  magnitude = np.sqrt(np.square(viewPivot).sum(axis=1))
  dataViewPivot = viewPivot.divide(magnitude, axis='index')

  print('Create temp matrix to store the similarity')
  data_matrix = calculate_cosine_similarity(dataViewPivot)

  print('Top 10 tags with their recommended tags')
  print(data_matrix.loc['ff0d3fb21c00bc33f71187a2beec389e9eff5332'].nlargest(11))

  print('Save data to csv to use in your own recommendation system')
  data_matrix.to_csv('./results/temp_matrix_result.csv')
  data_matrix.loc['ff0d3fb21c00bc33f71187a2beec389e9eff5332'].nlargest(11).to_csv(
    './results/similar_result.csv')


similarity_function(sys.argv[1])
