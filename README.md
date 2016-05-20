# query_dataset

*****
Runs on Python 3
*****

This is an exercise with a 'dataset search engine'. The goal was to 
get the best matches for a list of queries against a dataset. A further goal was to 
optimize search time (while dataset loading time was not important). 

Three versions were created and analyzed:
* search_app_base (the naive approach), using a list for all dataset items
* search_app_improved, using dictionaries and sets to improve search time
* c_search_app_improved, a cythonised version of the improved code to optimize further with c code.

The last version's search is more than 10 times faster than in the first solution. 
For convenience and interest the output of the performance analysis is 
provided below. 

The program takes two files as input: 
* A text file with queries (i.e. keywords to search for), one query per line. 
* A csv dataset file with one clothing item per line. Each item 
  consists of 3 elements [id, item, brand]. There are close to 70,000 items. 

Scoring is based on: 
* Number of unigram keyword occurrences in an entry 
* Full match (non-case sensitive) 
* Partial match on word beginning 

Output: 
* Query (keywords) 
* Number of matches or partial matches for this query in the dataseta 
* Top ten items matched, ordered by descending score 

Performance analysis includes: 
* Timings 
* Profiles
 
To install and run on linux: 

```
Install git and virtualenv, then issue:
mkdir somedir
cd somedir
virtualenv -p python3 envdir
git clone https://github.com/noamba/1_query_dataset codedir
cd codedir
source ../envdir/bin/activate 
pip3 install -r requirements.txt
```

That's it. 
Run any file ending with .py while activated with: 

```
python3 name_of_file.py
```

To run the cythonised c_search_app_improved you will need to import it as done in efficiency_analysis.py

------

Following is the output of efficiency_analysis.py: 

