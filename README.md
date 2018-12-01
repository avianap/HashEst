# HashEst
Estimate Jaccard Similarities Using Min Hashing

#### Problem 1 
##### Create a co-occurrence matrix

Implement a function that takes in sentences and outputs a co-occurence matrix

Input:
  1. Who was the first king of Poland?
  2. Who was the first ruler of Poland?
  3. Who was the last pharaoh of egypt?

Output:

|               | 1    | 2   | 3   |
| ------------- |:----:| ---:| ---:|
| who           | 1    | 1   | 1   |
| was           | 1    | 1   | 1   |
| the           | 1    | 1   | 1   |
| first         | 1    | 1   | 1   |
| king          | 1    | 1   | 1   |
| of            | 1    | 1   | 1   |
| poland        | 1    | 1   | 1   |
| last          | 1    | 1   | 1   |
| pharaoh       | 1    | 1   | 1   |
| egypt         | 1    | 1   | 1   |

```python
import pandas as pd

def sentence_dict_to_matrix(string_dict):
  """ Calculates co-occurance matrix for dictionary of strings
  Args:
    string_dict (dict): dict with keys mapped to values that are strings of words
  Returns:
    object: a pandas dataframe with columns corresponding to the dictionary key of each element in the string_dict and rows for each unique word in the string_dict’s values
  """


```

#### Problem 2
##### Directly Calculate Jaccard Similarity

Implement a function that calculates a Jaccard matrix directly
J(X,Y) = |X \cap Y| / |X \cup Y|

```python

def direct_jaccard(co_mat):
  """ Calculates a jaccard matrix of size mxm from a co-occurence matrix of size m x n
  Args: 
    co_mat (pd.DataFrame): co-occurence matrix of size m x n
  Returns:
    object: a pandas dataframe of size m x m 
