# query_dataset

This is a primitive 'dataset search engine'. It takes a text file
with queries and then matchs and scores against a datatset of lines
consisting of 3 elements [id, item, brand].
It outputs the number of matches per query, the items matched and
their score ordered by descending score.

Scoring could be improved as only measuring:
Number of key-word occurances in entry
Full match (non-case sensitive)
Partial match on word beginning

names of files:

most developed version with fastest search:
edited_better_ds.py

queries.txt
search_dataset.csv

Runs on Python 3
