# HashEst
Estimate Jaccard Similarities Using Min Hashing

In this problem set everything you create should be inside your python package folder 'HashEst'. 

### Problem 1 
### Create a word occurrence nested dictionary

Implement a function that takes in a dictionary of sentences and outputs a nested dictionary containing word occurances

Input: 
```python
{
0: "Who was the first king of Poland?", 
1: "Who was the first ruler of Poland?",
2: "Who was the last pharaoh of Egypt?"}
```

Word Occurence Visualization:

coded representation| vocab         |*0*   |*1*  |*2*  |
|-------------------| ------------- |:----:| ---:| ---:|
|1                  | who           | 1    | 1   | 1   |
|2                  | was           | 1    | 1   | 1   |
|3                  | the           | 1    | 1   | 1   |
|4                  | first         | 1    | 1   | 0   |
|5                  | king          | 1    | 0   | 0   |
|6                  | of            | 1    | 1   | 1   |
|7                  | poland        | 1    | 1   | 0   |
|8                  | last          | 0    | 0   | 1   |
|9                  | ruler         | 0    | 1   | 0   |
|10                 | pharaoh       | 0    | 0   | 1   |
|11                 | egypt         | 0    | 0   | 1   |

Output:
```python
{
0: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 0, 9: 0, 10: 0, 11: 0}, 
1: {1: 1, 2: 1, 3: 1, 4: 1, 5: 0, 6: 1, 7: 1, 8: 0, 9: 1, 10: 0, 11: 0}, 
2: {1: 1, 2: 1, 3: 1, 4: 0, 5: 0, 6: 1, 7: 0, 8: 1, 9: 0, 10: 1, 11: 1}
}
```

```python
class jaccard_maker:
    def __init__(self, string_dict):
        self.string_dict = string_dict

    def string_dict_to_occur_dict(self):
        """ Calculates a word occurance dataframe from a dictionary of strings
        Args:
            string_dict (dict): dict with keys (representing column numbers starting from 0) mapped to values (strings)
        Returns:
            dictionary: nested dictionary with outer keys (representing column numbers starting from 0) and inner dictionary key representing each unique word in the vocabulary and values representing a binary for whether that word occurs in the sentence

        Example:
            string_dict = {0: "The cat is grey", 1: "The dog is brown"}
            vocab_dict = {"the":1, "cat":2, "is":3, "grey":4, "dog":5, "brown":6}
            
            occur_dict = {0: {1:1, 2:1, 3:1, 4:1, 5:0, 6:0}, 1: {1:1, 2:0, 3:1, 4:0, 5:1, 6:1}}
            
        """
        tokenized_dict = #break sentences down into lists of words
        vocab = #find unique words in the vocab
        vocab_dict = #map words to integers
        coded_dict = #map lists of words to corresponding integers
        occur_dict = #create dictionary of coded word occurences
        return(occur_dict)

```

Hints:
* Dictionary comprehensions will be helpful
* [itertools.chain()](https://docs.python.org/2/library/itertools.html#itertools.chain)


#### Problem 2
#### Directly Calculate Jaccard Similarity

Implement a class method that calculates a Jaccard matrix directly from a word occurence matrix
<br>
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/eaef5aa86949f49e7dc6b9c8c3dd8b233332c9e7)


```python
class jaccard_maker:
    ...
    def direct_jaccard(self, occur_df):
        """ Calculates a jaccard matrix of size m x m from a word occurence matrix of size m x n
        Args: 
            co_mat (pd.DataFrame): co-occurence matrix of size m x n
        Returns:
            pandas.DataFrame of size m x m containing jaccard similarities between each row and column combination
        """
        jac_df = #initialize a dataframe of zeros m x m
        #iterate though combos of columns and calculate pairwise jaccard similarities 
        ...
        return(jac_df)
 ```
  
Hints:
* [itertools.product()](https://docs.python.org/2/library/itertools.html#itertools.product) 
* [sklearn.metrics.jaccard_similarity_score()](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_similarity_score.html)


#### Problem 3
#### Use min row number and multiple permutations to estimate Jaccard Similarity

Implement function to estimate jaccard similarity. The function should randomly permute an inputted co-occurrence matrix, save the “min” match value for each permutation for each column to a new matrix-- the signature matrix. The jaccard similarity of columns in the signature matrix will provide a close estimate of the jaccard similarity between columns of the co-occurrence matrix.

| perm 1        | perm 2        | perm 3        | perm 4        | word          | *A*  | *B* | *C* |
|---------------|---------------|---------------|---------------| ------------- |:----:| ---:| ---:|
| 1             | 9             | 3             | 9             | who           | 1    | 1   | 1   |
| 2             | 4             | 5             | 11            | was           | 1    | 1   | 1   |
| 3             | 1             | 7             | 4             | the           | 1    | 1   | 1   |
| 4             | 10            | 2             | 5             | first         | 1    | 1   | 0   |
| 5             | 3             | 10            | 1             | king          | 1    | 0   | 0   |
| 6             | 7             | 9             | 8             | of            | 1    | 1   | 1   |
| 11            | 6             | 4             | 2             | poland        | 1    | 1   | 0   |
| 7             | 5             | 11            | 7             | ruler         | 0    | 1   | 0   |
| 8             | 2             | 8             | 10            | last          | 0    | 0   | 1   |
| 9             | 8             | 1             | 3             | pharaoh       | 0    | 0   | 1   |
| 10            | 11            | 6             | 6             | egypt         | 0    | 0   | 1   |

Signature Matrix

|permutation|*A*|*B*|*C*|
| ------ | - | - | - |
| perm 1 | 1 | 1 | 1 |
| perm 2 | 1 | 1 | 1 |
| perm 3 | 2 | 2 | 1 |
| perm 4 | 1 | 2 | 3 |

```python
def permute_jaccard(co_mat, permutations = 100):
  """ Calculates a jaccard matrix of size m x m from a co-occurence matrix of size m x n using min row numbers from multiple permutations
  Args:
    co_mat (pd.DataFrame): co-occurence matrix
    permutations (int): number of times to permute matrix
  Returns:
     pandas.DataFrame of size m x m containing jaccard similarities between each row and column combination
   """
 
  for i in permutations:
    df = df.sample(n=len(df), frac = 1, replace = False, random_state = i)
    df.multiply(df.index.values, axis = 1)
    df.replace(to_replace = 0, value = np.nan, inplace = True)
    vals = []
    for col in df.cols:
      col_values = df[col].values.dropnas()
      vals.append(col_values[0])
    min_vals_df.append(vals)
    
 sim_df = pd.DataFrame() #empty square df of size m x m
 for i,j in min_vals_df: #same logic from question 2
  jaccard_score = jaccard_similarity_score(df[i],df[j])
  sim_df.loc[[i,j]] = jaccard_score
  sim_df.loc[[j,i]] = jaccard_score
  
  ```


