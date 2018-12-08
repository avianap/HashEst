import time
from hashest import hashest
from hashest import get_words

string_dict = {0: "Who was the first king of Poland?", 1: "Who was the first ruler of Poland?", 2: "Who was the last pharaoh of Egypt?"}
print(string_dict)

start = time.time()
j = hashest.jaccard_maker(string_dict)
occur_dict = j.string_dict_to_occur_dict()
end = time.time()
print(occur_dict)
print(end-start)


start = time.time()
jac_df = j.direct_jaccard(occur_dict)
end = time.time()
print(jac_df)
print(end-start)


start = time.time()
jac_est_df = j.permute_jaccard(occur_dict, permutations = 10000)
end = time.time()
print(jac_est_df)
print(end-start)


start = time.time()
jac_hash_est_df = j.hash_jaccard(string_dict, hashes = 10000)
end = time.time()
print(jac_hash_est_df)
print(end-start)
