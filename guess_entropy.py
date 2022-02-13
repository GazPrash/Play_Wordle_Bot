from math import log2


def entropy_function(selection, word_freq):
    # Entropy (H) = p(x) * log2(1/p(x))
    res_information = {}
    for word in word_freq["Word"]:
        word = word.lower()
        if word in selection:
            p_x = float(word_freq[word_freq["Word"] == word]["Prob"])
            entropy = p_x * log2(1 / p_x)
            res_information[word] = entropy

    sorted_information: list = sorted(
        res_information.items(), key=lambda x: x[1], reverse=True
    )
    return sorted_information
