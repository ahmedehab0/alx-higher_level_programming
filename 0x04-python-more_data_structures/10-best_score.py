#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    best = 0
    best_key = ''
    for keys in a_dictionary.keys():
        if a_dictionary[keys] > best:
            best = a_dictionary[keys]
            best_key = keys
    return best_key
