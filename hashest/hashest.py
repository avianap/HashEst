import itertools
import pandas as pd
import numpy as np
import random
from sklearn.metrics import jaccard_similarity_score
from hashest import get_words

class jaccard_maker:
    def __init__(self, string_dict):
        self.string_dict = string_dict

    def string_dict_to_occur_dict(self):
        """ Calculates a word occurance dataframe from a dictionary of strings
        Args:
            string_dict (dict): dict with keys (counting from 0 to len-1) mapped to values that are strings of words
        Returns:
            --EDIT pandas.DataFrame with columns corresponding to the dictionary key of each element in the string_dict and rows for each unique word in the string_dict’s values
        """
        tokenized_dict = {k:get_words.tokenize(v) for (k,v) in self.string_dict.items()}
        vocab = tuple(set(itertools.chain.from_iterable(tokenized_dict.values())))
        vocab_dict = {v:x+1 for x, v in zip(range(len(vocab)),vocab)}
        coded_dict = {k: [vocab_dict[x] for x in v] for k,v in tokenized_dict.items()}
        occur_dict = {k: {i:int(i in v) for i in vocab_dict.values()} for k,v in coded_dict.items()}
        return(occur_dict)

    def direct_jaccard(self, occur_dict):
        """ Calculates a jaccard matrix of size m x m from a word occurence dictionary of size m x n
        Args: 
            occur_dict (dictionary): nested dictionary of length m with dictionaries as values containing keys = words and values = occurence boolean
        Returns:
            pandas.DataFrame of size m x m containing jaccard similarities between each row and column combination
        """
        jac_df = pd.DataFrame(np.zeros((len(occur_dict), len(occur_dict)))) 
        for x in itertools.product(occur_dict.keys(), occur_dict.keys()): 
            coded_occur = [k*v for k,v in occur_dict[x[0]].items()] 
            coded_occur_mask = np.ma.masked_equal(np.array(coded_occur),0)
            import pdb; pdb.set_trace()
            jac_df.iat[x[0],x[1]] = jaccard_similarity_score(np.ma.masked_equal(np.array([k*v for k,v in occur_dict[x[0]].items()]),0), np.ma.masked_equal(np.array([k*v for k,v in occur_dict[x[1]].items()]),0))
            #mask is not working, drop zeros instead
        return(jac_df)

    def permute_jaccard(self, occur_dict, permutations):
        """ Calculates a jaccard matrix of size m x m from a word occurence nested dictionary of size m x n using min row numbers from multiple row order permutations
        Args:
            occur_dict (dictionary): word occurence nested dictionary 
            permutations (int): number of times to permute row numbers
        Returns:
            pandas.DataFrame of size m x m containing jaccard similarities between each row and column combination
        """
        row_num = [x+1 for x in range(len(occur_dict[1]))]
        perm_dict = {k:np.array([]) for k in occur_dict.keys()}
        for i in range(0,permutations):
            random.shuffle(row_num)
            row_num_dict = {k:np.array(list(itertools.chain(occur_dict[k].values())))*row_num for k,v in occur_dict.items()}
            min_row_num_dict = {k:np.ma.min(np.ma.masked_equal(v,0)) for k,v in row_num_dict.items()}
            perm_dict = {k:np.append(v,min_row_num_dict[k]) for k,v in perm_dict.items()}
        jac_df = pd.DataFrame(np.zeros((len(perm_dict),len(perm_dict))))
        for x in itertools.product(perm_dict.keys(),perm_dict.keys()):
            co_occur = (perm_dict[x[0]]==perm_dict[x[1]]).astype(int)
            jac_df.iat[x[0],x[1]] = sum(co_occur)/len(co_occur)
        #sim_df = pd.DataFrame() #empty square df of size m x m
        #for i,j in min_vals_df: #same logic from question 2
        #    jaccard_score = jaccard_similarity_score(df[i],df[j])
        #    sim_df.loc[[i,j]] = jaccard_score
        #    sim_df.loc[[j,i]] = jaccard_score



