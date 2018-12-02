import itertools
import pandas as pd
import numpy as np
from sklearn.metrics import jaccard_similarity_score
from hashest import get_words

class jaccard_maker:
    def __init__(self, string_dict):
        self.string_dict = string_dict

    def string_dict_to_occur_df(self):
        """ Calculates a word occurance dataframe from a dictionary of strings
        Args:
            string_dict (dict): dict with keys mapped to values that are strings of words
        Returns:
            pandas.DataFrame with columns corresponding to the dictionary key of each element in the string_dict and rows for each unique word in the string_dict’s values
        """
        tokenized_dict = {k:get_words.tokenize(v) for (k,v) in self.string_dict.items()}
        vocab = tuple(set(itertools.chain.from_iterable(tokenized_dict.values())))
        occur_dict = {k: [int(i in v) for i in vocab] for k,v in tokenized_dict.items()}
        df = pd.DataFrame.from_dict(occur_dict, orient = 'columns')
        df['vocab'] = vocab
        df.set_index('vocab', inplace = True)
        return(df)

    def direct_jaccard(self, occur_df):
        """ Calculates a jaccard matrix of size m x m from a word occurence matrix of size m x n
        Args: 
            co_mat (pd.DataFrame): co-occurence matrix of size m x n
        Returns:
            pandas.DataFrame of size m x m containing jaccard similarities between each row and column combination
        """
        jac_df = pd.DataFrame(np.zeros((occur_df.shape[1], occur_df.shape[1])))
        for x in itertools.product(range(0,occur_df.shape[1]), range(0,occur_df.shape[1])):
            jac_df.iat[x[0],x[1]] = jaccard_similarity_score(occur_df.iloc[:,x[0]].values, occur_df.iloc[:,x[1]].values)
        return(jac_df)




