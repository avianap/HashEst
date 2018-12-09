import itertools
import pandas as pd
import functools
import numpy as np
import random
import hashlib
from sklearn.metrics import jaccard_similarity_score
from hashest import get_words

class jaccard_maker:
    def __init__(self, doc_1, doc_2):
        self.string_dict = {0:doc_1, 1:doc_2}

    def string_dict_to_occur_dict(self):
        """ Calculates a word occurance dataframe from two strings

        Returns:
            dictionary: nested dictionary with outer keys (representing column numbers starting from 0) and inner dictionary key representing each unique word in the vocabulary and values representing a binary for whether that word occurs in the sentence

        Example:
            string_dict = {0: "The cat is grey", 1: "The dog is brown"}
            vocab_dict = {"the":1, "cat":2, "is":3, "grey":4, "dog":5, "brown":6}
            
            occur_dict = {0: {1:1, 2:1, 3:1, 4:1, 5:0, 6:0}, 1: {1:1, 2:0, 3:1, 4:0, 5:1, 6:1}}
            
        """
        tokenized_dict = {k:get_words.tokenize(v) for (k,v) in self.string_dict.items()}
        vocab = tuple(set(itertools.chain.from_iterable(tokenized_dict.values())))
        print('length of vocab is {}'.format(len(vocab)))
        vocab_dict = {v:x+1 for x, v in zip(range(len(vocab)),vocab)}
        coded_dict = {k: [vocab_dict[x] for x in v] for k,v in tokenized_dict.items()}
        occur_dict = {k: {i:int(i in v) for i in vocab_dict.values()} for k,v in coded_dict.items()}
        return(occur_dict)

    def direct_jaccard(self):
        """ Calculates the jaccard similarity between doc_1 and doc_2 directly

        Returns:
            float: jaccard similarity between doc_1 and doc_2 
        """
        occur_dict = self.string_dict_to_occur_dict()
        coded_arrays = {outer_k:np.array([inner_k*inner_v for inner_k,inner_v in occur_dict[outer_k].items()]) for outer_k, outer_v in occur_dict.items()}
        coded_arrays_nonzero = {k:v[np.nonzero(v)] for k,v in coded_arrays.items()}
        intersection = len(np.intersect1d(coded_arrays_nonzero[0], coded_arrays_nonzero[1]))
        union = len(coded_arrays_nonzero[0]) + len(coded_arrays_nonzero[1]) - intersection
        return(intersection/union)

    def permute_jaccard(self, permutations):
        """ Calculates the jaccard similarity between doc_1 and doc_2 using min row numbers from multiple row order permutations

        Args:
            permutations (int): number of times to permute row numbers
        Returns:
            float: jaccard similarity estimate between doc_1 and doc_2
        """
        occur_dict = self.string_dict_to_occur_dict()
        row_num = [x+1 for x in range(len(occur_dict[1]))]
        perm_dict = {k:np.array([]) for k in occur_dict.keys()}
        for i in range(0,permutations):
            random.shuffle(row_num)
            row_num_dict = {k:np.array(list(itertools.chain(occur_dict[k].values())))*row_num for k,v in occur_dict.items()}
            min_row_num_dict = {k:np.ma.min(np.ma.masked_equal(v,0)) for k,v in row_num_dict.items()}
            perm_dict = {k:np.append(v,min_row_num_dict[k]) for k,v in perm_dict.items()}
        co_occur = perm_dict[0]==perm_dict[1]
        return(sum(co_occur)/len(co_occur))

    def hash_jaccard(self, hashes):
        """ Calculates the jaccard similarity between doc_1 and doc_2 using min hash values from multiple hashes

        Args:
            hashes (int): number of hashes to use in jaccard estimation
        Returns: 
            float: jaccard similarity estimate between doc_1 and doc_2
        """
        tokenized_dict = {k:get_words.tokenize(v) for (k,v) in self.string_dict.items()}
        hash_dict = {k:np.array([]) for k in tokenized_dict.keys()}

        def hash_item(word, salt):
            return(int(hashlib.md5((word+str(salt)).encode()).hexdigest(),16))

        def get_min_hash(map_object):
            min_hash_val = np.inf
            for hash_val in map_object:
                if hash_val < min_hash_val:
                    min_hash_val = hash_val
            return(min_hash_val)

        co_occur =  np.array([get_min_hash(map(functools.partial(hash_item, salt = i), tokenized_dict[0])) for i in range(0,hashes)]) == np.array([get_min_hash(map(functools.partial(hash_item, salt = i), tokenized_dict[1])) for i in range(0,hashes)]) 

        return(sum(co_occur)/len(co_occur))


