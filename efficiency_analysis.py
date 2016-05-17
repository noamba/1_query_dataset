#!/usr/bin/python3

import timeit

# Benchmark:

number=1 # times the tested function is run for timing
repeat=2 # test is repeated to get multiple results 


print("**** Dataset as Dictionaries ****")
setup = "import search_app_improved as e"
setup_with_loaded_dataset = setup + "; data_set = e.load_dataset('search_dataset.csv')"

print("Time to load dataset: ")
print(timeit.repeat("e.load_dataset('search_dataset.csv')", setup=setup, number=number, repeat=repeat))


print("Time to process query file without printing output: ")
print(timeit.repeat("e.process_query_file('queries.txt', False, *data_set)", setup=setup_with_loaded_dataset, number=number, repeat=repeat))


print("\n\n**** Dataset as List ****")
setup = "import search_app_base as e"
setup_with_loaded_dataset = setup + "; data_set = e.load_dataset('search_dataset.csv')"

print("Time to load dataset: ")
print(timeit.repeat("e.load_dataset('search_dataset.csv')", setup=setup, number=number, repeat=repeat))


print("Time to process query file without printing output: ")
print(timeit.repeat("e.process_query_file('queries.txt', False, data_set)", setup=setup_with_loaded_dataset, number=number, repeat=repeat))

