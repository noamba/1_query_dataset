import timeit
import search_app_improved as e


 
def average_dict_width(dictionary):

    dictionary_length = len(dictionary)

    total_values = 1
    for v in dictionary.values():
        total_values += len(v)    

    return dictionary_length, total_values/dictionary_length

def main():
    
    #dataset = 'data/mini.csv'
    dataset = 'data/search_dataset.csv'
    queries_file = 'queries/queries.txt'

    # print avg dictionary width (wider means slower)
    items_by_keyword_start, items_by_id, items_original_form = e.load_dataset(dataset)
    length, width = average_dict_width(items_by_keyword_start)
    print("\n\nDict entries: ", length) 
    print("Avg. keywprd start dictionary width: ", width)
    
    # find number of queries  to be processed:
    with open(queries_file) as f:
        print("\nNumber ofqueries: ",  sum(1 for _ in f))
    
    # Benchmark:

    number=1 # times the tested function is run for timing
    repeat=2 # test is repeated to get multiple results 

    print("\n**** Dataset as List ****")
    setup = "import search_app_base as e"
    setup_with_loaded_dataset = setup + "; data_set = e.load_dataset('" + dataset + "')"

    print("Time to load dataset: ")
    print(timeit.repeat("e.load_dataset('" + dataset + "')", setup=setup, number=number, repeat=repeat))

    print("Time to process query file without printing output: ")
    print(timeit.repeat("e.process_query_file('" + queries_file + "', False, data_set)", setup=setup_with_loaded_dataset, number=number, repeat=repeat))


    print("\n\n**** Dataset as Dictionaries ****")
    setup = "import search_app_improved as e"
    setup_with_loaded_dataset = setup + "; data_set = e.load_dataset('" + dataset + "')"

    print("Time to load dataset: ")
    print(timeit.repeat("e.load_dataset('" + dataset + "')", setup=setup, number=number, repeat=repeat))


    print("Time to process query file without printing output: ")
    print(timeit.repeat("e.process_query_file('" + queries_file + "', False, data_set)", setup=setup_with_loaded_dataset, number=number, repeat=repeat))


    print("\n\n**** In Cython! ****")
    setup = "import c_search_app_improved as e"
    setup_with_loaded_dataset = setup + "; data_set = e.load_dataset('data/search_dataset.csv')"

    print("Time to load dataset: ")
    print(timeit.repeat("e.load_dataset('" + dataset + "')", setup=setup, number=number, repeat=repeat))

    print("Time to process query file without printing output: ")
    print(timeit.repeat("e.process_query_file('" + queries_file + "', False, data_set)", setup=setup_with_loaded_dataset, number=number, repeat=repeat))

if __name__ == "__main__":
    main()
