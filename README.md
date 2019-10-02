# word_recommender

word_recommeder.py recommends words after a previous word is typed. I was inspired by how my phone's keyboard recommends three words for every word I type. 

The algorithm takes all the words from a file, and finds the next logical word to recommend. It creates a hashmap of hashpmaps. The outer hashmap takes a word and maps it to the word and frequency of all recommendations. The inner hashmap contains the recommendations and their frequencies for following a certain word. 

To run the algorithm, just type in the text file or import your own text file(s) into the 'text' directory. In the code, there is an option for the user to filter certain text files since the program can take a large amount of time to finish executing for large word amounts.

Since the hashmap of hashmaps takes a while to load, this would ideally be computed once. Then you would just search for the word you are trying to find a recommendation for.
