import time
import random
from hashest import hashest
from hashest import get_words

x = random.sample(range(50000), 40000)
y = random.sample(range(90000), 40000)

doc_1 = ' '.join(str(e) for e in x)
doc_2 = ' '.join(str(e) for e in y)

j = hashest.jaccard_maker(doc_1, doc_2)

start = time.time()
jac_sim = j.direct_jaccard()
end = time.time()
print("direct jaccard = {}".format(jac_sim))
print(end-start)


start = time.time()
jac_hash_est_df = j.hash_jaccard(hashes = 200)
end = time.time()
print("hash jaccard = {}".format(jac_hash_est_df))
print(end-start)
