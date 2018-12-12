# HashEst
Estimate Jaccard Similarities Using Min Hashing

#### Problem 1 
##### Create a co-occurrence matrix

Implement a function that takes in two documents and outputs a co-occurence matrix

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
        ...

```



#### Problem 2
##### Directly Calculate Jaccard Similarity

Implement a function that calculates a Jaccard matrix directly 
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

Implement a function compares the minimum hashes of each document and tracks the results in a co-occurence array. The co-occurence array can be used to estimate the jaccard similarity.

1. Take muliple hashes of each word 

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

