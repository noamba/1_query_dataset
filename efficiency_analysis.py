import timeit
import cProfile  
 
import search_app_base as base_search
import search_app_improved as improved_search


def average_dict_width(dictionary):

    dictionary_length = len(dictionary)

    total_values = 1
    for v in dictionary.values():
        total_values += len(v)    

    return dictionary_length, total_values/dictionary_length

def main():
    
    # SETTINGS for all profiling/benchmarking
    #dataset = 'data/mini.csv'
    dataset = 'data/search_dataset.csv'
    queries_file = 'queries/queries.txt'

    descriptive_data(dataset, queries_file)   
    timeit_benchmark(dataset, queries_file)
    cprofile_benchmark(dataset, queries_file)


def descriptive_data(dataset, queries_file):
        
        print("\n\n______General descriptive information_______")
        # find number of queries  to be processed:
        with open(queries_file) as f:
            print("\n    Number of queries (lines) in queries file (" + queries_file + "): ",  sum(1 for __ in f))

        with open(dataset) as f:
            print("    Number of items (lines) in dataset file (" + dataset + "): ",  sum(1 for __ in f))

        print("\nDescriptive information for search_app_improved: ")
        items_by_keyword_start, items_by_id, items_original_form = improved_search.load_dataset(dataset)
        length, width = average_dict_width(items_by_keyword_start)
        print("\n    Keyword (first letters) Dictionary entries: ", length) 
        print("    Keyword (first letters) Dictionary avg. width (wider is slower): ", width)
        

def timeit_benchmark(dataset, queries_file):   # Benchmarking with timeit:
    """
    Provides specific timings for loading the dataset and processing it.
    Benchmarks:
    1. Base and improved search_apps.
    2. Cythonised version of the improved search_app.
    """
    number=1 # times the tested function is run for timing
    repeat=2 # test is repeated to get multiple results 
    

    print("\n\n________PROFILING with timeit_________")
    print("\n**** Dataset as List (search_app_base) ****")
    setup = "import search_app_base as e"
    setup_with_loaded_dataset = setup + "; data_set = e.load_dataset('" + dataset + "')"

    print("Time to load dataset: ")
    print(timeit.repeat("e.load_dataset('" + dataset + "')", setup=setup, number=number, repeat=repeat))

    print("Time to process query file (no dataset loading, no printout): ")
    print(timeit.repeat("e.process_query_file('" + queries_file + "', False, data_set)", setup=setup_with_loaded_dataset, number=number, repeat=repeat))


    print("\n\n**** Dataset as Dictionaries (search_app_improved)****")
    setup = "import search_app_improved as e"
    setup_with_loaded_dataset = setup + "; data_set = e.load_dataset('" + dataset + "')"

    print("Time to load dataset: ")
    print(timeit.repeat("e.load_dataset('" + dataset + "')", setup=setup, number=number, repeat=repeat))


    print("Time to process query file (no dataset loading, no printout): ")
    print(timeit.repeat("e.process_query_file('" + queries_file + "', False, data_set)", setup=setup_with_loaded_dataset, number=number, repeat=repeat))


    print("\n\n**** In Cython (cythonised search_app_improved) ****")
    setup = "import c_search_app_improved as e"
    setup_with_loaded_dataset = setup + "; data_set = e.load_dataset('data/search_dataset.csv')"

    print("Time to load dataset: ")
    print(timeit.repeat("e.load_dataset('" + dataset + "')", setup=setup, number=number, repeat=repeat))

    print("Time to process query file (no dataset loading, no printout): ")
    print(timeit.repeat("e.process_query_file('" + queries_file + "', False, data_set)", setup=setup_with_loaded_dataset, number=number, repeat=repeat))


def cprofile_benchmark(dataset, queries_file):
    
    print("\n\n\n______PROFILING WITH cProfile (with dataset loading, no printout)______")
    print(" \n**** search_app_base ****\n")
    cProfile.run("base_search.main('" + dataset + "', '" + queries_file + "', False)", sort="time")

    print(" \n**** search_app_improved ****\n")
    cProfile.run("improved_search.main('" + dataset + "', '" + queries_file + "', False)", sort="time")


if __name__ == "__main__":
    main()
