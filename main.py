import time
import random
from hashest import hashest
from hashest import get_words

#with open('doc_1.txt') as f:
#    doc_1 = f.read()
#with open('doc_2.txt') as f:
#    doc_2 = f.read()

x = random.sample(range(20000), 10000)
y = random.sample(range(40000), 30000)

doc_1 = ' '.join(str(e) for e in x)
doc_2 = ' '.join(str(e) for e in y)


#doc_1 = "1 2 3 4 5 6"
#doc_2 = "1 2 3 4 5 7"

j = hashest.jaccard_maker(doc_1, doc_2)

start = time.time()
jac_sim = j.direct_jaccard()
end = time.time()
print("direct jaccard = {}".format(jac_sim))
print(end-start)


start = time.time()
jac_est_df = j.permute_jaccard(permutations = 100)
end = time.time()
print("row perm jaccard = {}".format(jac_est_df))
print(end-start)


start = time.time()
jac_hash_est_df = j.hash_jaccard(hashes = 100)
end = time.time()
print("hash jaccard = {}".format(jac_hash_est_df))
print(end-start)
