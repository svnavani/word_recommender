import sys, os, urllib.request

def initalize_english_dictionary():
	# make a set of english vocab for fast lookup
	english_vocab = set()
	data = urllib.request.urlopen('https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt')
	
	for line in data:
		english_vocab.add(line[:-1].decode('UTF-8'))

	return english_vocab

# helper method to see if a word is in the dictionary
def in_english_dict(word, english_vocab):
	return True if word in english_vocab else False


def initialize_word_list(directory, english_vocab):

	# words in all the text files
	words = str()

	# go through text files in the directory
	for filename in os.listdir(directory):
		if (filename.startswith('')): # the program takes a while so this filters which text files are used
			file = open(os.path.join(directory, filename), 'r')
			print(filename)

			# turn the text into lowercase and append it to all the words
			file_text = file.read().lower()
			words = words + file_text

	temp = str()
	words = words.split(' ')
	
	# filtering the words to only words that are in the english dictionary
	# reduces wierd symbols and punctuation
	for index in range(len(words)):
		word = words[index]
		if in_english_dict(word, english_vocab):
			print(len(words) - index) # used to estimate how much time is left
			temp = temp + ' ' + word
		else:
			print(len(words) - index)

		
	words = temp
	return words.split(' ')


def initalize_dictionary(words):

	curr_word_dict = dict()
	for index in range(len(words) - 1):
		# initialize current word and next word
		curr_word = words[index]
		next_word = words[index + 1]

		# if the current word has been seen
		if curr_word in curr_word_dict.keys():
			inner_dict = curr_word_dict[curr_word]
			if next_word in inner_dict.keys(): # if the next word has been seen
				inner_dict[next_word] += 1
			else: # if the next word has not been seen
				inner_dict[next_word] = 1
		else: # if the current word has not been seen
			# create a new dictionary of the next word and assign it to the current word
			curr_word_dict[curr_word] = {next_word: 1}


	return curr_word_dict

def find_recommendation(word, curr_word_dict):
	if word in curr_word_dict.keys():
		inner_dict = curr_word_dict[word]
		recommendation = max(inner_dict, key=inner_dict.get)
		if recommendation == '':
			recommendation = 'Empty String'
	else:
		recommendation = 'No recommendation'

	return recommendation

if __name__ == '__main__':
	#directory = './slurp-master/text'
	directory = './text/'
	english_vocab = initalize_english_dictionary()
	words = initialize_word_list(directory, english_vocab)
	curr_word_dict = initalize_dictionary(words)

	# comment out if you don't want to see the dictionary
	print(curr_word_dict)

	inp = input('Enter a word: ')
	while inp != 'q':
		print(find_recommendation(inp, curr_word_dict))
		inp = input('Enter a word: ')