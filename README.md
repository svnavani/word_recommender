# word_recommender

word_recommeder.py is designed to recommend a word that should come after a word previously typed. My inspiration for this was how my keyboard will recommend three words for me for every word I type.

The algorithm take all words in a file, and sees what is the most common words that comes after a word. It creates a hashmap of hashpmaps. The the outter hashmap will map a word to the word an frequency of all the words that come after that word. The inner hashmap contains the words and their frequencies that follow a certain word

To run the algorithm just type in the text file or import your own text file(s) into the 'text' directory. In the code there is an option for the user to filter certain text files as the program will take a lot of time to finish executing for a large amount of words.

Since the hashmap of hashmaps takes a while to load, this would idealy be computed once and then you would just search for the word you are trying to find a recommendation for.
