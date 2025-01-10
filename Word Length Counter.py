file = input('What is the file name?\n')

import os


def word_counter(file):
    data = ()
    with open(file, 'r') as test:
        storage = test.read()
        #print(storage)
        start = 0
        
        for word in storage.split():
            print(word)
            if len(word) > start:
                start = len(word)
            else:
                continue
    return(start)

def word_tally(file, length_of_longest_word):
        i = 1
        count = 0
        total = 0
        with open(file, 'r') as test:
            storage = test.read()
        while i <= length_of_longest_word:
            for word in storage.split(): 
                if len(word) == i:
                    total += 1
            #print(total)
            print(f'There are {total} {i} letter words in {file}') 
            i += 1
            total = 0 
            

            #else:
                #continue
                #start += 1
        #print(start)

#word_counter(file)
word_tally('kadowk.txt', word_counter('kadowk.txt'))

def file_creator(file):
    try:
        with open(file, 'r') as test:
            print('File Exist!')
    except:
        with open(file, 'a') as test:
            print('File Empty!')
#file_creator(file)

#def count_words(file):
    #with open(file, 'r') as test:
        #for 