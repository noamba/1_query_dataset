"""
Note: This is the initial phase of this exercise. As I moved on from it
pretty quickly  I didn't spend much time and effort on it.
For better  code and comments see 'search_app_improved.py'.
"""


import csv


def main(dataset, queries_file, print_output):
    dataset = load_dataset(dataset)
    process_query_file(queries_file, print_output,  dataset)


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
        score = calculate_score(keywords, entry)
        if score > 0:
            matches += 1
            results.append([str(score)] + entry)

    return (matches, results)


def calculate_score(keywords, entry):

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
    main('data/search_dataset.csv', 'queries/queries.txt', True)
