#!/usr/bin/python3

"""
Hello,

This is a primitive 'search engine'. It takes a file with queries and then
matchs and scores against a datatset of lines
consisting of 3 elements [id, item, brand].
It outputs the numberof matches per query, the items matached and
their score ordered by descending score.

Scoring could be improved as only measuring:print
Number of key-word occurances in entry
Full match but non-case sensitive
Partial match on word beginnin

names of files:

queries.txt
search_dataset.csv

Ruins on Python 2 and 3
"""
import csv


def main():
    dataset = load_dataset('search_dataset.csv')
    process_query_file('queries.txt', True,  dataset)


def load_dataset(dataset_file):
    dataset = []
    with open(dataset_file) as f:
        for line in f:
            # read csv into a list of lists
            dataset = list(list(rec) for rec in csv.reader(f, delimiter=','))

    return dataset


def process_query_file(file, print_output, dataset):
    with open(file) as f:
        for query_line in f:
            matches, results = process_query(query_line, dataset)
            if matches > 0 and print_output:
                print_results(query_line, matches, results)


def process_query(query, dataset):

    keywords = query.split()

    matches = 0
    results = []

    # score every line in dataset against query keywords
    for entry in dataset:
        score = calculate_score_1(keywords, entry)
        if score > 0:
            matches += 1
            results.append([str(score)] + entry)

    return (matches, results)


def calculate_score(keywords, entry):

    entry_line = entry[2] + " " + entry[1]
    entry = entry_line.split()

    score = 0
    for kw in keywords:
        for word in entry:
            if kw == word:
                score += 1
            elif kw.lower() == word.lower():
                score += 0.8
            elif word.startswith(kw):
                score += 0.5

    if score > 0:
        score = (float(score)/len(entry))

    return score


def calculate_score_1(keywords, entry):

    entry_line = entry[2] + " " + entry[1]
    entry = set(entry_line.split())

    score = 0
    for kw in keywords:
        for word in entry:
            if kw.lower() == word.lower():
                score += 1
            elif word.lower().startswith(kw.lower()):
                score += 0.5

    if score > 0:
        score = (float(score)/len(entry))

    return score


def print_results(query_line, matches, results):

    print (query_line, matches)

    results.sort(reverse=True)  # Will sort automatically by first element
    results = results[:10]
    for r in results:
        print (','.join(r))
    print ()

    return


if __name__ == "__main__":
    main()
