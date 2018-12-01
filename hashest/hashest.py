import itertools
import pandas as pd
from hashest import get_words

class jaccard_maker:
    def __init__(self, string_dict):
        self.string_dict = string_dict

    def string_dict_to_matrix(self):
        """ Calculates co-occurance matrix for dictionary of strings
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






