
# coding: utf-8

# In[1]:

import re


# In[2]:

str = "'Furious 7' is a glorious overcompensation, a film so concerned about its rampant machismo that the casual viewer might miss how it Tokyo-drifts atop soap opera bubbles. Like Lee Daniels' hit TV drama 'Empire,' 'Furious 7' is stuffed with situations that require go-for-broke absurdity, but even Daniels and his nighttime soap predecessor Aaron Spelling would pause before attempting the level of 'get the f—k outta here!' style shenanigans director James Wan and writer Chris Morgan employ."


# In[3]:

def unigram(source):
    #lowercase the input string
    source = source.lower()
    #remove the delimiters
    source = re.sub(r"[^\w\s]", '', source)
    #split the input string on whitespace
    array = source.split()
    #create a dictionary which will maintain the unigram tokens and their frequency
    unigram = dict()
    #loop through the array to generate unigrams and put the unigram token and it's frequency in dictionary
    for i in range(0,len(array)):
        token = array[i]
        if token in unigram:
            unigram[token] = unigram[token] + 1
        else:
            unigram[token] = 1
    return unigram;  


# In[4]:

def bigram(source):
    #lowercase the input string
    source = source.lower()
    #remove the delimiters
    source = re.sub(r"[^\w\s]", '', source)
    #split the input string on whitespace
    array = source.split()
    #create a dictionary which will maintain the bigram tokens and their frequency
    bigram = dict()
    #loop through the array to generate bigrams and put the bigram token and it's frequency in dictionary
    for i in range(0,len(array)-1):
        token1 = array[i]
        token2 = array[i+1]
        bigram_token = token1 + " " +token2
        if bigram_token in bigram:
            bigram[bigram_token] = bigram[bigram_token] + 1
        else:
            bigram[bigram_token] = 1
    return bigram;  


# In[5]:

#Sum of all the frequency values present in the dictionary
def getTotalFrequency(dictionary):
    total_count = 0
    for key, value in dictionary.iteritems():
        total_count += value
    return total_count;        


# In[22]:

#Computes and returns the probability of a token in a corpus. The ngram_type could take values as 'unigram' and 'bigram' 
#to generate corresponding tokens from the corpus.
def computeProbability(corpus,token,ngram_type):
    probability = 0.0
    if ngram_type == "unigram":
        unigram_dict = unigram(corpus)
        if token in unigram_dict:
            frequency = unigram_dict[token]
            total_count = float(getTotalFrequency(unigram_dict))
            probability = frequency/total_count
        else:
            print "Token Not Found!!!"
    elif ngram_type == "bigram":
        bigram_dict = bigram(corpus)
        if token in bigram_dict:
            frequency = bigram_dict[token]
            total_count = float(getTotalFrequency(bigram_dict))
            probability = frequency/total_count
        else:
            print "Token Not Found!!!"
    return probability;
    


# In[7]:

print unigram(str)


# In[8]:

print bigram(str)


# In[24]:

print computeProbability(str,"furious","unigram")


# In[23]:

print computeProbability(str,"furious 7","bigram")

