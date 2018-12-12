# HashEst
Estimate Jaccard Similarities Using Min Hashing

#### Setup

* Create a main.py file for running your hashest/hashest.py module
* Reuse the tokenize words function you created for your previous pset

```python
import random
from hashest import hashest
from hashest import get_words

x = random.sample(range(50000), 40000)
y = random.sample(range(90000), 40000)

doc_1 = ' '.join(str(e) for e in x)
doc_2 = ' '.join(str(e) for e in y)

j = hashest.jaccard_maker(doc_1, doc_2)

jac_sim = j.direct_jaccard()
print("direct jaccard = {}".format(jac_sim))

jac_hash_est_df = j.hash_jaccard(hashes = 200)
print("hash jaccard = {}".format(jac_hash_est_df))
```

#### Problem 1 
##### Create a co-occurrence matrix

Implement a function that takes in two documents and outputs a co-occurence matrix
=======
In this problem set everything you create should be inside your python package folder 'HashEst'. 

### Problem 1 
### Create a word occurrence nested dictionary
>>>>>>> solutions

Implement a function that takes in a dictionary of sentences and outputs a nested dictionary containing word occurances

Input: 
```python
<<<<<<< HEAD
doc_1 = "Who was the first king of Poland?"
doc_2 = "Who was the first ruler of Poland?"
```

Output:

```python
{0 : {1:1, 2;1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:0}, 1 : {1:1, 2;1, 3:1, 4:1, 5:1, 6:1, 7:0, 8:1} }
```
Representing: 

|row number| vocab         |*0*   |*1*  |
|----------| ------------- |:----:| ---:| 
|1         | who           | 1    | 1   |
|2         | was           | 1    | 1   |
|3         | the           | 1    | 1   |
|4         | first         | 1    | 1   |
|5         | king          | 1    | 0   |
|6         | of            | 1    | 1   |
|7         | poland        | 1    | 1   |
|8         | ruler         | 0    | 1   |

=======
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
>>>>>>> solutions

Output:
```python
<<<<<<< HEAD
class jaccard_maker:
    def __init__(self, doc_1, doc_2):
        self.string_dict = {0:doc_1, 1:doc_2}

    def string_dict_to_occur_dict(self):
        """ Calculates a word occurance dataframe from two strings

        Returns:
            dictionary: nested dictionary with outer keys (representing each document) mapped to dictionaries with keys representing each unique word in the vocabulary and values representing a binary for whether that word occurs in the sentence

        Example:
            string_dict = {0: "The cat is grey", 1: "The dog is brown"}
            vocab_dict = {"the":1, "cat":2, "is":3, "grey":4, "dog":5, "brown":6}

            occur_dict = {0: {1:1, 2:1, 3:1, 4:1, 5:0, 6:0}, 1: {1:1, 2:0, 3:1, 4:0, 5:1, 6:1}}

        """
        ...

```

=======
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
>>>>>>> solutions


#### Problem 2
#### Directly Calculate Jaccard Similarity

<<<<<<< HEAD
Implement a function that calculates a Jaccard matrix directly 
=======
Implement a class method that calculates a Jaccard matrix directly from a word occurence matrix
>>>>>>> solutions
<br>
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/eaef5aa86949f49e7dc6b9c8c3dd8b233332c9e7)


```python
<<<<<<< HEAD

    def direct_jaccard(self):
        """ Calculates the jaccard similarity between doc_1 and doc_2 directly

        Returns:
            float: jaccard similarity between doc_1 and doc_2
        """
        ...

 ```
  
  

#### Problem 3
##### Use Minhashing to Estimate Jaccard Similarity

Implement a function compares the minimum hashes of each document and tracks the results in a co-occurence array. The co-occurence array can be used to estimate the jaccard similarity.

1. Take muliple hashes of each word 
=======
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
>>>>>>> solutions

| Hash 1        | Hash 2        | Hash 3        | Hash 4        | vocab         | *0*  | *1* |
|---------------|---------------|---------------|---------------| ------------- |:----:| ---:|
| 151           | 898           | 339           | 616           | who           | 1    | 1   |
| 244           | 493           | 596           | 357           | was           | 1    | 1   |
| 357           | 124           | 608           | 419           | the           | 1    | 1   |
| 404           | 263           | 211           | 544           | first         | 1    | 1   |
| 590           | 316           | 160           | 123           | king          | 1    | 0   |
| 675           | 739           | 845           | 881           | of            | 1    | 1   |
| 743           | 628           | 438           | 245           | poland        | 1    | 1   |
| 811           | 543           | 721           | 755           | ruler         | 0    | 1   |

2. Calculate a co-occurence array
```python
co-occur = [1,1,0,0...
```
3. Use the co-occurence array to calculate a jaccard estimate:
```python
output = sum(co-occur)/len(co-occur)
```


```python
    def hash_jaccard(self, hashes):
        """ Calculates the jaccard similarity between doc_1 and doc_2 using min hash values from multiple hashes

        Args:
            hashes (int): number of hashes to use in jaccard estimation
        Returns:
            float: jaccard similarity estimate between doc_1 and doc_2
        """
        ...
        
        return(sum(co_occur)/len(co_occur))
  ```

Hints
* Use salt to create different hashes
* `functools.partial()` 

