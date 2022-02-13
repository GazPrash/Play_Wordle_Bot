from math import log2
import pandas as pd
import numpy as np

# data = []
# words = []

# with open("data/long_freqs.txt", "r") as file:
#     for line in file.readlines():
#         word, fq = line.split()
#         try:
#             words.append(word)
#             data.append(float(fq))
#         except Exception as e:
#             print(e)        

# with open("data/short_freqs.txt", "r") as file:
#     for line in file.readlines():
#         word, fq = line.split()
#         try:
#             words.append(word)
#             data.append(float(fq))
#         except Exception as e:
#             print(e)        

# word_freq = pd.DataFrame()
# word_freq["Word"] = words
# word_freq["Freq"] = data
# word_freq["Prob"] = [100 * x for x in data]
# word_freq.index = np.arange(1, len(data)+1)
# # print(word_freq)

def entropy_function(selection, word_freq):
    # Entropy (H) = p(x) * log2(1/p(x))
    res_information = {}
    for word in word_freq["Word"]:
        word = word.lower()
        if word in selection:
            p_x = float(word_freq[word_freq["Word"] == word]["Prob"])
            entropy =  p_x * log2(1/p_x) 
            res_information[word] = entropy

    sorted_information:list = sorted(res_information.items(), key = lambda x : x[1], reverse= True)
    return sorted_information




