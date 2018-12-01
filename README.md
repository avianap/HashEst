# HashEst
Estimate Jaccard Similarities Using Min Hashing

#### Problem 1 
##### Create a co-occurrence matrix

Implement a function that takes in sentences and outputs a co-occurence matrix

Input:
```{A: "Who was the first king of Poland?",
    B: "Who was the first ruler of Poland?"
    C: "Who was the last pharaoh of Egypt?"
    }
```

Output:

|word           |*A*   |*B*  |*C*  |
| ------------- |:----:| ---:| ---:|
| who           | 1    | 1   | 1   |
| was           | 1    | 1   | 1   |
| the           | 1    | 1   | 1   |
| first         | 1    | 1   | 0   |
| king          | 1    | 0   | 0   |
| of            | 1    | 1   | 1   |
| poland        | 1    | 1   | 0   |
| last          | 0    | 0   | 1   |
| ruler         | 0    | 1   | 0   |
| pharaoh       | 0    | 0   | 1   |
| egypt         | 0    | 0   | 1   |

```python
import pandas as pd

def sentence_dict_to_matrix(string_dict):
  """ Calculates co-occurance matrix for dictionary of strings
  Args:
    string_dict (dict): dict with keys mapped to values that are strings of words
  Returns:
    pandas.DataFrame with columns corresponding to the dictionary key of each element in the string_dict and rows for each unique word in the string_dict’s values
  """


```

#### Problem 2
##### Directly Calculate Jaccard Similarity

Implement a function that calculates a Jaccard matrix directly
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/eaef5aa86949f49e7dc6b9c8c3dd8b233332c9e7)


```python

def direct_jaccard(co_mat):
  """ Calculates a jaccard matrix of size m x m from a co-occurence matrix of size m x n
  Args: 
    co_mat (pd.DataFrame): co-occurence matrix of size m x n
  Returns:
    pandas.DataFrame of size m x m containing jaccard similarities between each row and column combination
  """
 ```
  
Hints:
itertools.combinations() 
sklearn.metrics.jaccard_similarity_score()


#### Problem 3
##### Use min row number and multiple permutations to estimate Jaccard Similarity

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

|permutation| A | B | C |
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


