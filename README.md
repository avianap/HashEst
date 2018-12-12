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

### Problem 1 
### Create word occurrence nested dictionary

Implement a function that takes in a dictionary of sentences and outputs a nested dictionary containing word occurances

Input: 
```python
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



```python
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
```
        


#### Problem 2
#### Directly Calculate Jaccard Similarity

Implement a class method that calculates a Jaccard matrix directly from a word occurence matrix

<br>
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/eaef5aa86949f49e7dc6b9c8c3dd8b233332c9e7)


```python
    def direct_jaccard(self):
        """ Calculates the jaccard similarity between doc_1 and doc_2 directly

        Returns:
            float: jaccard similarity between doc_1 and doc_2
        """
        ...

 ```
  
  

#### Problem 3
##### Use Minhashing to Estimate Jaccard Similarity

Implement a function that compares the minimum hashes of each document and tracks the results in a co-occurence array. The co-occurence array can be used to estimate the jaccard similarity.

1. Take multiple hashes of the words in the document
```python
min([hash1("who"), hash1("was"), hash1("the"), hash1("first"), hash1("king"), hash1("of"), hash1("poland")]) 
==
min([hash1("who"), hash1("was"), hash1("the"), hash1("first"), hash1("ruler"), hash1("of"), hash1("poland")]) 

min([hash2("who")... 
```

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

