# open file 
# read in file by line
# parse each line - for each line: split by spaces
#   for each word in the line: check if it is in the dictionary and count up
# return or print the wordcount at the end

def count_words_dict(filename):
        the_file = open(filename)
        for line in the_file:
            line = line.strip('\n')
            words = line.split(' ')
            print(line) ###
            print(words)
        # word_counts: {}
        # for word in phrase:
        #     word[letter] = letter_counts.get(letter, 0) + 1
        # return word

count_words_dict('test.txt')