```
______General descriptive information_______

    Number of queries (lines) in queries file (queries/queries.txt):  2
    Number of items (lines) in dataset file (data/search_dataset.csv):  69258

Descriptive information for search_app_improved: 

    Keyword (first letters) Dictionary entries:  5151
    Keyword (first letters) Dictionary avg. width (wider is slower):  70.60726072607261


________TIMINGS with timeit_________

**** Dataset as List (search_app_base) ****
Time to load dataset: 
[0.07699599300030968, 0.06918929500170634]
Time to process query file (no dataset loading, no printout): 
[1.0237973209987103, 1.002753077998932]


**** Dataset as Dictionaries (search_app_improved)****
Time to load dataset: 
[1.2686008180025965, 1.2663522990005731]
Time to process query file (no dataset loading, no printout): 
[0.10782761800146545, 0.10076834500068799]


**** In Cython (cythonised search_app_improved) ****
Time to load dataset: 
[1.2343492600011814, 1.24061114199867]
Time to process query file (no dataset loading, no printout): 
[0.07990729900120641, 0.08037057500041556]



______PROFILING WITH cProfile (with dataset loading, no printout)______
 
**** search_app_base ****

         9970501 function calls in 2.207 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   138514    1.323    0.000    2.046    0.000 search_app_base.py:88(calculate_score_1)
  7689080    0.463    0.000    0.463    0.000 {method 'lower' of 'str' objects}
  1918240    0.210    0.000    0.210    0.000 {method 'startswith' of 'str' objects}
    69258    0.082    0.000    0.084    0.000 search_app_base.py:37(<genexpr>)
        2    0.062    0.031    2.109    1.054 search_app_base.py:50(process_query)
   138516    0.049    0.000    0.049    0.000 {method 'split' of 'str' objects}
        1    0.007    0.007    2.207    2.207 <string>:1(<module>)
        1    0.006    0.006    0.090    0.090 search_app_base.py:32(load_dataset)
      380    0.002    0.000    0.002    0.000 {built-in method utf_8_decode}
        1    0.001    0.001    2.200    2.200 search_app_base.py:27(main)
     8057    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
     8057    0.001    0.000    0.001    0.000 {built-in method len}
      380    0.000    0.000    0.002    0.000 codecs.py:316(decode)
        2    0.000    0.000    0.000    0.000 {built-in method open}
        1    0.000    0.000    2.207    2.207 {built-in method exec}
        1    0.000    0.000    2.109    2.109 search_app_base.py:42(process_query_file)
        2    0.000    0.000    0.000    0.000 {built-in method nl_langinfo}
        2    0.000    0.000    0.000    0.000 _bootlocale.py:23(getpreferredencoding)
        2    0.000    0.000    0.000    0.000 codecs.py:306(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method reader}
        2    0.000    0.000    0.000    0.000 codecs.py:257(__init__)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


 
**** search_app_improved ****

         977969 function calls in 1.650 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    1.263    1.263    1.389    1.389 search_app_improved.py:13(load_dataset)
        1    0.102    0.102    1.650    1.650 <string>:1(<module>)
    16572    0.079    0.000    0.128    0.000 search_app_improved.py:97(_find_match)
   366261    0.068    0.000    0.068    0.000 {method 'add' of 'set' objects}
    69260    0.034    0.000    0.034    0.000 {method 'split' of 'str' objects}
   237756    0.026    0.000    0.026    0.000 {method 'startswith' of 'str' objects}
    74464    0.017    0.000    0.017    0.000 {method 'copy' of 'set' objects}
        2    0.016    0.008    0.157    0.079 search_app_improved.py:52(_process_one_query)
     8292    0.011    0.000    0.140    0.000 search_app_improved.py:74(_calculate_score)
    69258    0.010    0.000    0.010    0.000 {method 'join' of 'str' objects}
    69260    0.010    0.000    0.010    0.000 {method 'lower' of 'str' objects}
    33144    0.004    0.000    0.004    0.000 {method 'copy' of 'list' objects}
      379    0.003    0.000    0.003    0.000 {built-in method utf_8_decode}
        1    0.001    0.001    0.159    0.159 search_app_improved.py:46(process_query_file)
     8283    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
     8061    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
     8292    0.001    0.000    0.001    0.000 {built-in method len}
        5    0.001    0.000    0.001    0.000 {method 'update' of 'set' objects}
     8283    0.001    0.000    0.001    0.000 {method 'remove' of 'set' objects}
      379    0.001    0.000    0.004    0.000 codecs.py:316(decode)
        2    0.000    0.000    0.000    0.000 {built-in method open}
        1    0.000    0.000    1.650    1.650 {built-in method exec}
        1    0.000    0.000    1.548    1.548 search_app_improved.py:8(main)
        2    0.000    0.000    0.000    0.000 _bootlocale.py:23(getpreferredencoding)
        2    0.000    0.000    0.000    0.000 {built-in method nl_langinfo}
        1    0.000    0.000    0.000    0.000 __init__.py:28(get_stop_words)
        2    0.000    0.000    0.000    0.000 codecs.py:306(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method reader}
        2    0.000    0.000    0.000    0.000 codecs.py:257(__init__)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


 
**** cythonised c_search_app_improved ****

         771 function calls in 1.389 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    1.386    1.386    1.389    1.389 {c_search_app_improved.main}
      379    0.002    0.000    0.002    0.000 {built-in method utf_8_decode}
      379    0.001    0.000    0.003    0.000 codecs.py:316(decode)
        1    0.000    0.000    1.389    1.389 {built-in method exec}
        2    0.000    0.000    0.000    0.000 {built-in method nl_langinfo}
        2    0.000    0.000    0.000    0.000 _bootlocale.py:23(getpreferredencoding)
        1    0.000    0.000    1.389    1.389 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 __init__.py:28(get_stop_words)
        2    0.000    0.000    0.000    0.000 codecs.py:306(__init__)
        2    0.000    0.000    0.000    0.000 codecs.py:257(__init__)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

```


