# Pseudocode:
#   open file 
#   read in file by line
#   parse each line - for each line: split by spaces
#     for each word in the line: check if it is in the dictionary and count up
#   return or print the wordcount at the end

def count_words_dict(filename):
    """ Count the number of instances of each word in a text file. """

    the_file = open(filename)
    word_counts = {}

    for line in the_file: # parse each line
        punctuation = """.,!?:;/-_"'"""
        line = line.strip('\n')
        words = line.split(' ') # this is a list

        for word in words: # word is the key 
            # sanitize input:
            word = word.lower()
            word = word.strip(punctuation) 

            # tick up the counts for the words in ths line:
            word_counts[word] = word_counts.get(word, 0) + 1

    # print output:
    for word in word_counts:
        print(word, word_counts[word])
           
        

count_words_dict('test.txt')
