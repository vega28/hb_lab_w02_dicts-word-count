# Pseudocode
# open file 
# read in file by line
# parse each line - for each line: split by spaces
#   for each word in the line: check if it is in the dictionary and count up
# return or print the wordcount at the end

def count_words_dict(filename):
        the_file = open(filename)
        word_counts = {}
        for line in the_file:
            # punctuation = ['.', ',', '!', '?', ':', ';', '/', '-', '_', '"', "'"]
            punctuation = """.,!?:;/-_"'"""
            line = line.strip('/n')
            words = line.split(' ') # this is a list
            for word in words: # word is the key 
                word = word.lower()
                word = word.strip(punctuation)
                word_counts[word] = word_counts.get(word, 0) + 1
        for word in word_counts:
            print(word, word_counts[word])
        print(punctuation)

            
        

count_words_dict('test.txt')
